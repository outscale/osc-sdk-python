import os

def get_version() -> str:
    osc_sdk_python_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(osc_sdk_python_path, "VERSION"), "r") as fd:
        return fd.read().strip()

