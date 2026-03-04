# FROM ros:humble
FROM my-devcontainer-image:latest

ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
&& useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
&& apt-get update \
&& apt-get install -y sudo \
&& echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
&& chmod 0440 /etc/sudoers.d/$USERNAME
# Set environment for ROS 2
ENV SHELL=/bin/bash

# Pre-install system dependencies and ROS packages
RUN apt-get update && apt-get install -y \
    nvidia-cuda-toolkit \
    python3-pip \
    python3-opencv\
    libopencv-dev\
    net-tools \
    nano \
    iputils-ping \
    curl \
    fswebcam \
    nano \
    gnupg2 \
    lsb-release \
    sudo \
    build-essential \
    mesa-utils\
    python3-colcon-common-extensions \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-slam-toolbox \
    ros-humble-teleop-twist-keyboard \
    ros-humble-gazebo-ros-pkgs\
    ros-humble-gazebo-plugins \
    ros-humble-cv-bridge \
    ros-humble-rqt* \
    # ros-humble-gazebo-*\
    # ros-humble-ros-gz\
    ros-humble-cartographer \
    ros-humble-cartographer-ros \
    ros-humble-rviz2 \
    ros-humble-common-interfaces \
    ros-humble-tf2-tools \
    ros-humble-tf-transformations \
    ros-humble-xacro \
    ros-humble-joint-state-publisher \
    ros-humble-joint-state-publisher-gui \
    ros-humble-robot-state-publisher \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-controller-manager \
    ros-humble-joint-trajectory-controller \
    ros-humble-forward-command-controller \
    ros-humble-position-controllers \
    ros-humble-velocity-controllers \
    ros-humble-effort-controllers \
    ros-humble-joint-state-broadcaster \
    ros-humble-force-torque-sensor-broadcaster \
    ros-humble-ur \
    ros-humble-ur-description \
    ros-humble-ur-msgs \
    ros-humble-ur-client-library \
    ros-humble-hardware-interface \
    ros-humble-controller-interface \
    ros-humble-moveit \
    ros-humble-moveit-common \
    ros-humble-moveit-core \
    ros-humble-moveit-ros-planning \
    ros-humble-moveit-ros-planning-interface \
    ros-humble-moveit-ros-move-group \
    ros-humble-moveit-ros-visualization \
    ros-humble-moveit-planners \
    ros-humble-moveit-servo \
    ros-humble-tf2 \
    ros-humble-tf2-ros \
    ros-humble-tf2-eigen \
    ros-humble-tf2-geometry-msgs \
    ros-humble-geometry-msgs \
    ros-humble-sensor-msgs \
    ros-humble-std-msgs \
    ros-humble-control-msgs \
    ros-humble-trajectory-msgs \
    ros-humble-realtime-tools \
    ros-humble-control-toolbox \
    ros-humble-rqt-controller-manager \
    ros-humble-rqt-joint-trajectory-controller \
    ros-humble-plotjuggler \
    ros-humble-joy \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pyrealsense2
RUN pip install paho-mqtt

RUN usermod -aG video $USERNAME
RUN usermod -aG dialout $USERNAME
RUN usermod -aG plugdev $USERNAME
RUN usermod -aG input $USERNAME
    
# Source ROS setup
RUN echo "source /opt/ros/humble/setup.bash && source /home/ros2_ws/install/setup.bash" >> /home/$USERNAME/.bashrc

# Set default user
USER $USERNAME

CMD ["/bin/bash"]
