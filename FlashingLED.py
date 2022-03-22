# In this project, a small LED is connected through GPIO2 o fmy Pi 4
# It will flashing the LED every 2 second
#
#Program:FlashingLED.py
#Date: 03-21-2022
#Author: Mr.Tang
#Version: 1.0


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)


try:
    while True:
        GPIO.output(2 , 1)  # turn on the LED
        time.sleep(2)
        GPIO.output(2, 0)   # turn off the LED
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
        
        
