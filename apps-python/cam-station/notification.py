import serial
import os, time
import json
from datetime import datetime

class NotificationServices():

    def __init__(self):
        #1 - Open Serial Port
        self.port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
        print('/dev/ttyUSB0 opened ...')
        ###
        #2 - Create MQTT Connection
        ###
        ###

        self.user_list = []
        self.__isReadyForSMS = True
        self.__isReadyForBells = False

        pass

    def loadConfigs(self, fname = 'Notification.json'):
        with open(fname) as json_file:
            data = json.load(json_file)
            self.user_list = data['users']
            # for p in self.user_list:
            #     print(p)

    # def chmod_serial(self):
        # pass
        #https://stackoverflow.com/questions/13045593/using-sudo-with-python-script

    def call_bells(self):
        pass

    def call_sms(self, phoneNum = '0936261441', contents = "Hello HoangQC"):
        self.__isReadyForSMS = False
        self.__transmit_AT_commands()

        self.port.write(str.encode('AT+CMGS="' + phoneNum + '"\r\n'))
        rcv = self.port.read(10)
        print(rcv)
        time.sleep(1)

        now = datetime.now()
        date = now.strftime("\n %d/%m/%Y, %H:%M:%S")

        self.port.write(str.encode("[FireBot]: " + contents + date +'\r\n'))  # Message
        rcv = self.port.read(10)
        print(rcv)

        self.port.write(str.encode("\x1A"))  # Enable to send SMS
        for i in range(10):
            rcv = self.port.read(10)
            print(rcv)

        print("SMS is done!")
        time.sleep(20)
        self.__isReadyForSMS = True
        pass

    def checkReadyNotification(self):
        return self.__isReadyForSMS


    def __transmit_AT_commands(self):
        sTime = 1

        self.port.write(str.encode('AT' + '\r\n'))
        rcv = self.port.read(10)
        print(rcv)
        time.sleep(sTime)

        self.port.write(str.encode('ATE0' + '\r\n'))  # Disable the Echo
        rcv = self.port.read(10)
        print(rcv)
        time.sleep(sTime)

        self.port.write(str.encode('AT+CMGF=1' + '\r\n'))  # Select Message format as Text mode
        rcv = self.port.read(10)
        print(rcv)
        time.sleep(sTime)

        self.port.write(str.encode('AT+CNMI=2,1,0,0,0' + '\r\n'))  # New SMS Message Indications
        rcv = self.port.read(10)
        print(rcv)
        time.sleep(sTime)
        pass