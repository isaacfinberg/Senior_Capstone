import RPi.GPIO as GPIO
from time import sleep
import pygame
from subprocess import Popen
import os
import sys
from PIL import Image

def SetAngleDoor( angle, p1, p2 ):
    for i in range( 0, angle ):
        dutyRatioL = i / 18 + 2
        dutyRatioR = ( angle - i ) / 18 + 2
        p1.ChangeDutyCycle( dutyRatioL )
        p2.ChangeDutyCycle( dutyRatioR )
        sleep( .01 )
    
def SetAngleWheel( angle, p, state ):
    if state == 'closed':
        for i in range( 0, angle ):
            dutyRatio = i / 18 + 2
            p.ChangeDutyCycle( dutyRatio )
            sleep( .01 )
    else:
        for i in range( 0, angle ):
            dutyRatio = ( angle - i ) / 18 + 2
            p.ChangeDutyCycle( dutyRatio )
            sleep( .01 )          
    
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
    
def three_one( prim1, prim2, p, sound_high, state, image_file ):
    angle = 90
    SetAngleDoor( angle, prim1, prim2, p )
    SetAngleWheel( angle, p, state )
    DisplayImg( image_file )
    PlayAudio( sound_high )

def one_two( sec1, sec2, p, sound_low, image_file ):
    angle = 90
    SetAngleDoor( angle, sec1, sec2, p )
    DisplayImg( image_file )
    PlayAudio( sound_low )
    
def two_one( sec1, sec2, p, sound_high, image_file ):
    angle = 90
    SetAngleDoor( angle, sec2, sec1, p )
    DisplayImg( image_file )
    PlayAudio( sound_high )
    
def two_three( prim1, prim2, sec1, sec2, p, sound_neutral, state, image_file ):
    angle = 90
    SetAngleDoor( angle, sec2, sec1, p )
    SetAngleWheel( angle, p, state )
    SetAngleDoor( angle, prim2, prim1, p )
    DisplayImg( image_file )
    PlayAudio( sound_neutral )
    
def three_two( prim1, prim2, sec1, sec2, p, sound_low, state, image_file ):
    angle = 90
    SetAngleDoor( angle, prim1, prim2, p )
    SetAngleWheel( angle, p, state )
    SetAngleDoor( angle, sec1, sec2, p )
    DisplayImg( image_file )
    PlayAudio( sound_low )
    
def one_three( prim1, prim2, p, sound_neutral, state, image_file ):
    angle = 90
    SetAngleWheel( angle, p, state )
    SetAngleDoor( angle, prim2, prim1, p )
    DisplayImg( image_file )
    PlayAudio( sound_neutral )