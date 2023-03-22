FROM humble_base

# Brain

WORKDIR /home

RUN mkdir -p brain_ws/src
COPY ./brain_turtle /home/brain_ws/src
WORKDIR /home/brain_ws
RUN sudo rosdep fix-permissions 
RUN rosdep update && rosdep install --from-paths src --ignore-src -r -y
RUN colcon build --symlink-install

# Turtlebot2 simulated
WORKDIR /home
RUN mkdir -p turtlebot2_ws/src
COPY ./turtlebot2 /home/turtlebot2_ws/src
COPY ./darknet_ros_yolov4/darknet_ros /home/turtlebot2_ws/src/darknet_ros
RUN /home/turtlebot2_ws/src/darknet_ros/rm_darknet_CMakeLists.sh
WORKDIR /home/turtlebot2_ws
RUN sudo rosdep fix-permissions 
RUN rosdep update && rosdep install --from-paths src --ignore-src -r -y

RUN apt update && \
    apt install -y \
        ros-humble-v4l2-camera

RUN colcon build --symlink-install --packages-skip darknet_ros darknet_ros_msgs

COPY empty_world_robot /home/turtlebot2_ws
COPY ./robotics_academy /RoboticsAcademy

RUN pip install websocket
RUN pip install websocket_server

# Django server
EXPOSE 8000

# Manager websocket
EXPOSE 8765

# Code websocket
EXPOSE 1905
EXPOSE 1904

# GUI websockets
EXPOSE 2303
EXPOSE 2304

# noVNC Console
EXPOSE 1108

# noVNC Gazebo
EXPOSE 6080

# WebRtc
EXPOSE 1831
