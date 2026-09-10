from .exceptions import (
    SdkClientError,
    SdkConfigurationError,
    SdkError,
    SdkHttpError,
    SdkOperationError,
    SdkResponseError,
    SdkServerError,
    SdkTransportError,
    SdkUsageError,
    SdkValidationError,
)
from .outscale_gateway import AsyncClient, Client
from .outscale_gateway import AsyncOutscaleGateway as AsyncGateway
from .outscale_gateway import OutscaleGateway as Gateway
from .problem import Problem, ProblemDecoder
from .runtime.transport import RateLimiter
from .version import get_version

__author__ = "Outscale SAS"
__version__ = get_version()
__all__ = [
    "__version__",
    "__author__",
    "Gateway",
    "AsyncGateway",
    "Client",
    "AsyncClient",
    "Problem",
    "ProblemDecoder",
    "RateLimiter",
    "SdkError",
    "SdkUsageError",
    "SdkConfigurationError",
    "SdkValidationError",
    "SdkOperationError",
    "SdkTransportError",
    "SdkHttpError",
    "SdkClientError",
    "SdkServerError",
    "SdkResponseError",
]
