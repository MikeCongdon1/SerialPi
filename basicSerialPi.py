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

def fnParse():
    while True:

        response = ser.readline()
        #print("read data: {}".format(response.decode()))

        if 'money' in response.decode():
            print("you're rich!")
        else:
            print("you're poor")


if ser.isOpen():

    ser.flushInput() #flush input buffer, discarding all its contents
    ser.flushOutput()#flush output buffer, aborting current output

    ser.write(b"started, insert commands here\r\n")
    #print("write data: ATI")
    time.sleep(0.5)
    numberOfLine = 0

    fnParse()

else:
    try:
        ser.open()
        fnParse()
    exception:
        print('serial not found')
        exit()
