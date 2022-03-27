#--------------------------------------------------------
#
#       LED Control from android app
#
#
# In this project, a small LED is connected to port GPIO 2
# of Raspberry Pi through a current limiting ressitor.
# The LED is turned ON and OFF from android app
#
#
# Program: LEDAppControl_BT.py
# Date   : 02/27/2022
# Author : Xincheng Tang
#---------------------------------------------------------

import socket             # import socket library
import RPi.GPIO as GPIO
GPIO.setwarnings(False)   # disable warnings
GPIO.setmode(GPIO.BCM)    # set BCM pin numbering

LED = 2                   # LED out on GPIO 2
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, 0)

Port = 1
MAC = 'DC:A6:32:8E:0F:3E'
s=socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
s.bind((MAC, Port))
s.listen(1)
client, addr = s.accept()


try:
    while True:
        data = client.recv(1024)
        if data.decode('utf-8') == "1":
            GPIO.output(LED, 1)
        elif data.decode('utf-8') == "0":
            GPIO.output(LED, 0)

except KeyboardInterrupt:
    client.close()
    s.close()
        








