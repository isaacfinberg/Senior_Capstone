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

