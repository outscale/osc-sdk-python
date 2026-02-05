from .authentication import Authentication
from .authentication import DEFAULT_USER_AGENT
from .credentials import Profile
from .requester import Requester
from requests import Session
from urllib3.util import parse_url
from datetime import timedelta
from .limiter import RateLimiter

import json
import warnings


class Call(object):
    def __init__(self, logger=None, limiter=None, **kwargs):
        self.version = kwargs.pop("version", "latest")
        self.host = kwargs.pop("host", None)
        self.ssl = kwargs.pop("_ssl", True)
        self.user_agent = kwargs.pop("user_agent", DEFAULT_USER_AGENT)
        self.logger = logger
        self.limiter: RateLimiter | None = limiter
        self.retry_kwargs = {}
        self.session = Session()

        kwargs = self.update_limiter(**kwargs)
        kwargs = self.update_retry(**kwargs)
        self.update_profile(**kwargs)

    def update_credentials(self, **kwargs):
        warnings.warn(
            "update_credentials is deprecated, use update_profile instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.update_profile(**kwargs)

    def update_profile(self, **kwargs):
        self.profile = Profile.from_standard_configuration(
            kwargs.pop("path", None), kwargs.pop("profile", None)
        )
        self.profile.merge(Profile(**kwargs))
        return kwargs

    def update_limiter(self, **kwargs):
        limiter_window = kwargs.pop("limiter_window", None)
        if limiter_window is not None and self.limiter is not None:
            self.limiter.window = timedelta(seconds=int(limiter_window))

        limiter_max_requests = kwargs.pop("limiter_max_requests", None)
        if limiter_max_requests is not None and self.limiter is not None:
            self.limiter.max_requests = limiter_max_requests

        return kwargs

    def update_retry(self, **kwargs):
        max_retries = kwargs.pop("max_retries", None)
        if max_retries is not None:
            self.retry_kwargs["max_retries"] = int(max_retries)

        for key in ["backoff_factor", "backoff_jitter", "backoff_max"]:
            value = kwargs.pop(f"retry_{key}", None)
            if value is not None:
                self.retry_kwargs[key] = float(value)
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
                **self.retry_kwargs,
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
