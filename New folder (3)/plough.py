import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

def armdown():
    GPIO.output(13,False)
    GPIO.output(15,True)
    time.sleep(0.4)
    GPIO.cleanup()

    
    
def armup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.output(13,True)
    GPIO.output(15,False)
    time.sleep(0.4)
    GPIO.cleanup()
    
