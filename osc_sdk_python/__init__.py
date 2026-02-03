from .outscale_gateway import OutscaleGateway as Gateway
from .outscale_gateway import LOG_NONE
from .outscale_gateway import LOG_STDERR
from .outscale_gateway import LOG_STDIO
from .outscale_gateway import LOG_MEMORY
from .version import get_version
from .problem import Problem, ProblemDecoder
from .limiter import RateLimiter

# what to Log
from .outscale_gateway import LOG_ALL
from .outscale_gateway import LOG_KEEP_ONLY_LAST_REQ

__author__ = "Outscale SAS"
__version__ = get_version()
__all__ = [
    "__version__",
    "__author__",
    "Gateway",
    "LOG_NONE",
    "LOG_STDERR",
    "LOG_STDIO",
    "LOG_MEMORY",
    "LOG_ALL",
    "LOG_KEEP_ONLY_LAST_REQ",
    "Problem",
    "ProblemDecoder",
    "RateLimiter",
]
