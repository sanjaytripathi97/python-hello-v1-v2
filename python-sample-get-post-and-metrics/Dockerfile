# Use Red Hat UBI9 with Python 3.11
FROM registry.access.redhat.com/ubi9/python-311

# Switch to root to install packages
USER root

# Optional: update OS packages
RUN dnf -y update && dnf clean all

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir prometheus_client psutil

# Expose ports
EXPOSE 8000
EXPOSE 8001

# Set working directory
WORKDIR /opt/app-root/src

# Copy application files
COPY . /opt/app-root/src

# Run the Python web server
CMD ["python3", "-u", "web.py"]
