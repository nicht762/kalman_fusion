from serial import Serial
from pyubx2 import UBXReader

stream = Serial('COM20', 115200, timeout=3)
ubr = UBXReader(stream)

# (raw_data, parsed_data) = ubr.read()
for (raw_data, parsed_data) in ubr:
    print(parsed_data)

# NMEA/GNGGA
# <NMEA(GNGGA, time=22:11:25, lat=55.7490593333, NS=N, lon=48.7426426667, EW=E,
# quality=2, numSV=7, HDOP=1.79, alt=204.3, altUnit=M, sep=-0.1, sepUnit=M, diffAge=, diffStation=0)>

