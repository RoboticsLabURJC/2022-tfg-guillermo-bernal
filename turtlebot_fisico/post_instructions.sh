rm src/openni2_camera/COLCON_IGNORE
rm src/turtlebot2/kobuki_base/kobuki_ros/COLCON_IGNORE 
rm src/turtlebot2/kobuki_base/kobuki_ros_interfaces/COLCON_IGNORE
echo Deleting COLCON_IGNORE files
cd src/Robots
git checkout humble
cd ../..
echo Robots on humble 
cd src/openni2_camera/openni2_camera
mkdir -p ~/.ros/camera_info
mv rgb_PS1080_PrimeSense.yaml ~/.ros/camera_info
cd ../../..
echo Camera driver ready

echo Physical kobuki driver ready
colcon build --symlink-install