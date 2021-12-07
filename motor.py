import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

steps_per_rotation = 200
step_sequence =    [[1,0,0,0],
                    [0,0,0,0],
                    [0,1,0,0],
                    [0,0,0,0],
                    [0,0,1,0],
                    [0,0,0,0],
                    [0,0,0,1],
                    [0,0,0,0]]

class stepMotor:
    # This defines a class that contols the 
    # movement of an individual motor
    def __init__(self,in1,in2,in3,in4,sleep=0.0005):
        self._motorPins = [in1,in2,in3,in4]
        self._stepSleep = sleep
        self._location = 0
        self._direction = True
        for i in range(0,len(self._motorPins)):
            GPIO.setup( self._motorPins[i], GPIO.OUT )
            GPIO.output( self._motorPins[i], GPIO.LOW )
            
    def step(self, steps = 20):
        if steps >= 0:    
            motor_step_counter = 0
            i = 0
            for i in range(steps):
                for pin in range(0,len(self._motorPins)):
                    GPIO.output( self._motorPins[pin], step_sequence[motor_step_counter][pin] )
                if self._direction == True:
                    motor_step_counter = (motor_step_counter + 1) % 8
                else:
                    motor_step_counter = (motor_step_counter - 1) % 8
                time.sleep( self._stepSleep )

    def set_direction(self, counterclockwise=True):
        self._direction=counterclockwise

    def get_location(self):
        return self._location
        
    def get_pins(self):
        return self._motorPins

    def cleanup(self):
        for pin in range(0,len(self._motorPins)):
            GPIO.output( self._motorPins[pin], GPIO.LOW )

