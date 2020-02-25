# Test to make sure that rotation from 0-90 degrees and rotation from 90-0 degrees works
# Date: 02/19/2020 Status: Working

import RPi.GPIO as GPIO
from time import sleep

servo = 17
GPIO.setmode( GPIO.BCM )
GPIO.setup( servo, GPIO.OUT )
p = GPIO.PWM( servo, 50 )
p.start( 2.5 )

def SetAngleDoor1( angle, servo, p ):
    for i in range( 0, angle ):
        dutyRatioL = i / 18 + 2
        p.ChangeDutyCycle( dutyRatioL )
        sleep( .01 )
    
def SetAngleDoor2( angle, servo, p ):
    for i in range( 0, angle ):
        dutyRatioR = ( angle - i ) / 18 + 2
        p.ChangeDutyCycle( dutyRatioR )
        sleep( .01 )

#SetAngleDoor1( 90, servo, p )
SetAngleDoor2( 90, servo, p )

p.stop()
GPIO.cleanup()