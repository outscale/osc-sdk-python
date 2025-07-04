# -*- coding: utf-8 -*-
from .authentication import Authentication
from .authentication import DEFAULT_USER_AGENT
from .credentials import Credentials
from .requester import Requester

import json
import os


class Call(object):
    def __init__(self, logger=None, **kwargs):
        self.version = kwargs.pop("version", "latest")
        self.host = kwargs.pop("host", None)
        self.ssl = kwargs.pop("_ssl", True)
        self.user_agent = kwargs.pop("user_agent", DEFAULT_USER_AGENT)
        self.logger = logger
        self.update_credentials(
            access_key=kwargs.pop("access_key", None),
            secret_key=kwargs.pop("secret_key", None),
            region=kwargs.pop("region", None),
            profile=kwargs.pop("profile", None),
            email=kwargs.pop("email", None),
            password=kwargs.pop("password", None),
            proxy=kwargs.pop("proxy", None),
            x509_client_cert=kwargs.pop("x509_client_cert", None),
            max_retries=kwargs.pop("max_retries", None),
            retry_backoff_factor=kwargs.pop("retry_backoff_factor", None),
            retry_backoff_jitter=kwargs.pop("retry_backoff_jitter", None)
        )

    def update_credentials(
        self,
        region=None,
        profile=None,
        access_key=None,
        secret_key=None,
        email=None,
        password=None,
        proxy=None,
        x509_client_cert=None,
        max_retries=None,
        retry_backoff_factor=None,
        retry_backoff_jitter=None,
    ):
        self.credentials = {
            "access_key": access_key,
            "secret_key": secret_key,
            "region": region,
            "profile": profile,
            "email": email,
            "password": password,
            "x509_client_cert": x509_client_cert,
            "max_retries": max_retries,
            "retry_backoff_factor": retry_backoff_factor,
            "retry_backoff_jitter": retry_backoff_jitter,
        }

    def api(self, action, **data):
        try:
            credentials = Credentials(**self.credentials)
            host = (
                self.host
                if self.host
                else "api.{}.outscale.{}".format(
                    credentials.region, credentials.get_url_extension()
                )
            )
            uri = "/api/{}/{}".format(self.version, action)
            protocol = "https" if self.ssl else "http"

            endpoint = os.environ.get("OSC_ENDPOINT_API")
            if endpoint is None:
                endpoint = "{}://{}{}".format(protocol, host, uri)
            else:
                endpoint = "{}{}".format(endpoint, uri)

            requester = Requester(
                Authentication(credentials, host, user_agent=self.user_agent),
                endpoint,
                credentials.max_retries,
                credentials.retry_backoff_factor,
                credentials.retry_backoff_jitter,
            )
            if self.logger != None:
                self.logger.do_log(
                    "uri: " + uri + "\npayload:\n" + json.dumps(data, indent=2)
                )
            return requester.send(uri, json.dumps(data))
        except Exception as err:
            raise err
