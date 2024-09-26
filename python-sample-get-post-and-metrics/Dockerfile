# Use Red Hat Universal Base Image with Python 3.9
FROM registry.access.redhat.com/ubi8/python-39

# Install required Python packages
RUN pip install prometheus_client psutil

# Expose ports for the HTTP server and metrics
EXPOSE 8000
EXPOSE 8001

# Set the working directory inside the container
WORKDIR /opt/app-root/src

# Copy the application files into the container
COPY . /opt/app-root/src

# Run the Python HTTP server
CMD ["python3", "-u", "web.py"]
