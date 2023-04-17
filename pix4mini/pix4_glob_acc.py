import time
import numpy as np
from scipy.spatial.transform import Rotation as Rot
from MavParser import MavParser

# parser = MavParser('com3')
parser = MavParser("/dev/ttyACM0")
g_acc = np.array([0.0, 0.0, 9.81])


def get_glob_acc(imu_data):
    accel_global = np.zeros(4)
    accel_global[3] = imu_data[6]
    acc_rot = Rot.from_euler('xyz', data[0:3])
    acc_with_g = acc_rot.apply(data[3:6])
    accel_global[0:3] = acc_with_g + g_acc
    return accel_global


while True:
    print('waiting')
    data = parser.parse_imu()
    get_glob_acc(data)
    print(get_glob_acc(data))
    time.sleep(0.01)

