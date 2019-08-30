import sys
sys.path.append("..") 
from osc_sdk_python import Gateway
gw = Gateway()
vms = gw.ReadVms()
assert(isinstance(vms, dict))
assert(isinstance(vms["Vms"], list))
vols = gw.ReadVolumes()
assert(isinstance(vols, dict))
assert(isinstance(vols["Volumes"], list))
