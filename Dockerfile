FROM ubuntu:22.04

WORKDIR /app
COPY requirements.txt requirements.txt


RUN apt-get update \
    && apt-get install -y \
    python3 \
    python3-pip\
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r /app/requirements.txt \
    && rm /app/requirements.txt
COPY ./python-app /app
#CMD [ "python3", "/app/python-app/app_test.py"]