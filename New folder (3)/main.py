import RPi.GPIO as GPIO
import motor
import time
import plough
plough.armdown()
plough.armup()


GPIO.cleanup()
