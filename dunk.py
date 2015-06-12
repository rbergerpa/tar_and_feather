#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class Dunk():
    def __init__(self):
        # The pi we're using on this has on=false off=true, so...
        self.ON = False
        self.OFF = True
        
        self.HORN_PIN = 16
        self.LEFT_WATER_PIN = 27
        self.LEFT_FEATHER_PIN = 17
        self.RIGHT_WATER_PIN = 21
        self.RIGHT_FEATHER_PIN = 20
        
        self.HORN_DURATION = 0.5
        self.WATER_DURATION = 0.5
        self.FEATHER_DURATION = 0.5
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.HORN_PIN, GPIO.OUT)
        GPIO.setup(self.LEFT_WATER_PIN, GPIO.OUT)
        GPIO.setup(self.LEFT_FEATHER_PIN, GPIO.OUT)
        GPIO.setup(self.RIGHT_WATER_PIN, GPIO.OUT)
        GPIO.setup(self.RIGHT_FEATHER_PIN, GPIO.OUT)

        self.reset_switches()

    def reset_switches(self):
        GPIO.output(self.HORN_PIN, self.OFF)
        GPIO.output(self.LEFT_WATER_PIN, self.OFF)
        GPIO.output(self.LEFT_FEATHER_PIN, self.OFF)
        GPIO.output(self.RIGHT_WATER_PIN, self.OFF)
        GPIO.output(self.RIGHT_FEATHER_PIN, self.OFF)
    
    def blow_horn(self):
        GPIO.output(self.HORN_PIN, self.ON)
        time.sleep(self.HORN_DURATION)
        GPIO.output(self.HORN_PIN, self.OFF)
    
    def dunk_left(self):
        self.blow_horn()
        GPIO.output(self.LEFT_WATER_PIN, self.ON)
        time.sleep(self.WATER_DURATION)
        GPIO.output(self.LEFT_WATER_PIN, self.OFF)
        GPIO.output(self.LEFT_FEATHER_PIN, self.ON)
        time.sleep(self.FEATHER_DURATION)
        GPIO.output(self.LEFT_FEATHER_PIN, self.OFF)
    
    def dunk_right(self):
        self.blow_horn()
        GPIO.output(self.RIGHT_WATER_PIN, self.ON)
        time.sleep(self.WATER_DURATION)
        GPIO.output(self.RIGHT_WATER_PIN, self.OFF)
        GPIO.output(self.RIGHT_FEATHER_PIN, self.ON)
        time.sleep(self.FEATHER_DURATION)
        GPIO.output(self.RIGHT_FEATHER_PIN, self.OFF)

    # Note, dunk_both can't just call dunk_left and dunk_right 
    # because we want them to go off simultaneously.
    def dunk_both(self):
        self.blow_horn()
        GPIO.output(self.RIGHT_WATER_PIN, self.ON)
        GPIO.output(self.LEFT_WATER_PIN, self.ON)
        time.sleep(self.WATER_DURATION)
        GPIO.output(self.RIGHT_WATER_PIN, self.OFF)
        GPIO.output(self.LEFT_WATER_PIN, self.OFF)
    
        GPIO.output(self.RIGHT_FEATHER_PIN, self.ON)
        GPIO.output(self.LEFT_FEATHER_PIN, self.ON)
        time.sleep(self.FEATHER_DURATION)
        GPIO.output(self.RIGHT_FEATHER_PIN, self.OFF)
        GPIO.output(self.LEFT_FEATHER_PIN, self.OFF)
    
