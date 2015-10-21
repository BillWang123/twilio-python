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


class MobileList(ListResource):

    def __init__(self, version, owner_account_sid):
        """
        Initialize the MobileList
        
        :param Version version: Version that contains the resource
        :param owner_account_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: MobileList
        :rtype: MobileList
        """
        super(MobileList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'owner_account_sid': owner_account_sid,
        }
        self._uri = '/Accounts/{owner_account_sid}/IncomingPhoneNumbers/Mobile.json'.format(**self._kwargs)

    def stream(self, beta=values.unset, friendly_name=values.unset,
               phone_number=values.unset, limit=None, page_size=None, **kwargs):
        """
        Streams MobileInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param bool beta: The beta
        :param unicode friendly_name: The friendly_name
        :param unicode phone_number: The phone_number
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
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            MobileInstance,
            {},
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, limit=None, page_size=None, **kwargs):
        """
        Reads MobileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param bool beta: The beta
        :param unicode friendly_name: The friendly_name
        :param unicode phone_number: The phone_number
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
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        """
        Retrieve a single page of MobileInstance records from the API.
        Request is executed immediately
        
        :param bool beta: The beta
        :param unicode friendly_name: The friendly_name
        :param unicode phone_number: The phone_number
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of MobileInstance
        :rtype: Page
        """
        params = values.of({
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            MobileInstance,
            {},
            'GET',
            self._uri,
            params=params,
        )

    def create(self, area_code, phone_number, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset):
        """
        Create a new MobileInstance
        
        :param unicode area_code: The area_code
        :param unicode phone_number: The phone_number
        :param unicode api_version: The api_version
        :param unicode friendly_name: The friendly_name
        :param unicode sms_application_sid: The sms_application_sid
        :param unicode sms_fallback_method: The sms_fallback_method
        :param unicode sms_fallback_url: The sms_fallback_url
        :param unicode sms_method: The sms_method
        :param unicode sms_url: The sms_url
        :param unicode status_callback: The status_callback
        :param unicode status_callback_method: The status_callback_method
        :param unicode voice_application_sid: The voice_application_sid
        :param bool voice_caller_id_lookup: The voice_caller_id_lookup
        :param unicode voice_fallback_method: The voice_fallback_method
        :param unicode voice_fallback_url: The voice_fallback_url
        :param unicode voice_method: The voice_method
        :param unicode voice_url: The voice_url
        
        :returns: Newly created MobileInstance
        :rtype: MobileInstance
        """
        data = values.of({
            'AreaCode': area_code,
            'PhoneNumber': phone_number,
            'ApiVersion': api_version,
            'FriendlyName': friendly_name,
            'SmsApplicationSid': sms_application_sid,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceApplicationSid': voice_application_sid,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
        })
        
        return self._version.create(
            MobileInstance,
            {},
            'POST',
            self._uri,
            data=data,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MobileList>'


class MobileInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the MobileInstance
        
        :returns: MobileInstance
        :rtype: MobileInstance
        """
        super(MobileInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'address_requirements': payload['address_requirements'],
            'api_version': payload['api_version'],
            'beta': payload['beta'],
            'capabilities': payload['capabilities'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'phone_number': payload['phone_number'],
            'sid': payload['sid'],
            'sms_application_sid': payload['sms_application_sid'],
            'sms_fallback_method': payload['sms_fallback_method'],
            'sms_fallback_url': payload['sms_fallback_url'],
            'sms_method': payload['sms_method'],
            'sms_url': payload['sms_url'],
            'status_callback': payload['status_callback'],
            'status_callback_method': payload['status_callback_method'],
            'uri': payload['uri'],
            'voice_application_sid': payload['voice_application_sid'],
            'voice_caller_id_lookup': payload['voice_caller_id_lookup'],
            'voice_fallback_method': payload['voice_fallback_method'],
            'voice_fallback_url': payload['voice_fallback_url'],
            'voice_method': payload['voice_method'],
            'voice_url': payload['voice_url'],
        }

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def address_requirements(self):
        """
        :returns: The address_requirements
        :rtype: mobile.address_requirement
        """
        return self._properties['address_requirements']

    @property
    def api_version(self):
        """
        :returns: The api_version
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def beta(self):
        """
        :returns: The beta
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def capabilities(self):
        """
        :returns: The capabilities
        :rtype: unicode
        """
        return self._properties['capabilities']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def phone_number(self):
        """
        :returns: The phone_number
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def sms_application_sid(self):
        """
        :returns: The sms_application_sid
        :rtype: unicode
        """
        return self._properties['sms_application_sid']

    @property
    def sms_fallback_method(self):
        """
        :returns: The sms_fallback_method
        :rtype: unicode
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: The sms_fallback_url
        :rtype: unicode
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: The sms_method
        :rtype: unicode
        """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """
        :returns: The sms_url
        :rtype: unicode
        """
        return self._properties['sms_url']

    @property
    def status_callback(self):
        """
        :returns: The status_callback
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The status_callback_method
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def voice_application_sid(self):
        """
        :returns: The voice_application_sid
        :rtype: unicode
        """
        return self._properties['voice_application_sid']

    @property
    def voice_caller_id_lookup(self):
        """
        :returns: The voice_caller_id_lookup
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']

    @property
    def voice_fallback_method(self):
        """
        :returns: The voice_fallback_method
        :rtype: unicode
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: The voice_fallback_url
        :rtype: unicode
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: The voice_method
        :rtype: unicode
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: The voice_url
        :rtype: unicode
        """
        return self._properties['voice_url']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MobileInstance>'
