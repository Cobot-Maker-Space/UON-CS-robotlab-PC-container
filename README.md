# Turtlebot Desktop Development Container 🐢🐳

This repository contains a ready-to-use **Docker-based ROS 2 Humble** development environment for working with **TurtleBot3**. It includes Visual Studio Code support, useful extensions, and common ROS 2 packages preinstalled — making it easy to get started with TurtleBot simulation and development on any Linux machine.

---

## 🚀 Features

- ROS 2 Humble preinstalled  
- VS Code extensions preconfigured  
- Docker-based isolation  
- TurtleBot3 packages ready to use  
- Network-ready for communication with physical robots

---

## 📦 Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/turtlebot-desktop-container.git
cd turtlebot-desktop-container/src
```

> Replace `yourusername` with your actual GitHub username.

---

### 2. Open in VS Code

1. Launch VS Code.
2. Open the `src/` directory of this repo.
3. You should see a `.devcontainer/` folder in the file tree.

---

### 3. Personalize the Container (IMPORTANT)

Open the following files:
- `.devcontainer/devcontainer.json`
- `.devcontainer/Dockerfile`

Search and replace all occurrences of:

```text
$USERNAME
```

with your **actual Linux terminal username** (e.g., `pszaa1`).

---

### 4. Start the Container

Inside VS Code:

- Press `Ctrl+Shift+P`
- Type and select: `Dev Containers: Reopen in Container`
- VS Code will now build and launch your ROS 2 container

---

### 5. Test the Setup

Once inside the container terminal:

```bash
ros2 topic list
```

If ROS 2 is installed correctly, you’ll see an empty or populated list depending on what's running.

---

## ⚠️ Potential Issues

| Issue | Solution |
|-------|----------|
| `Permission denied` on `/dev/video0` | Add the user to the `video` group or pass proper `--device` and `--privileged` flags in `devcontainer.json`. |
| ROS 2 topics not showing across network | Ensure matching `ROS_DOMAIN_ID` and `ROS_LOCALHOST_ONLY=0` across devices and that you're using the same `RMW_IMPLEMENTATION`. |
| Cannot build container due to `groupadd: group 'video' already exists` | Wrap the groupadd command in the Dockerfile with `|| true` to avoid failure if the group already exists. |
| Can't access GUI apps | Ensure X11 forwarding is set up or use an X11-enabled dev container setup (contact the maintainer for advanced support). |

---

## 🧠 Tips

- For TurtleBot3 networking, ensure host and container share the network (`--net=host`).
- Use `colcon build` and `ros2 launch` to build and run packages inside the container.
- Cache folders (`build/`, `install/`, `log/`) are volume-mounted for persistence.

---

## 📫 Maintainer

**Areeb Mohammad**  
Email: areeb@example.com  
GitHub: [@mohammad-areeb](https://github.com/mohammad-areeb)

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.