FROM ubuntu:latest

LABEL maintainer="dmsorensen@alaska.edu"

# Update the image to the latest packages
RUN apt-get update && apt-get upgrade -y

# Testing to make sure files are moved to image
CMD mkdir Battleship
ADD .* /Battleship
WORKDIR /Battleship
