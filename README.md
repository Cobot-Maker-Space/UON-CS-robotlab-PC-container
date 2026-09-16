# Turtlebot Desktop Development Container 

[![CI](https://github.com/Cobot-Maker-Space/UON-CS-robotlab-PC-container/actions/workflows/ci.yml/badge.svg)](https://github.com/Cobot-Maker-Space/UON-CS-robotlab-PC-container/actions/workflows/ci.yml)

This repository contains a ready-to-use **Docker-based ROS 2 Humble** development environment for working with **TurtleBot3**. It includes Visual Studio Code support, useful extensions, and common ROS 2 packages preinstalled — making it easy to get started with TurtleBot simulation and development on any Linux machine.

---

## 📦 Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Cobot-Maker-Space/UON-CS-robotlab-PC-container.git
cd UON-CS-robotlab-PC-container/src
```

---

### 2. Open in VS Code

1. Launch a Terminal. Press `Ctrl+Alt+T`
2. Type the following in the Terminal to open VS Code.

```bash
cd COMP4034/src
code .
```  
3. You should see a `.devcontainer/` folder in the file tree now with other Turtlebot Packages alongside it.

---

### 3. Reopen in Dev Container

1. Now inside VS Code:
  - Press `Ctrl+Shift+P`
  - Type and select: `Dev Containers: Rebuild and Reopen in Container`
  - VS Code will now build and launch your ROS 2 container

2. You should see now a colcon build running on your screen and building all the Turtlebot packages.

3. When all of them are finished and it says `Press Any Key to Continue`

4. Go to the top menu and choose `Terminal` and click on `New Terminal`.

---

### 4. Test the Setup

Inside the container, a variety of environment variables are already set up through devcontainer.json file which would be matching the turtlebot environment variables, via `.rosenv` file which we have set up with Ansible on deployment.

Inside the container terminal:

```bash
source /opt/ros/humble/setup.bash
source /home/ros2_ws/install/setup.bash
ros2 topic list
```

If ROS 2 environment is installed correctly, and your Turtlebot is switched on for at least 2 Minutes, you’ll see a populated list of the Turtlebot Topics.

---

## 🛠 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `Docker permission denied` | Make sure your user is added to the `docker` group: <br> `sudo usermod -aG docker $USER` <br> Then logout your user and then log back in and check. |
| `Cannot access /dev/video0` | Add your user to the `video` group: <br> `sudo usermod -aG video $USER` |
| When launching Gazebo simulations, if it takes too much time and exits at `Spawn service failed. Exiting.` | Do not press `Ctrl + C` Let it fail completely and cleanly and then close it and run it again. |
<!--| `No ROS 2 topics across devices` | Ensure matching `ROS_DOMAIN_ID`, set `ROS_LOCALHOST_ONLY=0`, and use same `RMW_IMPLEMENTATION`. And try to repeat the 6th Step in case of wired setup. | -->
---

## 💡 Notes

- Default user inside container is `team-user` (non-root).
- Workspace is mounted to `/home/ros2_ws/src`.
- Includes support for Gazebo, SLAM, Navigation2, Teleop, Cartographer, and more.
- VS Code extensions preinstalled for ROS, C++, Python, and Git.

---

