# Docker Interview Guide 🐳

## Table of Contents
1. [What is Docker?](#what-is-docker)
2. [Why Docker?](#why-docker)
3. [Docker Concepts](#docker-concepts)
4. [Dockerfile Explained](#dockerfile-explained)
5. [Docker Commands](#docker-commands)
6. [Common Interview Questions](#common-interview-questions)
7. [Docker Compose](#docker-compose)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

---

## What is Docker? 🐳

Docker is like a **shipping container** for your applications. Just like how shipping containers can carry any cargo and work on any ship, Docker containers can run any application on any computer.

### Key Terms:
- **Image**: Blueprint/Template (like a class in programming)
- **Container**: Running instance (like an object in programming)
- **Dockerfile**: Instructions to build an image
- **Registry**: Storage for Docker images (Docker Hub, AWS ECR)

---

## Why Docker? 

### The Problem Docker Solves:
- **"It works on my machine" problem** - Your app works on your laptop but fails on production server
- **Environment inconsistency** - Different OS, Python versions, dependencies
- **Deployment complexity** - Manual setup on each server
- **Scaling issues** - Hard to replicate exact environment

### Benefits:
- ✅ **Consistency** - Same environment everywhere (dev, test, production)
- ✅ **Isolation** - Each app runs in its own container, no conflicts
- ✅ **Scalability** - Easy to scale up/down
- ✅ **Portability** - Run anywhere (AWS, Azure, your laptop)
- ✅ **Resource efficiency** - Less overhead than VMs
- ✅ **Version control** - Track changes to your environment

---

## Docker Concepts

### Image vs Container
```
Dockerfile → Docker Image → Docker Container
   (Recipe)    (Blueprint)    (Running App)
```

### Docker Architecture:
```
┌─────────────────┐
│   Docker Client │
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Docker Daemon  │
└─────────┬───────┘
          │
┌─────────▼───────┐
│   Containers    │
└─────────────────┘
```

---

## Dockerfile Explained

Let's break down our Flask app's Dockerfile:

### 1. Base Image
```dockerfile
FROM python:3.11-slim
```
**What it does:** Starts with a base image that has Python 3.11
**Interview answer:** "We use a base image as our starting point. `slim` means smaller size, no unnecessary packages."

### 2. Working Directory
```dockerfile
WORKDIR /app
```
**What it does:** Sets `/app` as the working directory inside container
**Interview answer:** "Like `cd /app` - all commands will run from this directory"

### 3. Environment Variables
```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
```
**What it does:** Sets environment variables
**Interview answer:** "These configure Python and Flask behavior. `PYTHONUNBUFFERED=1` ensures logs appear immediately."

### 4. Install System Dependencies
```dockerfile
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*
```
**What it does:** Installs system packages, then cleans up
**Interview answer:** "We install `gcc` for compiling Python packages, then clean up to reduce image size."

### 5. Install Python Dependencies
```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```
**What it does:** Copies requirements file, then installs Python packages
**Interview answer:** "We copy requirements first for better Docker layer caching. If code changes, we don't reinstall packages."

### 6. Copy Application Code
```dockerfile
COPY . .
```
**What it does:** Copies all application files
**Interview answer:** "This copies our Flask app code into the container."

### 7. Security - Non-root User
```dockerfile
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser
```
**What it does:** Creates a non-root user for security
**Interview answer:** "Security best practice - don't run as root. We create a regular user and switch to it."

### 8. Expose Port
```dockerfile
EXPOSE 5000
```
**What it does:** Documents which port the app uses
**Interview answer:** "This documents that our app uses port 5000. It doesn't actually open the port - that's done when running the container."

### 9. Health Check
```dockerfile
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1
```
**What it does:** Checks if app is healthy every 30 seconds
**Interview answer:** "Docker will check if our app is running by calling `/health` endpoint. If it fails 3 times, container is marked unhealthy."

### 10. Run Command
```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
```
**What it does:** Runs the Flask app with Gunicorn
**Interview answer:** "This is the command that runs when container starts. Gunicorn is a production WSGI server with 4 worker processes."

---

## Docker Commands

### Basic Commands
```bash
# Build image
docker build -f Dockerfile.backend -t my-flask-app .

# Run container
docker run -p 5000:5000 my-flask-app

# Run in background
docker run -d -p 5000:5000 my-flask-app

# Run with environment variables
docker run -e FLASK_DEBUG=true -p 5000:5000 my-flask-app

# List images
docker images

# List running containers
docker ps

# List all containers
docker ps -a

# Stop container
docker stop <container_id>

# Remove container
docker rm <container_id>

# Remove image
docker rmi <image_id>

# View logs
docker logs <container_id>

# Execute command in running container
docker exec -it <container_id> /bin/bash
```

### Advanced Commands
```bash
# Build with no cache
docker build --no-cache -t my-flask-app .

# Run with volume mount
docker run -v $(pwd):/app -p 5000:5000 my-flask-app

# Run with custom name
docker run --name my-app -p 5000:5000 my-flask-app

# Inspect container
docker inspect <container_id>

# View container stats
docker stats <container_id>
```

---

## Common Interview Questions

### Q: What's the difference between Docker and Virtual Machine?

**Answer:**
| Docker | Virtual Machine |
|--------|----------------|
| Shares host OS kernel | Full OS + App |
| Lightweight (10-100 MB) | Heavy (1-2 GB) |
| Fast startup | Slow startup |
| Less isolation | More isolation |
| Better resource utilization | Higher resource usage |

### Q: What are Docker layers?

**Answer:** "Each instruction in Dockerfile creates a layer. Layers are cached and reused. If one layer changes, only that layer and below are rebuilt. This makes builds faster and more efficient."

### Q: How do you optimize Docker image size?

**Answer:**
- Use `slim` or `alpine` base images
- Combine RUN commands to reduce layers
- Use `.dockerignore` to exclude unnecessary files
- Don't install unnecessary packages
- Clean up package caches in same RUN command
- Use multi-stage builds for complex apps

### Q: What's the difference between COPY and ADD?

**Answer:**
- **COPY:** Simple file copying (recommended)
- **ADD:** Can copy from URLs and extract tar files
- **Best practice:** Use COPY unless you need ADD's extra features

### Q: What's the difference between CMD and ENTRYPOINT?

**Answer:**
- **CMD:** Default command, can be overridden
- **ENTRYPOINT:** Fixed command, parameters can be added
- **Example:**
  ```dockerfile
  ENTRYPOINT ["python"]
  CMD ["app.py"]
  # Can run: docker run my-app --help
  ```

### Q: How do you handle secrets in Docker?

**Answer:**
- Use Docker secrets (Docker Swarm)
- Use environment variables
- Use external secret management (AWS Secrets Manager)
- Mount secret files as read-only volumes
- Never put secrets in Dockerfile or image

### Q: What's Docker Compose?

**Answer:** "Docker Compose manages multiple containers as a single application. Perfect for microservices. You define services in a YAML file and can start/stop all services with one command."

### Q: How do you debug a Docker container?

**Answer:**
- `docker logs <container_id>` - View logs
- `docker exec -it <container_id> /bin/bash` - Enter container
- `docker inspect <container_id>` - Inspect container details
- `docker stats <container_id>` - View resource usage

---

## Docker Compose

### Example docker-compose.yml:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    depends_on:
      - database
    volumes:
      - .:/app
  
  database:
    image: postgres:13
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

### Docker Compose Commands:
```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Build and start
docker-compose up --build

# Stop all services
docker-compose down

# View logs
docker-compose logs

# Scale service
docker-compose up --scale web=3
```

---

## Best Practices

### 1. Security
- Don't run as root user
- Use specific image tags, not `latest`
- Scan images for vulnerabilities
- Use secrets management
- Keep base images updated

### 2. Performance
- Use multi-stage builds
- Minimize layers
- Use .dockerignore
- Optimize for size
- Use health checks

### 3. Development
- Use volumes for development
- Use docker-compose for local development
- Keep Dockerfile simple
- Document your Dockerfile

### 4. Production
- Use specific versions
- Set resource limits
- Use health checks
- Monitor container logs
- Use orchestration (Kubernetes, Docker Swarm)

---

## Troubleshooting

### Common Issues:

#### 1. Container won't start
```bash
# Check logs
docker logs <container_id>

# Check if port is already in use
netstat -tulpn | grep :5000
```

#### 2. Permission denied
```bash
# Check file permissions
ls -la

# Run with proper user
docker run --user $(id -u):$(id -g) my-app
```

#### 3. Out of space
```bash
# Clean up unused images
docker image prune

# Clean up everything
docker system prune -a
```

#### 4. Can't connect to container
```bash
# Check if container is running
docker ps

# Check port mapping
docker port <container_id>

# Test connection
curl http://localhost:5000
```

---

## Quick Reference

### Essential Commands:
```bash
# Build and run
docker build -t my-app .
docker run -p 5000:5000 my-app

# Development
docker run -v $(pwd):/app -p 5000:5000 my-app

# Production
docker run -d --name my-app -p 5000:5000 my-app

# Debugging
docker logs my-app
docker exec -it my-app /bin/bash
```

### Key Interview Points:
1. **Docker solves "works on my machine" problem**
2. **Images are blueprints, containers are running instances**
3. **Layers are cached for faster builds**
4. **Security: Don't run as root**
5. **Optimize for size and performance**
6. **Docker Compose for multi-container apps**
7. **Use health checks for production**
8. **Environment variables for configuration**

---

## Practice Questions for Interview

1. **Explain Docker architecture in simple terms**
2. **How would you optimize a large Docker image?**
3. **What's the difference between Docker and Kubernetes?**
4. **How do you handle database connections in Docker?**
5. **Explain Docker networking**
6. **How do you monitor Docker containers?**
7. **What's the difference between Docker and Podman?**
8. **How do you handle logging in Docker?**
9. **Explain Docker volumes and bind mounts**
10. **How do you deploy Docker containers in production?**

---

**Remember:** Practice with real projects! Build, run, and debug Docker containers to gain hands-on experience. Good luck with your interviews! 🚀
