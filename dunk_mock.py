#!/usr/bin/env python
import time

class Dunk():
    def __init__(self):
        print "INITIALIZING MOCK_DUNK"
        # The pi we're using on this has on=false off=true, so...
        self.ON = False
        self.OFF = True
        
        self.HORN_PIN = 16
        self.LEFT_WATER_PIN = 27
        self.LEFT_FEATHER_PIN = 17
        self.RIGHT_WATER_PIN = 21
        self.RIGHT_FEATHER_PIN = 20
        
        self.HORN_DURATION = 2
        self.PAUSE_DURATION = 1
        self.WATER_DURATION = 1
        self.FEATHER_DURATION = 1
        
        self.reset_switches()

    def reset_switches(self):
        print "RESETTING SWITCHES"
    
    def blow_horn(self):
        print "HORN ON"
        time.sleep(self.HORN_DURATION)
        print "HORN OFF"
    
    def dunk_left(self):
        self.blow_horn()
        time.sleep(self.PAUSE_DURATION)
        print "LEFT WATER ON"
        time.sleep(self.WATER_DURATION)
        print "LEFT WATER OFF"
        print "LEFT FEATHER ON"
        time.sleep(self.FEATHER_DURATION)
        print "LEFT FEATHER OFF"
    
    def dunk_right(self):
        self.blow_horn()
        time.sleep(self.PAUSE_DURATION)
        print "RIGHT WATER ON"
        time.sleep(self.WATER_DURATION)
        print "RIGHT WATER OFF"
        print "RIGHT FEATHER ON"
        time.sleep(self.FEATHER_DURATION)
        print "RIGHT FEATHER OFF"

    # Note, dunk_both can't just call dunk_left and dunk_right 
    # because we want them to go off simultaneously.
    def dunk_both(self):
        self.blow_horn()
        time.sleep(self.PAUSE_DURATION)
        print "RIGHT WATER ON"
        print "LEFT WATER ON"
        time.sleep(self.WATER_DURATION)
        print "RIGHT WATER OFF"
        print "LEFT WATER OFF"

        print "RIGHT FEATHER ON"
        print "LEFT FEATHER ON"
        time.sleep(self.FEATHER_DURATION)
        print "RIGHT FEATHER OFF"
        print "LEFT FEATHER OFF"
  
