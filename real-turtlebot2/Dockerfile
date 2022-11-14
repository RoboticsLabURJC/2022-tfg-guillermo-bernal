FROM ubuntu:22.04 

ENV DEBIAN_FRONTEND=noninteractive

# Install ROS2
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    sudo \
  && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null \
  && apt-get update && apt-get install -y \
    ros-humble-ros-base \
    python3-argcomplete \
  && rm -rf /var/lib/apt/lists/*

ENV ROS_DISTRO=humble
ENV AMENT_PREFIX_PATH=/opt/ros/humble
ENV COLCON_PREFIX_PATH=/opt/ros/humble
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/gazebo-11/plugins:/opt/ros/humble/opt/rviz_ogre_vendor/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/opt/ros/humble/lib:/usr/share/gazebo/../../lib/x86_64-linux-gnu/gazebo-11/plugins:
ENV PATH=/opt/ros/humble/bin:$PATH
ENV PYTHONPATH=/opt/ros/humble/lib/python3.10/site-packages
ENV ROS_PYTHON_VERSION=3
ENV ROS_VERSION=2
ENV QT_DEBUG_PLUGINS=1

RUN apt-get update && apt-get install -y \
  bash-completion \
  build-essential \
  cmake \
  gdb \
  git \
  pylint \
  python3-colcon-common-extensions \
  python3-pip \
  python3-rosdep \
  python3-vcstool \
  vim \
  wget \
  # Install ros distro testing packages
  ros-humble-ament-lint \
  ros-humble-launch-testing \
  ros-humble-launch-testing-ament-cmake \
  ros-humble-launch-testing-ros \
  && rm -rf /var/lib/apt/lists/* \
  && rosdep init || echo "rosdep already initialized" 

# Install the full release and rviz2
RUN apt-get update && apt-get install -y \
  ros-humble-desktop \
  ros-humble-joint-state-publisher \
  ros-humble-rviz2 \
  && rm -rf /var/lib/apt/lists/*

# Install gazebo
RUN apt-get update && apt-get install -q -y \
  gnupg \
  && wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null \
  && apt-get update && apt-get install -q -y \
    ros-humble-gazebo* \
  && rm -rf /var/lib/apt/lists/*


# Expose the nvidia driver to allow opengl. 
# Dependencies for glvnd and X11.
RUN apt-get update \
 && apt-get install -y -qq --no-install-recommends \
  libglvnd0 \
  libgl1 \
  libglx0 \
  libegl1 \
  libxext6 \
  libx11-6


# Liadas mias de muy poca verguenza
RUN apt-get install -y ros-humble-ecl-*
RUN apt-get install -y ros-humble-pcl-*

RUN apt-get install ros-humble-diagnostic-updater


# Env vars for the nvidia-container-runtime.
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility,compute
ENV QT_X11_NO_MITSHM 1

RUN sudo usermod -a -G audio root

# Include and build our Robot
RUN echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc

WORKDIR /home
RUN mkdir -p turtlebot2_ws/src
ADD ./turtlebot2 /home/turtlebot2_ws/src/turtlebot2
ADD ./ThirdParty /home/turtlebot2_ws/src/ThirdParty
ADD ./openni2_camera /home/turtlebot2_ws/src/openni2_camera
ADD ./post_instructions.sh /home/turtlebot2_ws/
ADD ./10-rplidar.rules /home/turtlebot2_ws/
ADD ./56-orbbec-usb.rules /home/turtlebot2_ws/
ADD ./camera.py /home/turtlebot2_ws/
WORKDIR /home/turtlebot2_ws
RUN chmod +x post_instructions.sh
RUN git clone https://github.com/IntelligentRoboticsLabs/Robots.git
RUN mv Robots src/
RUN sudo rosdep fix-permissions 



WORKDIR src/ThirdParty/kobuki_ftdi
RUN sudo cp 60-kobuki.rules /etc/udev/rules.d/
WORKDIR /home/turtlebot2_ws
RUN mv 56-orbbec-usb.rules /etc/udev/rules.d/
RUN mv 10-rplidar.rules /etc/udev/rules.d/


RUN rosdep update && rosdep install --from-paths src --ignore-src -r -y

RUN colcon build --symlink-install
