FROM ubuntu:devel

LABEL maintainer="dmsorensen@alaska.edu"
USER root
# Update the image to the latest packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends python3
RUN apt-get install -y --no-install-recommends python3-pip

# Testing to make sure files are moved to image
WORKDIR /cs372_battle_ship
COPY . /cs372_battle_ship

RUN pip3 install pipenv
RUN pip3 install -U pytest
RUN pipenv install --dev
# TODO: Figure out why this doesn't work from the Docker file
RUN pip3 install -e .
RUN apt-get install nano