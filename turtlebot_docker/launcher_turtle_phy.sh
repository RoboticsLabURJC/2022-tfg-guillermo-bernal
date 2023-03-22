#!/bin/bash

. install/setup.bash
rviz2 &
ros2 launch openni2_camera camera_only.launch.py &
ros2 launch rplidar_ros rplidar.launch.py &