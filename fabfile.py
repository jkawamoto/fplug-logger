#pylint: skip-file
#
# fabfile.py
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
from fabric.api import *
from fabric.contrib.project import rsync_project
env.use_ssh_config = True

@task
def build():
    """ Build a Docker image.
    """
    run("mkdir -p fplug-logger")
    rsync_project(local_dir=".", remote_dir="fplug-logger")
    with cd("fplug-logger"):
        run("docker build -t jkawamoto/fplug-logger .")

@task
def rpi_build():
    """ Build a Docker image for Raspberry Pi.
    """
    run("mkdir -p fplug-logger")
    rsync_project(local_dir=".", remote_dir="fplug-logger")
    with cd("fplug-logger"):
        run("mv Dockerfile.rpi Dockerfile")
        run("docker build -t jkawamoto/rpi-fplug-logger .")
