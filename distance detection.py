#need to install driver with pip install tmf882x-driver

from smbus2 import SMBus
from tmf882x import TMF882x

with SMBus as bus:
    device = TMF882x(bus=bus)

with device:
    measurement = device.measure()

for x in measurement.results:
    print(x)
