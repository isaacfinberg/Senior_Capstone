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
    
def three_one( p1, p2, sound_high, state, image_file ):
    angle = 90
    SetAngleDoor( angle, p1, p2 )
    SetAngleWheel( angle, p, state )
    #DisplayImg( image_file )
    #PlayAudio( sound_high )

def one_two( p1, p2, sound_low, image_file ):
    angle = 90
    SetAngleDoor( angle, p1, p2 )
    #DisplayImg( image_file )
    #PlayAudio( sound_low )
    
def two_one( p1, p2, sound_high, image_file ):
    angle = 90
    SetAngleDoor( angle, p2, p1 )
    #DisplayImg( image_file )
    #PlayAudio( sound_high )
    
def two_three( p1, p2, p3, p4, p5, sound_neutral, state, image_file ):
    angle = 90
    SetAngleDoor( angle, p2, p1 )
    SetAngleWheel( angle, p5, state )
    SetAngleDoor( angle, p2, p1 )
    #DisplayImg( image_file )
    #PlayAudio( sound_neutral )
    
def three_two( p1, p2, p3, p4, p5, sound_low, state, image_file ):
    angle = 90
    SetAngleDoor( angle, p1, p2 )
    SetAngleWheel( angle, p5, state )
    SetAngleDoor( angle, p3, p4 )
    #DisplayImg( image_file )
    #PlayAudio( sound_low )
    
def one_three( p1, p2, p3, sound_neutral, state, image_file ):
    angle = 90
    SetAngleWheel( angle, p3, state )
    SetAngleDoor( angle, p2, p1 )
    #DisplayImg( image_file )
    #PlayAudio( sound_neutral )