#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

ON = True
OFF = False

BIG_RED_BUTTON_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(BIG_RED_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while (True):
  time.sleep(0.5)
  if ON == GPIO.input(BIG_RED_BUTTON_PIN):
      print "BUTTON PRESSED"
  else:
      print "BUTTON NOT PRESSED"
