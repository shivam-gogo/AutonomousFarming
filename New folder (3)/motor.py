
def fwd():
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.output(16,True)
    GPIO.output(18,False)
    GPIO.output(22,True)
    GPIO.output(11,False)


def left():
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.output(16,False)
    GPIO.output(18,False)
    GPIO.output(22,True)
    GPIO.output(11,False)


def right():
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.output(16,True)
    GPIO.output(18,False)
    GPIO.output(11,False)
    GPIO.output(22,False)
