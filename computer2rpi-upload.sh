#!/bin/bash -f

builddir="`ls -1t /tmp | grep build | head -n 1`"
binpath="`ls -1 $builddir | grep .bin | head -n 1`"
cat "$binpath" | ssh pi@10.0.0.1 "cat > ~/arduino-upload/sketch.bin && ~/github/tools/rpi2arduino-upload.sh"
