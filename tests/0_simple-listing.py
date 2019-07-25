import sys
sys.path.append("..") 
from osc_python_sdk import Gateway
gw = Gateway()
vms = gw.ReadVms()
assert(isinstance(vms, dict))
assert(isinstance(vms["Vms"], list))
vols = gw.ReadVolumes()
assert(isinstance(vols, dict))
assert(isinstance(vols["Volumes"], list))