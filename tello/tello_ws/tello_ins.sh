#!/bin/sh

ros2 service call /tello_action tello_msgs/TelloAction "{cmd: 'takeoff'}"
sleep 4
ros2 service call /tello_action tello_msgs/TelloAction "{cmd: 'stop'}"
sleep 3
ros2 service call /tello_action tello_msgs/TelloAction "{cmd: 'cw 90'}"
sleep 4
ros2 service call /tello_action tello_msgs/TelloAction "{cmd: 'forward 10'}"
