import RPi.GPIO as GPIO
import numpy as np
import time

class StepperMotor:

    def __init__(self, position=0, pins = [7, 11, 13, 15]):
        self.control_pins = pins
        self.position = position * 512 / 360
        
    
    def get_angle (self):
        print('the stepper motor is at ' + str(self.position/512*360) + ' degrees' )
    
    
    def set_new_zero (self):
        self.position = 0
    

    def turn (self, angle, direction):
        GPIO.setmode(GPIO.BOARD)
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        halfstep_seq = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
            ]
        
        if direction == 'cw':
            a = 1
        elif direction == 'ccw':
            a = -1

        distance = int(angle / 360 * 512)

        for _ in range(distance):
            for halfstep in np.arange(8)[::-a]:
                for pin in range(4):
                    GPIO.output(self.control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)
        #GPIO.cleanup()
        
        self.position = (self.position + a*distance) % 512
    
    
    
    def set_angle (self, angle):
        change =  int(angle) - self.position * 360 / 512
        
        if change == 0:
            direction = 'cw'
        elif change/abs(change) == 1:
            direction = 'cw'
        elif change/abs(change) == -1:
            direction = 'ccw'

        self.turn(abs(change), direction)



    def set_dial (self, number):
        angle = number / 10 * 270
        self.set_angle(angle)

    
    def end (self):
        self.set_angle(0)
        GPIO.cleanup()