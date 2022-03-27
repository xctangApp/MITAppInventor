import RPi.GPIO as GPIO   #import GPIO library
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

try:
    while True:
        GPIO.output(2, 1)     #turn on the LED
        time.sleep(3.5)       #wait for 2.5 sec
        GPIO.output(2, 0)     #turn off the LED
        #time.sleep(1)         #wait for 1 sec
        

        GPIO.output(3, 1)     #turn on the LED
        time.sleep(1)         #wait for 1 sec
        GPIO.output(3, 0)     #turn off the LED
        #time.sleep(1)         #wait for 1 sec
        

        GPIO.output(4, 1)     #turn on the LED
        time.sleep(3.5)       #wait for 2.5 sec
        GPIO.output(4, 0)     #turn off the LED
        #time.sleep(1)         #wait for 1 sec


except KeyboardInterrupt:
    GPIO.cleanup()

