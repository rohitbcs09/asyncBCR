# -*- generated by 1.0.9 -*-
import da
_config_object = {}
import sys
import subprocess
import time
from src.replicas.replica import replica

class olympus(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def setup(self, config_file, **rest_186):
        super().setup(config_file=config_file, **rest_186)
        self._state.config_file = config_file
        self._state.config_file = self._state.config_file

    def run(self):
        print('In Olympus Run ')
        'for ind in range(1, 4):\n            print(str(ind) + "************************")\n            node_name = \'ReplicaNode\' + str(ind)\n            \n            #cmd = \'python3 -m da -n \'+ node_name + \' -D -f --logfilename logs/\' + node_name             #    + \'.log\' + \' -L info \' + \' src/replicas/replica.da \' + config_file + \' \' + node_name\n            #subprocess.Popen(cmd, shell= True)\n            #print("subprocess ran for ", node_name)\n            #time.sleep(1)\n            output("started node " + node_name)\n\n            if ind == 1:\n                rep = new(replica, args = ("ReplicaNode1", "ReplicaNode1",                     "ReplicaNode2", "ReplicaNode3", ), at = "ReplicaNode1")\n                start(rep)\n            elif ind == 2:\n                rep = new(replica, args = ("ReplicaNode1", "ReplicaNode2",                     "ReplicaNode3", "ReplicaNode3", ), at = "ReplicaNode2")\n                start(rep)\n            else:\n                rep = new(replica, args = ("ReplicaNode1", "ReplicaNode3",                     "None", "ReplicaNode3", ), at = "ReplicaNode3")\n                start(rep)'
