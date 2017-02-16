#!/usr/bin/env python
# based on Brett Dangerfield's raspberry pi tempature monitor project (and many others)

import time
import serial


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=5
)
counter=0


while 1:
    ser.write('Write counter: %d \n'%(counter))
    time.sleep(1)
    counter += 1