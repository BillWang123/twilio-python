import json
from math import ceil
from twilio import values
from twilio.exceptions import TwilioException
from twilio.rest.page import Page


class Domain(object):
    def __init__(self, twilio):
        """
        :param Twilio twilio:
        :return:
        """
        self.twilio = twilio
        self.base_url = None

    def request(self, method, uri, params=None, data=None, headers=None,
                auth=None, timeout=None, allow_redirects=False):
        url = '{}/{}'.format(self.base_url.strip('/'), uri.strip('/'))
        return self.twilio.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )


class Version(object):
    MAX_PAGE_SIZE = 1000

    META_KEYS = {
        'end',
        'first_page_uri',
        'next_page_uri',
        'last_page_uri',
        'page',
        'page_size',
        'previous_page_uri',
        'total',
        'num_pages',
        'start',
        'uri'
    }

    def __init__(self, domain):
        """
        :param Domain domain:
        :return:
        """
        self.domain = domain
        self.version = None

    def request(self, method, uri, params=None, data=None, headers=None,
                auth=None, timeout=None, allow_redirects=False):
        url = '{}/{}'.format(self.version.strip('/'), uri.strip('/'))
        return self.domain.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    def fetch(self, instance, instance_kwargs, method, uri, params=None, data=None, headers=None,
              auth=None, timeout=None, allow_redirects=False):
        response = self.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        if response.status_code != 200:
            raise TwilioException('Unable to fetch record')

        payload = json.loads(response.content)

        return instance(self, payload, **instance_kwargs)

    def update(self, instance, instance_kwargs, method, uri, params=None, data=None, headers=None,
               auth=None, timeout=None, allow_redirects=False):
        response = self.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        if response.status_code != 200:
            raise TwilioException('Unable to update record')

        payload = json.loads(response.content)

        return instance(self, payload, **instance_kwargs)

    def delete(self, method, uri, params=None, data=None, headers=None, auth=None, timeout=None,
               allow_redirects=False):
        response = self.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
        )

        if 500 <= response.status_code < 600:
            raise TwilioException('Unable to delete record')

        return response.status_code == 204

    def read_limits(self, limit=None, page_size=None):
        page_limit = values.unset

        if limit is not None:

            if page_size is None:
                # If there is no user-specified page_size, pick the most network efficient size
                page_size = min(limit, self.MAX_PAGE_SIZE)

            page_limit = int(ceil(limit / float(page_size)))

        return {
            'limit': limit or values.unset,
            'page_size': page_size or values.unset,
            'page_limit': page_limit,
        }

    def stream(self, pager, instance, instance_kwargs, method, uri, limit, page_limit, **kwargs):
        current_record = 1
        current_page = 1
        page = self.page(pager, instance, instance_kwargs, method, uri, **kwargs)
        for record in page:
            yield record
            current_record += 1

        while True:
            if page_limit and page_limit <= current_page:
                break

            page = page.next_page()
            if not page:
                break

            for record in page:
                yield record
                current_record += 1
                if limit and limit <= current_record:
                    break

            current_page += 1

    def page(self, pager, instance, instance_kwargs, method, uri, **kwargs):
        response = self.request(method, uri, **kwargs)

        if response.status_code != 200:
            raise TwilioException('Unable to fetch page')

        payload = json.loads(response.content)
        records = self.load_page(payload)
        previous_page_url = self.previous_page_url(payload)
        next_page_url = self.next_page_url(payload)

        return Page(
            self,
            pager,
            instance,
            instance_kwargs,
            previous_page_url,
            next_page_url,
            records
        )

    def previous_page_url(self, payload):
        if 'meta' in payload and 'previous_page_url' in payload['meta']:
            return payload['meta']['previous_page_url']
        elif 'previous_page_uri' in payload:
            return payload['previous_page_uri']

        return None

    def next_page_url(self, payload):
        if 'meta' in payload and 'next_page_url' in payload['meta']:
            return payload['meta']['next_page_url']
        elif 'next_page_uri' in payload:
            return payload['next_page_uri']

        return None

    def load_page(self, payload):
        if 'meta' in payload and 'key' in payload['meta']:
            return payload[payload['meta']['key']]
        else:
            keys = set(payload.keys())
            key = keys - self.META_KEYS
            if len(key) == 1:
                return payload[key.pop()]

        raise TwilioException('Page Records can not be deserialized')

    def create(self, instance, instance_kwargs, method, uri, **kwargs):
        response = self.request(method, uri, **kwargs)

        if response.status_code not in [200, 201]:
            raise TwilioException('[{}] Unable to create record\n{}'.format(response.status_code,
                                                                            response.content))

        payload = json.loads(response.content)
        return instance(self, payload, **instance_kwargs)


class ListResource(object):
    def __init__(self, version):
        """
        :param Version version:
        """
        self._version = version
        """ :type: Version """


class InstanceContext(object):
    def __init__(self, version):
        """
        :param Version version:
        """
        self._version = version
        """ :type: Version """


class InstanceResource(object):
    def __init__(self, version):
        """
        :param Version version:
        """
        self._version = version
        """ :type: Version """
