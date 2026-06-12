import asyncio
import base64
import hashlib
import hmac
import json
import random
import time
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from threading import Lock
from urllib.parse import urlencode

import httpx

from ..problem import LegacyProblem, LegacyProblemDecoder, Problem, ProblemDecoder
from ..version import get_version

MAX_RETRIES = 3
RETRY_BACKOFF_FACTOR = 1.0
RETRY_BACKOFF_JITTER = 3.0
RETRY_BACKOFF_MAX = 30.0
DEFAULT_USER_AGENT = "osc-sdk-python/" + get_version()


class RateLimiter:
    def __init__(self, window: timedelta, max_requests: int, datetime_cls=datetime):
        self.datetime_cls = datetime_cls
        self.window: timedelta = window
        self.max_requests: int = max_requests
        self.requests = []
        self._lock = Lock()
        self._async_lock = None

    def acquire(self):
        with self._lock:
            now = self.datetime_cls.now(timezone.utc)

            self.clean_old_requests(now)

            if len(self.requests) >= self.max_requests:
                oldest = self.requests[0]
                wait_time = self.window - (now - oldest)
                time.sleep(wait_time.total_seconds())

                now = self.datetime_cls.now(timezone.utc)
                self.clean_old_requests(now)

            self.requests.append(now)

    async def async_acquire(self):
        if self._async_lock is None:
            self._async_lock = asyncio.Lock()

        async with self._async_lock:
            now = self.datetime_cls.now(timezone.utc)

            self.clean_old_requests(now)

            if len(self.requests) >= self.max_requests:
                oldest = self.requests[0]
                wait_time = self.window - (now - oldest)
                await asyncio.sleep(wait_time.total_seconds())

                now = self.datetime_cls.now(timezone.utc)
                self.clean_old_requests(now)

            self.requests.append(now)

    def clean_old_requests(self, now):
        while len(self.requests) > 0 and self.requests[0] <= now - self.window:
            self.requests.pop(0)


