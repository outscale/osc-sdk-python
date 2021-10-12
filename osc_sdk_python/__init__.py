import os

def get_version():
    osc_sdk_python_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(osc_sdk_python_path, 'VERSION'), 'r') as fd:
        return fd.read().strip()

__author__ = "Outscale SAS"
__version__ = get_version()

from .outscale_gateway import OutscaleGateway as Gateway
from .outscale_gateway import LOG_NONE
from .outscale_gateway import LOG_STDERR
from .outscale_gateway import LOG_STDIO
from .outscale_gateway import LOG_MEMORY

# what to Log
from .outscale_gateway import LOG_ALL
from .outscale_gateway import LOG_KEEP_ONLY_LAST_REQ
