#!/bin/bash -f

stty -F /dev/ttyACM0 raw ispeed 1200 ospeed 1200 cs8 -cstopb ignpar eol 255 eof 255
bossac --port=ttyACM0 -U false -e -w -v -b ~/arduino-upload/sketch.bin -R