class SdkAuth(httpx.Auth):
    def __init__(
        self,
        profile,
        *,
        service="api",
        content_type="application/json; charset=utf-8",
        algorithm="OSC4-HMAC-SHA256",
        signed_headers="content-type;host;x-osc-date",
        user_agent=None,
    ):
        if service in profile.iam_v2_services:
            self.access_key = profile.access_key_v2
            self.secret_key = profile.secret_key_v2
        else:
            self.access_key = profile.access_key
            self.secret_key = profile.secret_key
        self.login = profile.login
        self.password = profile.password
        self.region = profile.region
        self.service = service
        self.content_type = content_type
        self.algorithm = algorithm
        self.signed_headers = signed_headers
        self.user_agent = user_agent or DEFAULT_USER_AGENT

    def auth_flow(self, request: httpx.Request):
        if self.service == "oks":
            request.headers.update(self.forge_headers_oks())
        elif self.is_basic_auth_configured():
            request.headers.update(self.get_basic_auth_header())
        else:
            request.headers.update(self.forge_headers_signed(request))
        yield request

    def forge_headers_signed(self, request: httpx.Request):
        date_iso, date = self.build_dates()
        credential_scope = f"{date}/{self.region}/{self.service}/osc4_request"
        canonical_request = self.build_canonical_request(request, date_iso)
        str_to_sign = self.create_string_to_sign(
            date_iso,
            credential_scope,
            canonical_request,
        )
        signature = self.compute_signature(date, str_to_sign)
        return {
            "Content-Type": self.content_type,
            "X-Osc-Date": date_iso,
            "Authorization": self.build_authorization_header(
                credential_scope,
                signature,
            ),
            "User-Agent": self.user_agent,
        }

    def forge_headers_oks(self):
        return {
            "AccessKey": self.access_key,
            "SecretKey": self.secret_key,
            "User-Agent": self.user_agent,
        }

    def build_dates(self):
        now = datetime.now(timezone.utc)
        return now.strftime("%Y%m%dT%H%M%SZ"), now.strftime("%Y%m%d")

    def sign(self, key, msg):
        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

    def get_signature_key(self, key, date_stamp_value):
        k_date = self.sign(("OSC4" + key).encode("utf-8"), date_stamp_value)
        k_region = self.sign(k_date, self.region)
        k_service = self.sign(k_region, self.service)
        return self.sign(k_service, "osc4_request")

    def build_canonical_request(self, request: httpx.Request, date_iso: str):
        canonical_headers = (
            f"content-type:{self.content_type}\n"
            f"host:{request.url.host}\n"
            f"x-osc-date:{date_iso}\n"
        )
        canonical_querystring = urlencode(
            sorted(request.url.params.multi_items()),
            doseq=True,
        )
        payload_hash = hashlib.sha256(request.content).hexdigest()
        return (
            f"{request.method}\n"
            f"{request.url.path}\n"
            f"{canonical_querystring}\n"
            f"{canonical_headers}\n"
            f"{self.signed_headers}\n"
            f"{payload_hash}"
        )

    def create_string_to_sign(self, date_iso, credential_scope, canonical_request):
        return (
            f"{self.algorithm}\n"
            f"{date_iso}\n"
            f"{credential_scope}\n"
            f"{hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()}"
        )

    def compute_signature(self, date, string_to_sign):
        signing_key = self.get_signature_key(self.secret_key, date)
        return hmac.new(
            signing_key,
            string_to_sign.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

    def build_authorization_header(self, credential_scope, signature):
        return (
            f"{self.algorithm} "
            f"Credential={self.access_key}/{credential_scope}, "
            f"SignedHeaders={self.signed_headers}, "
            f"Signature={signature}"
        )

    def is_basic_auth_configured(self):
        return self.login is not None and self.password is not None

    def get_basic_auth_header(self):
        if not self.is_basic_auth_configured():
            raise Exception("email or password not set")
        creds = f"{self.login}:{self.password}"
        b64_creds = base64.b64encode(creds.encode("utf-8")).decode("utf-8")
        date_iso, _ = self.build_dates()
        return {
            "Content-Type": self.content_type,
            "X-Osc-Date": date_iso,
            "Authorization": "Basic " + b64_creds,
        }


class RetryPolicy:
    def __init__(
        self,
        *,
        max_retries=MAX_RETRIES,
        backoff_factor=RETRY_BACKOFF_FACTOR,
        backoff_jitter=RETRY_BACKOFF_JITTER,
        backoff_max=RETRY_BACKOFF_MAX,
    ):
        self.max_retries = int(max_retries)
        self.backoff_factor = float(backoff_factor)
        self.backoff_jitter = float(backoff_jitter)
        self.backoff_max = float(backoff_max)

    def should_retry(self, error: httpx.HTTPError, attempt: int) -> bool:
        if isinstance(error, httpx.TooManyRedirects):
            return False
        if isinstance(error, httpx.InvalidURL | httpx.UnsupportedProtocol):
            return False

        response = getattr(error, "response", None)
        if response is not None:
            if 400 <= response.status_code < 500 and response.status_code != 429:
                return False
        return attempt < self.max_retries

    def backoff_time(self, attempt: int) -> float:
        backoff = self.backoff_factor * (2**attempt)
        backoff += random.uniform(0, self.backoff_jitter)
        return min(backoff, self.backoff_max)

    def retry_after_time(self, error: httpx.HTTPError):
        response = getattr(error, "response", None)
        if response is None:
            return None

        retry_after = response.headers.get("Retry-After")
        if retry_after is None:
            return None

        try:
            return max(0.0, float(retry_after))
        except ValueError:
            pass

        try:
            retry_date = parsedate_to_datetime(retry_after)
        except (TypeError, ValueError):
            return None

        if retry_date.tzinfo is None:
            retry_date = retry_date.replace(tzinfo=timezone.utc)
        return max(0.0, (retry_date - datetime.now(timezone.utc)).total_seconds())


def get_default_reason(response: httpx.Response) -> str:
    reason = getattr(response, "reason", None)
    if reason is None:
        return getattr(response, "reason_phrase", "")
    if isinstance(reason, bytes):
        try:
            return reason.decode("utf-8")
        except UnicodeDecodeError:
            return reason.decode("iso-8859-1")
    return reason


def _response_url(response: httpx.Response, request: httpx.Request | None) -> str:
    try:
        return str(response.url)
    except RuntimeError:
        if request is not None:
            return str(request.url)
        return ""


def raise_for_status(
    response: httpx.Response,
    request: httpx.Request | None = None,
) -> None:
    problem = None
    reason = get_default_reason(response)
    url = _response_url(response, request)

    try:
        ct = response.headers.get("content-type") or ""
        if "application/problem+json" in ct:
            problem = json.loads(response.text, cls=ProblemDecoder)
            problem.status = problem.status or str(response.status_code)
        elif "application/json" in ct:
            problem = json.loads(response.text, cls=LegacyProblemDecoder)
            problem.status = problem.status or str(response.status_code)
            problem.url = url
    except json.JSONDecodeError:
        pass

    http_error_msg = ""
    if 400 <= response.status_code < 500:
        if isinstance(problem, (LegacyProblem, Problem)):
            http_error_msg = f"Client Error --> {problem.msg()}"
        else:
            http_error_msg = (
                f"{response.status_code} Client Error: {reason} "
                f"for url: {url}"
            )
    elif 500 <= response.status_code < 600:
        if isinstance(problem, (LegacyProblem, Problem)):
            http_error_msg = f"Server Error --> {problem.msg()}"
        else:
            http_error_msg = (
                f"{response.status_code} Server Error: {reason} "
                f"for url: {url}"
            )

    if http_error_msg:
        raise httpx.HTTPStatusError(
            http_error_msg,
            request=request or response.request,
            response=response,
        )


class SdkTransport(httpx.BaseTransport):
    def __init__(self, *, limiter=None, retry_policy=None, **kwargs):
        self.limiter = limiter
        self.retry_policy = retry_policy or RetryPolicy()
        self._transport = httpx.HTTPTransport(**kwargs)

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        attempt = 0
        request.read()
        while True:
            if self.limiter is not None:
                self.limiter.acquire()
            try:
                response = self._transport.handle_request(request)
                response.read()
                raise_for_status(response, request)
                return response
            except httpx.HTTPError as error:
                if not self.retry_policy.should_retry(error, attempt):
                    raise
                sleep_time = self.retry_policy.retry_after_time(error)
                if sleep_time is None:
                    sleep_time = self.retry_policy.backoff_time(attempt)
                time.sleep(sleep_time)
                attempt += 1

    def close(self) -> None:
        self._transport.close()


class AsyncSdkTransport(httpx.AsyncBaseTransport):
    def __init__(self, *, limiter=None, retry_policy=None, **kwargs):
        self.limiter = limiter
        self.retry_policy = retry_policy or RetryPolicy()
        self._transport = httpx.AsyncHTTPTransport(**kwargs)

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        attempt = 0
        await request.aread()
        while True:
            if self.limiter is not None:
                await self.limiter.async_acquire()
            try:
                response = await self._transport.handle_async_request(request)
                await response.aread()
                raise_for_status(response, request)
                return response
            except httpx.HTTPError as error:
                if not self.retry_policy.should_retry(error, attempt):
                    raise
                sleep_time = self.retry_policy.retry_after_time(error)
                if sleep_time is None:
                    sleep_time = self.retry_policy.backoff_time(attempt)
                await asyncio.sleep(sleep_time)
                attempt += 1

    async def aclose(self) -> None:
        await self._transport.aclose()
