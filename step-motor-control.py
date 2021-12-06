#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
from motor import stepMotor

GPIO.setmode( GPIO.BOARD )

m1_in1 = 11
m1_in2 = 13
m1_in3 = 15
m1_in4 = 16

m2_in1 = 18
m2_in2 = 22
m2_in3 = 29
m2_in4 = 31
 

m1 = stepMotor(m1_in1,m1_in2,m1_in3,m1_in4)
m2 = stepMotor(m2_in1,m2_in2,m2_in3,m2_in4)

# the meat
try:
    i = 0
    for i in range(0,4):
        m1.step(100, True)
        m2.step(100, False)

except KeyboardInterrupt:
    pass
m1.cleanup()
m2.cleanup()
GPIO.cleanup()
exit( 0 )