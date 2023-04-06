import os
import sys
import time
import smbus
from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()

file = open('1.txt', 'w')

for i in range(5000): 
    imu.readSensor()
    imu.computeOrientation()
    print(i)
    #file.write("{0} {1} {2} {3} \n".format(i, imu.roll, imu.pitch, imu.yaw))
    # accel - y,x,z
    #print(imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2])
    #file.write("{0} {1} {2} {3} \n".format(i, imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2]))
    # gyro - 
    #print(imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2])
    file.write("{0} {1} {2} {3} \n".format(i, imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2]))
    # mag -
    #print(imu.MagVals[0], imu.MagVals[1], imu.MagVals[2])
    #file.write("{0} {1} {2} {3} \n".format(i, imu.MagVals[0], imu.MagVals[1], imu.MagVals[2]))
    time.sleep(0.1)
file.close()      