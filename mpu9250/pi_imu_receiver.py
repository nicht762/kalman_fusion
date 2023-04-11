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

g_vec = np.array([0.0, 0.0, 9.81])


def get_accel_global(rpy, acc):
    acc_rot = Rot.from_euler('xyz', rpy, degrees=True)
    accel_g = acc_rot.apply(np.array([acc[1], acc[0], acc[2]]))
    accel_global = accel_g - np.array([0.0, 0.0, 9.81])
    return accel_global


def rf(val):
    return round(float(val), 2)


while True:
    packet = socket.recv_json(0)
    pack_rpy = packet['rpy']
    rpy = np.array(json.loads(pack_rpy, parse_float=rf))
    print('RPY ', float(rpy[0]), float(rpy[1]), float(rpy[2]))
    pack_acc = packet['acc']
    acc = np.array(json.loads(pack_acc))
    print('ACC', float(acc[0]), float(acc[1]), float(acc[2]))

    accel_glob = get_accel_global(rpy, acc)
    print(accel_glob)


