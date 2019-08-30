# -*- coding: utf-8 -*-
from .authentication import Authentication
from .credentials import Credentials
from .requester import Requester
import json


class Call(object):
    def __init__(self, **kwargs):
        self.credentials = {'access_key': kwargs.pop('access_key', None),
                            'secret_key': kwargs.pop('secret_key', None),
                            'region': kwargs.pop('region', None),
                            'profile': kwargs.pop('profile', 'default')}
        self.version = kwargs.pop('version', 'latest')
        self.host = kwargs.pop('host', None)
        self.ssl = kwargs.pop('_ssl', True)

    def api(self, action, **data):
        try:
            credentials = Credentials(**self.credentials)
            host = (self.host if self.host
                    else 'api.{}.outscale.{}'.format(credentials.get_region(), credentials.get_url_extension()))
            uri = '/api/{}/{}'.format(self.version, action)
            protocol = 'https' if self.ssl else 'http'
            endpoint = '{protocol}://{host}{uri}'.format(**locals())

            requester = Requester(Authentication(credentials, host), endpoint)
            return requester.send(uri, json.dumps(data))
        except Exception as err:
            raise err
