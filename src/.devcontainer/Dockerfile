FROM ros:humble
# FROM my-devcontainer-image:latest

ARG USERNAME=team-user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create user without sudo
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Set environment for ROS 2
ENV SHELL=/bin/bash

# Pre-install system dependencies and ROS packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-opencv\
    libopencv-dev\
    net-tools \
    nano \
    iputils-ping \
    curl \
    fswebcam \
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
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    pyrealsense2==2.58.3.10794 \
    paho-mqtt==2.1.0

# Source ROS setup, add user to video group
RUN echo "source /opt/ros/humble/setup.bash && source /home/ros2_ws/install/setup.bash" >> /home/$USERNAME/.bashrc && \
    usermod -aG video $USERNAME

# Set default user
USER $USERNAME

CMD ["/bin/bash"]
