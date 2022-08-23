# -*- coding: utf-8 -*-
from .authentication import Authentication
from .authentication import DEFAULT_USER_AGENT
from .credentials import Credentials
from .requester import Requester
import json

class Call(object):
    def __init__(self, logger=None, **kwargs):
        self.credentials = {'access_key': kwargs.pop('access_key', None),
                            'secret_key': kwargs.pop('secret_key', None),
                            'region': kwargs.pop('region', None),
                            'profile': kwargs.pop('profile', None)}
        self.version = kwargs.pop('version', 'latest')
        self.host = kwargs.pop('host', None)
        self.ssl = kwargs.pop('_ssl', True)
        self.user_agent = kwargs.pop("user_agent", DEFAULT_USER_AGENT)
        self.logger = logger

    def api(self, action, **data):
        try:
            credentials = Credentials(**self.credentials)
            host = (self.host if self.host
                    else 'api.{}.outscale.{}'.format(credentials.region, credentials.get_url_extension()))
            uri = '/api/{}/{}'.format(self.version, action)
            protocol = 'https' if self.ssl else 'http'
            endpoint = '{}://{}{}'.format(protocol, host, uri)

            requester = Requester(Authentication(credentials, host, user_agent=self.user_agent), endpoint)
            if self.logger != None:
                self.logger.do_log("uri: " + uri + "\npayload:\n" + json.dumps(data, indent=2))
            return requester.send(uri, json.dumps(data))
        except Exception as err:
            raise err
