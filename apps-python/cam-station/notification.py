import serial
import os, time

class NotificationServices():

    def __init__(self):
        #1 - Open Serial Port
        port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

        #2 - Create MQTT Connection

    def chmod_serial(self):
        pass
        #https://stackoverflow.com/questions/13045593/using-sudo-with-python-script

