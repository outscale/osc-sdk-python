import json
import warnings
from datetime import timedelta
from urllib.parse import urlencode

import httpx
from urllib3.util import parse_url

from .requester import AsyncRequester
from ...authentication import Authentication, DEFAULT_USER_AGENT
from ...credentials import Profile
from ...limiter import RateLimiter
from ..request import RequestSpec


class AsyncCall(object):
    def __init__(self, logger=None, limiter=None, **kwargs):
        self.version = kwargs.pop("version", "latest")
        self.host = kwargs.pop("host", None)
        self.ssl = kwargs.pop("_ssl", True)
        self.user_agent = kwargs.pop("user_agent", DEFAULT_USER_AGENT)
        self.logger = logger
        self.limiter: RateLimiter | None = limiter
        self.retry_kwargs = {}

        kwargs = self.update_limiter(**kwargs)
        kwargs = self.update_retry(**kwargs)
        self.update_profile(**kwargs)
        self.client = self._make_client()

    def _make_client(self):
        cert_file = self.profile.x509_client_cert
        return httpx.AsyncClient(
            trust_env=False,
            verify=not self.profile.tls_skip_verify,
            cert=cert_file,
        )

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

    async def request(self, spec: RequestSpec, path_params=None):
        path = spec.resolved_path(path_params)
        endpoint = (
            self.profile.get_endpoint(spec.service).rstrip("/") + "/" + path.lstrip("/")
        )
        parsed_url = parse_url(endpoint)
        uri = parsed_url.path
        host = parsed_url.host
        canonical_querystring = urlencode(
            sorted((spec.query_params or {}).items()), doseq=True
        )
        payload = "" if spec.json_body is None else json.dumps(spec.json_body)

        if self.limiter is not None:
            await self.limiter.async_acquire()

        requester = AsyncRequester(
            self.client,
            Authentication(
                self.profile,
                host,
                method=spec.method.upper(),
                service=spec.service,
                user_agent=self.user_agent,
            ),
            endpoint,
            **self.retry_kwargs,
        )
        if self.logger is not None:
            self.logger.do_log(
                "uri: "
                + uri
                + "\npayload:\n"
                + json.dumps(spec.json_body, indent=2)
            )
        response = await requester.send(
            spec.method.upper(),
            uri,
            payload,
            query_params=spec.query_params,
            canonical_querystring=canonical_querystring,
        )
        return response.json()

    async def api(self, action, service="api", **data):
        return await self.request(
            RequestSpec(
                service=service,
                method="POST",
                path="/" + action,
                json_body=data,
            )
        )

    async def close(self):
        if self.client:
            await self.client.aclose()
