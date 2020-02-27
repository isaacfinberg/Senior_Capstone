from PiFunctions import *
import RPi.GPIO as GPIO
from time import sleep

prim1 = 17
prim2 = 27
sec1 = 22
sec2 = 10
wheel = 9
GPIO.setwarnings( False )
GPIO.setmode( GPIO.BCM )
GPIO.setup( prim1, GPIO.OUT )
GPIO.setup( prim2, GPIO.OUT )
GPIO.setup( sec1, GPIO.OUT )
GPIO.setup( sec2, GPIO.OUT )
GPIO.setup( wheel, GPIO.OUT )
p0 = GPIO.PWM( prim1, 50 )
p1 = GPIO.PWM( prim2, 50 )
p2 = GPIO.PWM( sec1, 50 )
p3 = GPIO.PWM( sec2, 50 )
p4 = GPIO.PWM( wheel, 50 )
p0.start( 2.5 ), p1.start( 2.5 ), p2.start( 2.5 ), p3.start( 2.5 ), p4.start( 2.5 )

none = None 
btns = [ 14, 15, 18 ]
check_mode = 0
for i in range( len( buttons ) ):
    GPIO.setup( btns[ i ], GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
    GPIO.add_event_detect( btns[ i ], GPIO.RISING )
while True:
    if GPIO.event_detected( btns[ 0 ] ):
        if mode == 0:
            three_one( p0, p1, none, 'open', none )
            mode = 1
        if mode == 2:
            two_one( p2, p3, none, none )
            mode = 1
    if GPIO.event_detected( btns[ 1 ] ):
        if mode == 1:
            one_two( p2, p3, none, none )
            mode = 2
        if mode == 3:
            three_two(p0, p1, p2, p3, p4, none, 'open', none )
            mode = 2
    if GPIO.even_detected( btns[ 2 ] ):
        if mode = 2:
            two_three( p0, p1, p2, p3, p4, none, 'closed', none )
            mode = 3
        if mode == 1:
            one_three(p0, p1, p4, none, 'closed', none )
            mode = 3