# Test if audio jack works
# Date 02/19/2020 Status: Working

import pygame

pygame.mixer.init()
pygame.mixer.music.load( "test_audio.wav" )
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue