# Linux System Monitoring Dashboard

A modern real-time Linux system monitoring dashboard built on Fedora Linux using Python, Flask, psutil, Docker, and systemd.

This project provides live monitoring of CPU, memory, disk usage, network activity, and running processes through a responsive web interface designed for Linux environments.

---

# Features

* Real-time CPU monitoring
* Memory usage tracking
* Disk usage analytics
* Live network statistics
* Running process monitoring
* Interactive live charts
* Responsive dashboard UI
* Docker container support
* systemd service integration
* REST API endpoints
* Fedora/Linux compatible

---

# Dashboard Preview

Add screenshots inside:

```text
screenshots/
```

Example:

```text
screenshots/dashboard.png
```

Then add:

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

# Tech Stack

* Python
* Flask
* psutil
* HTML
* CSS
* JavaScript
* Chart.js
* Docker
* Docker Compose
* systemd
* Fedora Linux

---

# Project Structure

```bash
linux-system-monitor/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .dockerignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── screenshots/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/NallellaNihal/linux-system-monitor.git
cd linux-system-monitor
```

---

# Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python app.py
```

Open browser:

```text
http://localhost:5000
```

---

# Docker Setup

## Build and Run

```bash
docker compose up --build
```

## Run in Background

```bash
docker compose up -d
```

## Stop Container

```bash
docker compose down
```

---

# systemd Service Setup

## Start Service

```bash
sudo systemctl start linux-monitor
```

## Enable on Boot

```bash
sudo systemctl enable linux-monitor
```

## Check Status

```bash
sudo systemctl status linux-monitor
```

## View Logs

```bash
journalctl -u linux-monitor -f
```

---

# API Endpoints

## System Statistics

```text
/api/stats
```

Returns:

* CPU usage
* Memory usage
* Disk usage
* Network statistics
* System information
* System uptime

---

## Running Processes

```text
/api/processes
```

Returns:

* Process ID
* Process name
* CPU usage
* Memory usage

---

# Linux Concepts Demonstrated

This project demonstrates practical Linux and DevOps skills including:

* Linux system monitoring
* Process management
* Linux networking statistics
* REST API development
* Docker containerization
* systemd service management
* Fedora Linux administration
* Python backend development
* Real-time monitoring dashboards

---

# Future Improvements

* GPU monitoring
* Log monitoring dashboard
* Email alert system
* Prometheus integration
* Grafana dashboards
* Authentication system
* SSH remote monitoring
* Security auditing tools
* Export reports as PDF/CSV

---

# Screenshots Folder

Create folder:

```bash
mkdir screenshots
```

Save dashboard screenshots inside it.

---

# Requirements

```text
Flask
psutil
```

Generate automatically:

```bash
pip freeze > requirements.txt
```

---

# GitHub Upload

```bash
git add .
git commit -m "Updated project documentation"
git push
```

---

# Learning Outcomes

Through this project, I gained hands-on experience with:

* Fedora Linux development
* Linux resource monitoring
* Docker containerization
* systemd services
* Backend API development
* Infrastructure monitoring
* Real-time dashboard design
* GitHub project deployment

---

# Author
Nihal

GitHub: [NallellaNihal GitHub](https://github.com/NallellaNihal?utm_source=chatgpt.com)

LinkedIn: [Nihal LinkedIn](https://linkedin.com/in/nallella-nihal?utm_source=chatgpt.com)
