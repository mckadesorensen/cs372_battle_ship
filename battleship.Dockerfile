FROM ubuntu:latest

LABEL maintainer="dmsorensen@alaska.edu"

# Update the image to the latest packages
RUN apt-get update && apt-get upgrade -y

# Testing to make sure files are moved to image

WORKDIR /cs372_battle_ship
COPY . /cs372_battle_ship