import RPi.GPIO as GPIO
import pigpio
from PiFunctions import *

pi = pigpio.pi()

prim1 = 17
prim2 = 27
sec1 = 22
sec2 = 10
wheel = 9
servo_bootup = [ sec1, sec2, wheel, prim1, prim2 ]
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False ) 
check_assembly_status( servo_bootup )
            
btns = [ 14, 15, 18 ]
check_mode = 3
for i in range( len( btns ) ):
    GPIO.setup( btns[ i ], GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
    GPIO.add_event_detect( btns[ i ], GPIO.RISING )
while True:
    PlayMedia( '/home/pi/Downloads/Video fast forward.mp4' )
    if GPIO.event_detected( btns[ 0 ] ):
        if check_mode == 3:
            three_one( prim1, prim2, wheel, "test_audio.wav", 'one.jpg' )
            check_mode = 1
        if check_mode == 2:
            two_one( sec1, sec2, "test_audio.wav", 'one,jpg' )
            check_mode = 1
    if GPIO.event_detected( btns[ 1 ] ):
        if check_mode == 1:
            one_two( sec1, sec2, "test_audio.wav", 'two.jpg' )
            check_mode = 2
        if check_mode == 3:
            three_two( prim1, prim2, sec1, sec2, wheel, "test_audio.wav", 'two.jpg' )
            check_mode = 2
    if GPIO.event_detected( btns[ 2 ] ):
        if check_mode == 2:
            two_three( prim1, prim2, sec1, sec2, wheel, "test_audio.wav", 'Qantas.mp4' )
            check_mode = 3
        if check_mode == 1:
            one_three( prim1, prim2, wheel, "test_audio.wav", 'Qantas.mp4' )
            check_mode = 3