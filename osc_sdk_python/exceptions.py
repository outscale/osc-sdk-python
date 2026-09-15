import json


REQUEST_ID_KEYS = (
    "RequestId",
    "request_id",
    "requestId",
    "x-request-id",
    "x-osc-request-id",
)
REQUEST_ID_HEADERS = (
    "x-osc-request-id",
    "x-request-id",
    "x-amzn-requestid",
    "x-amz-request-id",
)


def _request_id_from_mapping(data):
    if not isinstance(data, dict):
        return None

    for key in REQUEST_ID_KEYS:
        value = data.get(key)
        if value:
            return str(value)

    response_context = data.get("ResponseContext")
    if isinstance(response_context, dict):
        value = response_context.get("RequestId")
        if value:
            return str(value)

    return None


def extract_request_id(*, problem=None, response=None):
    """Best-effort extraction of the request ID associated with a failure."""
    problem_fields = getattr(problem, "__dict__", {})
    value = problem_fields.get("_request_id") or problem_fields.get("request_id")
    if value:
        return str(value)

    extras = getattr(problem, "extras", None)
    value = _request_id_from_mapping(extras)
    if value:
        return value

    headers = getattr(response, "headers", None)
    if headers is not None:
        for header in REQUEST_ID_HEADERS:
            value = headers.get(header)
            if value:
                return str(value)

    if response is None:
        return None

    try:
        data = response.json()
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError, RuntimeError):
        return None

    return _request_id_from_mapping(data)


class SdkError(Exception):
    """Base class for all public SDK exceptions."""


class SdkUsageError(SdkError):
    pass


class SdkConfigurationError(SdkError):
    pass


class SdkValidationError(SdkError):
    pass


class SdkOperationError(SdkValidationError):
    pass


class SdkTransportError(SdkError):
    def __init__(self, message, *, request=None, response=None):
        super().__init__(message)
        self.request = request
        self.response = response

    @property
    def request_id(self):
        value = getattr(self, "_request_id", None)
        if value:
            return str(value)
        return extract_request_id(response=self.response)

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def __str__(self):
        message = super().__str__()
        request_id = self.request_id
        if not request_id:
            return message
        existing_ids = (
            f"request_id={request_id}",
            f"request_id = {request_id}",
            f"RequestId={request_id}",
            f"RequestId = {request_id}",
        )
        if any(existing_id in message for existing_id in existing_ids):
            return message
        return f"{message} (request_id={request_id})"

    def __repr__(self):
        request_id = self.request_id
        if not request_id:
            return super().__repr__()
        return f"{self.__class__.__name__}({super().__str__()!r}, request_id={request_id!r})"


class SdkHttpError(SdkTransportError):
    def __init__(
        self,
        message,
        *,
        status_code=None,
        request=None,
        response=None,
        problem=None,
        url=None,
    ):
        super().__init__(message, request=request, response=response)
        self.status_code = status_code
        self.problem = problem
        self.url = url

    @property
    def request_id(self):
        value = getattr(self, "_request_id", None)
        if value:
            return str(value)
        return extract_request_id(problem=self.problem, response=self.response)

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


class SdkClientError(SdkHttpError):
    pass


class SdkServerError(SdkHttpError):
    pass


class SdkResponseError(SdkError):
    pass
