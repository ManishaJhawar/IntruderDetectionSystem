import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)        
GPIO.setup(3, GPIO.OUT)

flag = 0

def distance():
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    
    distance = (TimeElapsed * 34300) / 2
 
    return distance/6.0

def runUltrasonic():
    try:
        while True:
            soundAlarm()
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

def soundAlarm():
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7,0)
    time.sleep(.3)
    GPIO.output(7,1)
    time.sleep(.3)

while True:
       i=GPIO.input(11)
       print "i = ",i
       if i==0:
             print "No intruder, output value = ",i
             GPIO.output(3, 0)
             time.sleep(0.1)
       elif i==1:
             print "Intruder detected, output value = ",i
             GPIO.output(3, 1)
             time.sleep(0.1)
             flag = 1
             break

if flag==1:
       GPIO_TRIGGER = 18
       GPIO_ECHO = 24
       GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
       GPIO.setup(GPIO_ECHO, GPIO.IN)
    
       runUltrasonic()

