# Test servo acuation with button input
# Date: 02/25/2020 Status: Working but need to fix twitching

import RPi.GPIO as GPIO
from time import sleep

servo = 17
GPIO.setmode( GPIO.BCM )
GPIO.setup( servo, GPIO.OUT )
def pwm( servo ):
    p = GPIO.PWM( servo, 50 )
    return p
p = pwm( servo )
p.start( 2.5 )

def SetAngleDoor1( angle, p ):
    for i in range( 0, angle ):
        dutyRatioL = i / 18 + 2
        p.ChangeDutyCycle( dutyRatioL )
        sleep( .01 ) 
def SetAngleDoor2( angle, p ):
    for i in range( 0, angle ):
        dutyRatioR = ( angle - i ) / 18 + 2
        p.ChangeDutyCycle( dutyRatioR )
        sleep( .01 )

btn = 14
angle = 90
mode = 0
GPIO.setwarnings( False )
GPIO.setup( btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
GPIO.add_event_detect( btn, GPIO.RISING )
while True:
    if GPIO.event_detected( btn ) and mode == 0:
        SetAngleDoor1( angle, p )
        mode = 1
    if GPIO.event_detected( btn ) and mode == 1:
        SetAngleDoor2( angle, p )
        mode = 0
        
