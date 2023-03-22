#!/bin/bash

sudo docker run --net=host -it --privileged -p 8889:8889 -p 6080:6080 -p 8890:8890 -p 38065:30865 -p 11111:11111  -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X1 --rm tello_phy
