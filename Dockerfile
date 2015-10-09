#
# Dockerfile
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
#----------------------------------------------------------
# to run fplug-logger as a container on Raspberry Pi.
#
FROM resin/rpi-raspbian:wheezy-2015-10-07
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>

# Install a dependent library.
RUN apt-get update && apt-get install -y git python-serial

# Change the working directory.
WORKDIR /root

# Import a dependent library from GitHub.
RUN git clone https://github.com/hasegaw/pyfplug.git
ENV PYTHONPATH pyfplug

# Add the main script.
ADD bin .

CMD ./main.py