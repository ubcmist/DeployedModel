FROM ubuntu:16.04

MAINTAINER UBC MIST "ubc.mist@gmail.com"

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt && chmod -R 777 entrypoint.sh && ls

ENTRYPOINT ./entrypoint.sh

