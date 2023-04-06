import time

import numpy as np
from scipy.spatial.transform import Rotation as Rot
import smbus
from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()


while True:
    imu.readSensor()
    imu.computeOrientation()

    euler = np.array([imu.roll, imu.pitch, imu.yaw])
    accel_glob = Rot.from_euler('xyz', euler, degrees=True)
    accel_glob.apply(imu.AccelVals)
    print(accel_glob)
    time.sleep(0.1)
