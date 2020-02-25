# Test script to display media on screen
# Date: 02/20/2020 Status: Working

from subprocess import Popen

movie = '/home/pi/Senior-Capstone/test_video.mp4'
omxp = Popen( ['omxplayer', movie ] ) 
