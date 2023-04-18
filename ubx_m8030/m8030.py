import pymap3d
from serial import Serial
from pyubx2 import UBXReader

ellipsoid = pymap3d.Ellipsoid()
# base
lat_0 = 55.760057829964516
lon_0 = 48.75896086562219
hgt_0 = 199.37

stream = Serial('COM20', 115200, timeout=3)
ubr = UBXReader(stream)

# (raw_data, parsed_data) = ubr.read()
for (raw_data, parsed_data) in ubr:
    print(parsed_data)
    east, north, up = pymap3d.geodetic2enu(lat_1, lon_1, hgt_1,
                                           lat_0, lon_0, hgt_0,
                                           ell=ellipsoid, deg=True)

# NMEA/GNGGA
# <NMEA(GNGGA, time=22:11:25, lat=55.7490593333, NS=N, lon=48.7426426667, EW=E,
# quality=2, numSV=7, HDOP=1.79, alt=204.3, altUnit=M, sep=-0.1, sepUnit=M, diffAge=, diffStation=0)>

