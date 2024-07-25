# Use Red Hat Universal Base Image with Python 3.9
FROM registry.access.redhat.com/ubi8/python-39

# Expose port 8000 for the HTTP server
EXPOSE 8000

# Set the working directory inside the container
WORKDIR /opt/app-root/src

# Copy the application files into the container
COPY . /opt/app-root/src

# Run the Python HTTP server
CMD ["python3", "-u", "web.py"]
