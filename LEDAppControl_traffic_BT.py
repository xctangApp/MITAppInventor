#--------------------------------------------------------
#
#       LED Control from android app
#
#
# In this project, 3 LEDs are connected to ports GPIO 2,3,4
# of Raspberry Pi through a current limiting ressitor.
# The LED is turned ON and OFF from android app
#
#
# Program: LEDAppControl_traffic.py
# Date   : 02/27/2022
# Author : Xincheng Tang
#---------------------------------------------------------

import socket      # import socket library
import RPi.GPIO as GPIO
GPIO.setwarnings(False)   # disable warnings
GPIO.setmode(GPIO.BCM)    # set BCM pin numbering

LED1 = 2                   # LED on GPIO 2
LED2 = 3                   # LED on GPIO 3
LED3 = 4                   # LED on GPIO 4

GPIO.setup(LED1, GPIO.OUT) # conf LED1 as output
GPIO.setup(LED2, GPIO.OUT) # conf LED2 as output
GPIO.setup(LED3, GPIO.OUT) # conf LED3 as output

GPIO.output(LED1, 0)       # turn off LED1 to start with
GPIO.output(LED2, 0)       # turn off LED2 to start with
GPIO.output(LED3, 0)       # turn off LED3 to start with

#
# start of the main program loop, read commands from
# the android mobile phone, decode them and control LED
#

Port = 1
MAC = 'DC:A6:32:8E:0F:3E'
s = socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
s.bind((MAC, Port))
s.listen(1)
client, addr = s.accept()

#
# turn on the LED if command is : 1
# turn on the LED if command is : 0
#

try:
    while True:
        data = client.recv(1024)                # Recieve data bytes
        if data.decode('utf-8') == '11':        # 11 received
            GPIO.output(LED1, 1)                # LED ON
        elif data.decode('utf-8') == '10':      # 10 received
            GPIO.output(LED1, 0)                # LED OFF
        if data.decode('utf-8') == '21':        # 21 received
            GPIO.output(LED2, 1)                # LED ON
        elif data.decode('utf-8') == '20':      # 20 received
            GPIO.output(LED2, 0)                # LED OFF
        if data.decode('utf-8') == '31':        # 30 received
            GPIO.output(LED3, 1)                # LED ON
        elif data.decode('utf-8') == '30':      # 31 received
            GPIO.output(LED3, 0)                # LED OFF

except KeyboardInterrupt:                      # Keyboard interrupt
    client.close()
    s.close()







