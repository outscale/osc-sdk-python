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


class SdkClientError(SdkHttpError):
    pass


class SdkServerError(SdkHttpError):
    pass


class SdkResponseError(SdkError):
    pass
