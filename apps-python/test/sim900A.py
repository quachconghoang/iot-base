import serial     
import os, time
   

# Enable Serial Communication
port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write(str.encode('AT'+'\r\n'))
rcv = port.read(10)
print (rcv)
time.sleep(1)

port.write(str.encode('ATE0'+'\r\n'))      # Disable the Echo
rcv = port.read(10)
print (rcv)
time.sleep(1)

port.write(str.encode('AT+CMGF=1'+'\r\n'))  # Select Message format as Text mode 
rcv = port.read(10)
print (rcv)
time.sleep(1)

port.write(str.encode('AT+CNMI=2,1,0,0,0'+'\r\n'))   # New SMS Message Indications
rcv = port.read(10)
print (rcv)
time.sleep(1)

# Sending a message to a particular Number

port.write(str.encode('AT+CMGS="0936261441"'+'\r\n'))
rcv = port.read(10)
print (rcv)
time.sleep(1)

port.write(str.encode('[FireBot]:Hello HoangQC'+'\r\n'))  # Message
rcv = port.read(10)
print (rcv)

port.write(str.encode("\x1A")) # Enable to send SMS
for i in range(10):
    rcv = port.read(10)
    print (rcv)
