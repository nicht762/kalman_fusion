import time
import smbus
import zmq
from imusensor.MPU9250 import MPU9250


# initializing publisher
host = '192.168.1.3'
port = 8358
url = 'tcp://'+host+':'+str(port)
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(url)

# initializing IMU
address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()


while True:
    imu.readSensor()
    imu.computeOrientation()

    md = dict(topic='orientation', rpy=str([imu.roll, imu.pitch, imu.yaw]),
              acc=str([imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2]]))
    socket.send_json(md)
    time.sleep(0.1)
