# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class AllTimeList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the AllTimeList
        
        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: AllTimeList
        :rtype: AllTimeList
        """
        super(AllTimeList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Usage/Records/AllTime'.format(**self._kwargs)

    def stream(self, limit=None, page_size=None, **kwargs):
        """
        Streams AllTimeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            AllTimeInstance,
            {},
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        """
        Reads AllTimeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        """
        Retrieve a single page of AllTimeInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of AllTimeInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            AllTimeInstance,
            {},
            'GET',
            self._uri,
            params=params,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AllTimeList>'


class AllTimeInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the AllTimeInstance
        
        :returns: AllTimeInstance
        :rtype: AllTimeInstance
        """
        super(AllTimeInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'category': payload['category'],
            'count': payload['count'],
            'count_unit': payload['count_unit'],
            'description': payload['description'],
            'end_date': deserialize.rfc2822_datetime(payload['end_date']),
            'price': deserialize.decimal(payload['price']),
            'price_unit': payload['price_unit'],
            'start_date': deserialize.rfc2822_datetime(payload['start_date']),
            'subresource_uris': payload['subresource_uris'],
            'uri': payload['uri'],
            'usage': payload['usage'],
            'usage_unit': payload['usage_unit'],
        }

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The api_version
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def category(self):
        """
        :returns: The category
        :rtype: all_time.category
        """
        return self._properties['category']

    @property
    def count(self):
        """
        :returns: The count
        :rtype: unicode
        """
        return self._properties['count']

    @property
    def count_unit(self):
        """
        :returns: The count_unit
        :rtype: unicode
        """
        return self._properties['count_unit']

    @property
    def description(self):
        """
        :returns: The description
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def end_date(self):
        """
        :returns: The end_date
        :rtype: datetime
        """
        return self._properties['end_date']

    @property
    def price(self):
        """
        :returns: The price
        :rtype: unicode
        """
        return self._properties['price']

    @property
    def price_unit(self):
        """
        :returns: The price_unit
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def start_date(self):
        """
        :returns: The start_date
        :rtype: datetime
        """
        return self._properties['start_date']

    @property
    def subresource_uris(self):
        """
        :returns: The subresource_uris
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def usage(self):
        """
        :returns: The usage
        :rtype: unicode
        """
        return self._properties['usage']

    @property
    def usage_unit(self):
        """
        :returns: The usage_unit
        :rtype: unicode
        """
        return self._properties['usage_unit']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AllTimeInstance>'
