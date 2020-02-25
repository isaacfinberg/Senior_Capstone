import RPi.GPIO as GPIO
from time import sleep
import pygame
from subprocess import Popen
import os
import sys
from PIL import Image
from PiFunctions import *

prim1 = 17
prim2 = 27
sec1 = 22
sec2 = 5
wheel = 6
servos = [ prim1, prim2, sec1, sec2, wheel ]
GPIO.setmode( GPIO.BCM )
p = []
for i in range( len( servos ) ):
    GPIO.setup( servos[ i ], GPIO.OUT )
    p[ i ] = GPIO.PWM( servos[ i ], 50 )
p[ 0 ].start( 2.5 ), p[ 2 ].start( 2.5 ), p[ 4 ].start( 2.5 )
p[ 1 ].start( 7.5 ), p[ 3 ].start( 7.5 )


btn1 = 23
btn2 = 24
btn3 = 25
btn4 = 16
GPIO.setup( btn1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
GPIO.setup( btn2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
GPIO.setup( btn3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
GPIO.setup( btn4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
check_mode = 3
check_media = 0
while True:
    if GPIO.input( btn4 ) == GPIO.HIGH and check_media == 0:
        while True:
        PlayMedia( '/home/pi/Senior-Capstone/video.mp4' )
        check_media = 1
        if GPIO.input( btn4 ) == GPIO.HIGH and check_media == 1:
            os.system( 'killall omxplayer.bin' )
            check_media == 0
    if GPIO.input( btn1 ) == GPIO.HIGH:
        if check_mode == 3:
            three_one( prim1, prim2, p, "sound_high.wav", 'open', "high.jpg )
            check_mode = 1
        if check_mode == 2:
            two_one( sec1, sec2, p, "sound_high.wav", "high.jpg" )
            check_mode = 1
    if GPIO.input( btn2 ) == GPIO.HIGH:
        if check_mode == 1:
            one_two( sec1, sec2, p, "sound_low.wav", "low.jpg" )
            check_mode = 2
        if check_mode == 3:
            three_two( prim1, prim2, sec1, sec2, p, "sound_low.wav", 'open', "low.jpg" )
            check_mode = 2
    if GPIO.input( btn3 ) == GPIO.HIGH:
        if check_mode == 2:
            two_three( prim1, prim2, sec1, sec2, p, "sound_neutral.wav", 'closed', "neutral.jpg" )
            check_mode = 3
        if check_mode == 1:
            one_three( prim1, prim2, p, "sound_neutral.wav", 'closed', "neutral.jpg" )
            check_mode = 3

p.stop()
GPIO.cleanup()