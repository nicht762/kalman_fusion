import zmq
import numpy as np
import json
from scipy.spatial.transform import Rotation as Rot


host = '192.168.1.3'
port = 8358
url = 'tcp://'+host+':'+str(port)
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(url)
socket.setsockopt(zmq.SUBSCRIBE, b'')

while True:
    packet = socket.recv_json(0)
    pack_rpy = packet['rpy']
    rpy = np.array(json.loads(pack_rpy))
    pack_acc = packet['acc']
    acc = np.array(json.loads(pack_acc))

    acc_rot = Rot.from_euler('xyz', rpy, degrees=True)
    accel_glob = acc_rot.apply(acc)
    print(accel_glob)


