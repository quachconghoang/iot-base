import serial
import os, time
from datetime import datetime
import paho.mqtt.client as mqtt


class NotificationServices():

    def __init__(self):
        #1 - Open Serial Port
        self.port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
        print('/dev/ttyUSB0 opened ...')
        self.__transmit_AT_commands()

        ###
        # 2 - Create MQTT Connection
        self.mqttc = mqtt.Client()
        self.mqttc.on_message = self.__on_message
        self.mqttc.on_connect = self.__on_connect
        self.mqttc.on_publish = self.__on_publish
        self.mqttc.on_subscribe = self.__on_subscribe
        # Uncomment to enable debug messages
        # mqttc.on_log = on_log
        self.mqttc.connect("127.0.0.1", 1883, 60)
        self.mqttc.subscribe("FireAlarm/SMS", qos=0)
        # mqttc.loop_forever()
        # self.__mqttc.subscribe("FireAlarm/BELL", qos=0)

        self.user_list = []

        pass

    # def chmod_serial(self):
        # pass
        #https://stackoverflow.com/questions/13045593/using-sudo-with-python-script

    def call_bells(self):
        pass

    def call_sms(self, phoneNum = '0936261441', contents = "Hello Admin"):
        self.port.write(str.encode('AT+CNMI=2,1,0,0,0' + '\r\n'))  # New SMS Message Indications
        rcv = self.port.read(10)
        print(rcv)
        time.sleep(1)

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

        print("An SMS is done!")
        # time.sleep(20)
        pass

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
        pass

    def __on_connect(self, mqttc, obj, flags, rc):
        print("rc: " + str(rc))

    def __on_message(self, mqttc, obj, msg):
        print(msg.topic + ": " + str(msg.payload))

    def __on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))

    def __on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def __on_log(self, mqttc, obj, level, string):
        print(string)

if __name__ == "__main__":
    ntf = NotificationServices()
    ntf.mqttc.loop_forever()


