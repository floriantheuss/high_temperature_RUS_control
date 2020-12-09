import RPi.GPIO as GPIO
import numpy as np
import time


class PowerRelay:
    
    def __init__(self, pinnumber=37):
        self.pinN = pinnumber
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinN, GPIO.OUT)
        GPIO.output(self.pinN, 0)
        
    def set_pin (self, new_pin):
        #GPIO.cleanup()
        self.pinN = new_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinN, GPIO.OUT)
        GPIO.output(self.pinN, 0)
        
    def mode (self, mode):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinN, GPIO.OUT)
        if mode == 'on':
            GPIO.output(self.pinN, 0)
        if mode == 'off':
            GPIO.output(self.pinN, 1)
            
    def end (self):
        GPIO.cleanup()
        