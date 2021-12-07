#!/usr/bin/python3
import RPi.GPIO as GPIO
from pencil import Pencil

# the meat
try:
    p = Pencil()
    p.square(1)
    
    for i in range(0,9):
        p.circle(1+0.25*i)


except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
exit( 0 )