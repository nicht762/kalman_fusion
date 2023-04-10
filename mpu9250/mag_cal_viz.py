import matplotlib.pyplot as plt
import numpy as np
import zmq
import os
import time
import sys
import json


# initializing subscriber
host = '192.168.1.3'
port = 8358
url = 'tcp://'+host+':'+str(port)
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(url)
socket.setsockopt(zmq.SUBSCRIBE, b'')

# samples to be collected
numSamples = 500


def getSamples(numSamples, socket):
    count = 0
    magVals = np.zeros((numSamples, 3))
    while count != numSamples:
        packet = socket.recv_json(0)
        magData = packet['data']
        magData = json.loads(magData)
        magVals[count, :] = np.array(magData)
        count = count + 1
        if count % 100 == 0 and count != 0:
            print("Recieved {0} samples of mag data".format(count))
    return magVals


# maguncalib = getSamples(numSamples, socket)
# plt.scatter(maguncalib[:, 0], maguncalib[:, 1], color='red', label='mx my', marker='.')
# plt.scatter(maguncalib[:, 0], maguncalib[:, 2], color='blue', label='mx mz', marker='^')
# plt.scatter(maguncalib[:, 1], maguncalib[:, 2], color='green', label='my mz', marker='s')
# plt.legend(loc='best')
# plt.show()
#
# maguncalib1 = maguncalib

magcalib = getSamples(numSamples, socket)
plt.scatter(magcalib[:, 0], magcalib[:, 1], color='red', label='mx my', marker='.')
plt.scatter(magcalib[:, 0], magcalib[:, 2], color='blue', label='mx mz', marker='^')
plt.scatter(magcalib[:, 1], magcalib[:, 2], color='green', label='my mz', marker='s')
plt.legend(loc='best')
plt.show()

