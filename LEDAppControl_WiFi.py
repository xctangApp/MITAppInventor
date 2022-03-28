#--------------------------------------------------------
#
#       LED Control from android app
#
#
# In this project, one LED is connected to ports GPIO 2
# of Raspberry Pi through a current limiting ressitor.
# The LED is turned ON and OFF from android app
#
#
# Program: LEDAppControl_WiFi.py
# Date   : 02/27/2022
# Author : Xincheng Tang
#---------------------------------------------------------

from flask import Flask,render_template  # import Flask library
import RPi.GPIO as GPIO

app=Flask(__name__)

GPIO.setwarnings(False)   # disable warnings
GPIO.setmode(GPIO.BCM)    # set BCM pin numbering

LED = 2                   # LED on GPIO 2

GPIO.setup(LED, GPIO.OUT) # conf LED1 as output

GPIO.output(LED, 0)       # turn off LED1 to start with

#
# start of the main program loop, read commands from
# the android mobile phone, decode them and control LED
#

@app.route("/<device>/<action>")
def action(device, action):
    actuator = LED
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)     #LED1 on
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)      #LED1 off
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0', use_reloader=False)









