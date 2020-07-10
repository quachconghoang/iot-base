import serial
import os, time
import json

class NotificationServices():

    def __init__(self):
        #1 - Open Serial Port
        # port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
        ###
        ###
        #2 - Create MQTT Connection
        ###
        ###

        pass

    def loadConfigs(self, fname = 'Notification.json'):
        with open(fname) as json_file:
            data = json.load(json_file)
            self.user_list = data['users']
            for p in self.user_list:
                print(p)


    def chmod_serial(self):
        pass
        #https://stackoverflow.com/questions/13045593/using-sudo-with-python-script

    def call_bells(self):
        pass

    def call_sms(self):
        pass

