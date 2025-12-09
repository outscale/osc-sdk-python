from .authentication import Authentication
from .authentication import DEFAULT_USER_AGENT
from .credentials import Profile
from .requester import Requester
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib3.util import parse_url

import json
import warnings

MAX_RETRIES = "3"
RETRY_BACKOFF_FACTOR = "1"
RETRY_BACKOFF_JITTER = "3"
RETRY_BACKOFF_MAX = "30"

class Call(object):
    def __init__(self, logger=None, limiter=None, **kwargs):
        self.version = kwargs.pop("version", "latest")
        self.host = kwargs.pop("host", None)
        self.ssl = kwargs.pop("_ssl", True)
        self.user_agent = kwargs.pop("user_agent", DEFAULT_USER_AGENT)
        self.logger = logger
        self.limiter = limiter
        kwargs = self.update_limiter(**kwargs)
        kwargs = self.update_adapter(**kwargs)
        self.update_profile(**kwargs)
        self.session = Session()
        self.session.mount("https://", self.adapter)
        self.session.mount("http://", self.adapter)

    def update_credentials(self, **kwargs):
        warnings.warn(
            "update_credentials is deprecated, use update_profile instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.update_profile(**kwargs)

    def update_adapter(self, **kwargs):
        self.adapter = HTTPAdapter(
            max_retries=Retry(
                total=int(kwargs.pop("max_retries", MAX_RETRIES)),
                backoff_factor=float(kwargs.pop("retry_backoff_factor", RETRY_BACKOFF_FACTOR)),
                backoff_jitter=float(kwargs.pop("retry_backoff_jitter", RETRY_BACKOFF_JITTER)),
                backoff_max=float(kwargs.pop("retry_backoff_max", RETRY_BACKOFF_MAX)),
                status_forcelist=(400, 429, 500, 503),
                allowed_methods=("POST", "GET"),
            )
        )
        return kwargs

    def update_profile(self, **kwargs):
        self.profile = Profile.from_standard_configuration(
            kwargs.pop("path", None), kwargs.pop("profile", None)
        )
        self.profile.merge(Profile(**kwargs))
        return kwargs

    def update_limiter(
        self,
        **kwargs
    ):
        limiter_window = kwargs.pop("limiter_window", None)
        if limiter_window is not None:
            self.limiter.window = limiter_window

        limiter_max_requests = kwargs.pop("limiter_max_requests", None)
        if limiter_max_requests is not None:
            self.limiter.max_requests = limiter_max_requests

        return kwargs

    def api(self, action, service="api", **data):
        try:
            endpoint = self.profile.get_endpoint(service) + "/" + action
            parsed_url = parse_url(endpoint)
            uri = parsed_url.path
            host = parsed_url.host

            if self.limiter is not None:
                self.limiter.acquire()

            requester = Requester(
                self.session,
                Authentication(
                    self.profile,
                    host,
                    user_agent=self.user_agent,
                ),
                endpoint,
            )
            if self.logger is not None:
                self.logger.do_log(
                    "uri: " + uri + "\npayload:\n" + json.dumps(data, indent=2)
                )
            return requester.send(uri, json.dumps(data))
        except Exception as err:
            raise err

    def close(self):
        if self.session:
            self.session.close()
