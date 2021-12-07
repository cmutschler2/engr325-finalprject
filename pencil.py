from motor import stepMotor
import math

INCHES_PER_STEP = 0.0031

class Pencil:

    def __init__(self,x=0,y=0,x_in1=31,x_in2=22,x_in3=29,x_in4=18,
                    y_in1=16,y_in2=13,y_in3=15,y_in4=11):
        self._x = 0
        self._y = 0
        self._xMotor = stepMotor(x_in1,x_in2,x_in3,x_in4)
        self._yMotor = stepMotor(y_in1,y_in2,y_in3,y_in4)
    
    # returns current x position
    def get_x(self):
        return self._x
        
    #returns current y position
    def get_y(self):
        return self._y

    # moves head distance in inches
    def moveX(self,x=1):
        x_steps=round(x/INCHES_PER_STEP)
        if x_steps >= 10:
            self._xMotor.set_direction(True)
        elif x_steps <= -10:
            self._xMotor.set_direction(False)
        else:
            return False
        self._xMotor.step(abs(x_steps))
        self._x+=x
        return True

    # moves head distance in inches
    def moveY(self,y=1):
        y_steps=round(y/INCHES_PER_STEP)
        if y_steps >= 10:
            self._yMotor.set_direction(True)
        elif y_steps <= -10:
            self._yMotor.set_direction(False)
        else:
            return False
        self._yMotor.step(abs(y_steps))
        self._y+=y
        return True

    # draws a "circle" of given radius
    def circle(self,radius=1):
        theta_actual=math.acos((radius-(INCHES_PER_STEP*10))/radius)
        print(theta_actual)
        num_incr = math.floor(2*math.pi/theta_actual)
        print(num_incr)
        theta_estimate = 2*math.pi/num_incr
        print(theta_estimate)
        
        theta=0
        for i in range(0,num_incr):
            x = math.cos(theta)*radius
            y = math.sin(theta)*radius
            theta += theta_estimate
            self.moveY(y-self.get_y())
            self.moveX(x-self.get_x())
        
        self.moveY(-1*self.get_y())
        self.moveX(-1*self.get_x())
    
    # draws a square of given radius
    def square(self,radius):
        self.moveX(radius)
        self.moveY(radius)
        self.moveX(radius*-2)
        self.moveY(radius*-2)
        self.moveX(radius*2)
        self.moveY(radius)
        self.moveX(radius*-1)
