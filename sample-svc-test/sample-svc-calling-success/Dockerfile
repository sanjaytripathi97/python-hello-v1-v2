FROM registry.access.redhat.com/ubi8/python-39

EXPOSE 8000

COPY . /opt/app-root/src

WORKDIR /opt/app-root/src

# Install necessary dependencies
RUN pip install requests

CMD /bin/bash -c 'python3 -u web.py'
