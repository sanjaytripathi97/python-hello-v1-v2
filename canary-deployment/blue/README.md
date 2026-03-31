# Python Web Application - Blue Theme

This directory contains the **Blue Theme** version of the Python web application.

## Files
- `web.py` - Python web server with logging and metrics
- `index.html` - Blue-themed web interface
- `Dockerfile` - Container image definition

## Build the Image

```bash
# Navigate to this directory
cd blue/

# Build with podman
podman build -t quay.io/your-username/python-web-app:blue .

# Or build with docker
docker build -t quay.io/your-username/python-web-app:blue .
```

## Push to Quay Registry

```bash
# Login to Quay
podman login quay.io

# Push the image
podman push quay.io/your-username/python-web-app:blue
```

## Test Locally

```bash
# Run the container
podman run -p 8000:8000 -p 8001:8001 quay.io/your-username/python-web-app:blue

# Access the application
# Web UI: http://localhost:8000
# Metrics: http://localhost:8001/python-metrics
```

## Features
- 🎨 Professional blue color theme
- 📋 Real-time pod logs display
- 📊 Prometheus metrics on port 8001
- 🔄 Auto-refresh logs every 5 seconds
- ✅ Fully responsive design

## Deploy to Kubernetes/OpenShift

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app-blue
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-app
      theme: blue
  template:
    metadata:
      labels:
        app: python-app
        theme: blue
    spec:
      containers:
      - name: python-app
        image: quay.io/your-username/python-web-app:blue
        ports:
        - containerPort: 8000
        - containerPort: 8001
```

**Image Owner:** Sanjay Tripathi RH
