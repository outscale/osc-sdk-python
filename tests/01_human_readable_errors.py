import sys
sys.path.append("..")
from osc_sdk_python import Gateway
gw = Gateway()
res = gw.CreateNet(IpRange='142.42.42.42/32')
error = [error for error in res['Errors'] if error.get('Code') == '4014' and error.get('Details') == 'invalid-block-size']
assert len(error) == 1

