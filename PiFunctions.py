import RPi.GPIO as GPIO
import pigpio
from time import sleep
import pygame
from subprocess import Popen
import os
import sys
from PIL import Image
pi = pigpio.pi()

def SetAngleDoor( pw1, servo1, servo2 ):
    a1 = pi.get_servo_pulsewidth( servo1 )
    a2 = pi.get_servo_pulsewidth( servo2 )
    print( a1, a2 )
    j = 0
    for i in range( a1, pw1+1 ):
        pi.set_servo_pulsewidth( servo1, i )
        pi.set_servo_pulsewidth( servo2, a2 - j )
        j += 1
        sleep( .001 )
    
def SetAngleWheel( pw, servo ):
    a = pi.get_servo_pulsewidth( servo )
    if a == 1500 or a == 1501 or a == 1499:
        for i in range( a, pw ):
            pi.set_servo_pulsewidth( servo, i )
            sleep( .001 )
    else:
        for i in range( abs( a - pw ) ):
            pi.set_servo_pulsewidth( servo, a - i )
            sleep( .001 )          
    
def PlayAudio( audio_file ):
    pygame.mixer.init()
    pygame.mixer.music.load( audio_file )
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
        
def PlayMedia( media_file_path ):
    omxp = Popen( ['omxplayer', media_file_path ] )

def DisplayImg( image_file ):
    im = Image.open( image_file )
    im.show()
    
def three_one( prim1, prim2, wheel, sound_high, image_file ):
    pw1 = 2300
    pw = pw1
    SetAngleDoor( pw1, prim1, prim2 )
    SetAngleWheel( pw, wheel )
    #DisplayImg( image_file )
    #PlayAudio( sound_high )

def one_two( sec1, sec2, sound_low, image_file ):
    pw1 = 2300
    SetAngleDoor( pw1, sec1, sec2 )
    #DisplayImg( image_file )
    #PlayAudio( sound_low )
    
def two_one( sec1, sec2, sound_high, image_file ):
    pw1 = 1500
    SetAngleDoor( pw1, sec2, sec1 )
    #DisplayImg( image_file )
    #PlayAudio( sound_high )
    
def two_three( prim1, prim2, sec1, sec2, wheel, sound_neutral, image_file ):
    pw1 = 1500
    SetAngleDoor( pw1, sec2, sec1 )
    SetAngleWheel( pw1, wheel )
    SetAngleDoor( pw1, prim2, prim1 )
    #DisplayImg( image_file )
    #PlayAudio( sound_neutral )
    
def three_two( prim1, prim2, sec1, sec2, wheel, sound_low, image_file ):
    pw1 = 2300
    SetAngleDoor( pw1, prim1, prim2 )
    SetAngleWheel( pw1, wheel )
    SetAngleDoor( pw1, sec1, sec2 )
    #DisplayImg( image_file )
    #PlayAudio( sound_low )
    
def one_three( prim1, prim2, wheel, sound_neutral, image_file ):
    pw1 = 1500
    SetAngleWheel( pw1, wheel )
    SetAngleDoor( pw1, prim2, prim1 )
    #DisplayImg( image_file )
    #PlayAudio( sound_neutral )
    
def check_assembly_status( servos ):
    for i in range( len( servos ) ):
        pi.set_servo_pulsewidth( servos[ i ], 1500 )
#         if pi.get_servo_pulsewidth( servos[ i ] ) != 1500:
#             pi.set_servo_pulsewidth( servos[ i ], 1500 )