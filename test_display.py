# Test script to display media on screen
# Date: 02/20/2020 Status: Working

from subprocess import Popen

movie = '/home/pi/Downloads/Video fast forward.mp4'
omxp = Popen( ['omxplayer', movie ] ) 
