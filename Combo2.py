from twilio.rest import Client
import SendSMS as sms
import MakePhoneCall as call
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)        
GPIO.setup(3, GPIO.OUT)

flag = 0

def distance(GPIO_TRIGGER, GPIO_ECHO):
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
 
    return distance

def runUltrasonic(GPIO_TRIGGER, GPIO_ECHO):
    s = ""
    count = 0
    try:
        while True:
            count += 1
            soundAlarm()
            dist = distance(GPIO_TRIGGER, GPIO_ECHO)
            s += str(dist)
            s += "<br />"
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            if count==5:
                sms.sendSMS()
                return s
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        return s

def soundAlarm():
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7,0)
    time.sleep(.3)
    GPIO.output(7,1)
    time.sleep(.3)
    
def main():
    while True:
           i=GPIO.input(11)
           print "i = ",i
           if i==0:
                 print "No intruder, output value = ",i
                 GPIO.output(3, 0)
                 time.sleep(0.1)
           elif i==1:
                 call.dial_numbers()
                 print "Intruder detected, output value = ",i
                 GPIO.output(3, 1)
                 print "output"
                 time.sleep(0.1)
                 print "time.sleep"
                 flag = 1
                 print "flag set"
                 break
                 print "broke"

    if flag==1:
           print "Flag = 1 part"
           GPIO_TRIGGER = 18
           print "trigger set"
           GPIO_ECHO = 24
           GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
           GPIO.setup(GPIO_ECHO, GPIO.IN)
           s = runUltrasonic(GPIO_TRIGGER, GPIO_ECHO)
           print "In main ",s
           return s 
