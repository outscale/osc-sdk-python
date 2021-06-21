import sys
import requests
sys.path.append("..")
from osc_sdk_python import Gateway

gw = Gateway()
try:
    gw.CreateNet(IpRange='142.42.42.42/32')
    assert False, "CreateNet should not be allowed"
except requests.exceptions.HTTPError as e:
    errors = e.response.json().get('Errors')
    for error in errors:
        assert len(error.get('Details')) > 0
except:
    assert False, "Unexpected error occured"
