# Python Web Application - Green Theme

This directory contains the **Green Theme** version of the Python web application.

## Files
- `web.py` - Python web server with logging and metrics
- `index.html` - Green-themed web interface
- `Dockerfile` - Container image definition

## Build the Image

```bash
# Navigate to this directory
cd green/

# Build with podman
podman build -t quay.io/your-username/python-web-app:green .

# Or build with docker
docker build -t quay.io/your-username/python-web-app:green .
```

## Push to Quay Registry

```bash
# Login to Quay
podman login quay.io

# Push the image
podman push quay.io/your-username/python-web-app:green
```

## Test Locally

```bash
# Run the container
podman run -p 8000:8000 -p 8001:8001 quay.io/your-username/python-web-app:green

# Access the application
# Web UI: http://localhost:8000
# Metrics: http://localhost:8001/python-metrics
```

## Features
- 🎨 Fresh green color theme
- 📋 Real-time pod logs display
- 📊 Prometheus metrics on port 8001
- 🔄 Auto-refresh logs every 5 seconds
- ✅ Fully responsive design

## Deploy to Kubernetes/OpenShift

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app-green
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-app
      theme: green
  template:
    metadata:
      labels:
        app: python-app
        theme: green
    spec:
      containers:
      - name: python-app
        image: quay.io/your-username/python-web-app:green
        ports:
        - containerPort: 8000
        - containerPort: 8001
```

**Image Owner:** Sanjay Tripathi RH
