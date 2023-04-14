import numpy as np
from pymavlink import mavutil


class MavParser:
    def __init__(self, port):
        self.connection = mavutil.mavlink_connection(port, baud=115200)
        self.imu_data = np.zeros(8)

    def parse_imu(self):
        att = self.connection.recv_match(type='ATTITUDE', blocking=True)
        imu = self.connection.recv_match(type='HIGHRES_IMU', blocking=True)
        self.imu_data = np.array([att.roll, att.pitch, att.yaw,
                                  imu.xacc, imu.yacc, imu.zacc,
                                  att.time_boot_ms, imu.time_usec])
        # print(att.roll, att.pitch, att.yaw)
        return self.imu_data
    #
    # def norm_ang(self,ang):


# parser = MavParser('com3')
# g_acc = np.array([0.0, 0.0, 9.81])

