# Python Web Application - Build Instructions

## Directory Structure

```
python-image/
├── blue/                    # Blue theme version
│   ├── web.py              # Python web server
│   ├── index.html          # Blue-themed HTML
│   ├── Dockerfile          # Container definition
│   └── README.md           # Blue theme instructions
│
├── green/                   # Green theme version
│   ├── web.py              # Python web server
│   ├── index.html          # Green-themed HTML
│   ├── Dockerfile          # Container definition
│   └── README.md           # Green theme instructions
│
└── BUILD_INSTRUCTIONS.md   # This file
```

## Quick Build Commands

### Build Blue Theme
```bash
cd blue/
podman build -t quay.io/your-username/python-web-app:blue .
podman push quay.io/your-username/python-web-app:blue
```

### Build Green Theme
```bash
cd green/
podman build -t quay.io/your-username/python-web-app:green .
podman push quay.io/your-username/python-web-app:green
```

## Build Both Images (One-liner)

```bash
# From the python-image directory
cd blue && podman build -t quay.io/your-username/python-web-app:blue . && cd ../green && podman build -t quay.io/your-username/python-web-app:green . && cd ..
```

## Push Both Images

```bash
podman push quay.io/your-username/python-web-app:blue
podman push quay.io/your-username/python-web-app:green
```

## Test Locally

### Test Blue Theme
```bash
podman run -p 8000:8000 -p 8001:8001 quay.io/your-username/python-web-app:blue
# Open: http://localhost:8000
```

### Test Green Theme
```bash
podman run -p 8000:8000 -p 8001:8001 quay.io/your-username/python-web-app:green
# Open: http://localhost:8000
```

## Differences Between Themes

Both themes have **identical functionality**:
- ✅ Pod logs display with "View Logs" button
- ✅ Auto-refresh toggle (5 seconds)
- ✅ Prometheus metrics on port 8001
- ✅ Request header logging
- ✅ Responsive design

**Only difference:** Color scheme
- **Blue Theme**: Professional blue gradient (#1e3a8a → #3b82f6)
- **Green Theme**: Fresh green gradient (#065f46 → #059669)

## Use Cases

### Blue Theme
- Production environments
- Primary deployments
- Customer-facing applications

### Green Theme
- Staging environments
- Development deployments
- Testing/QA environments

The different colors make it easy to visually distinguish between deployments when accessing via OpenShift routes or Kubernetes ingress.

## Dependencies

Both images include:
- Python 3.11 (Red Hat UBI9)
- prometheus_client
- psutil

All dependencies are installed automatically during the build process.

---

**Image Owner:** Sanjay Tripathi RH
