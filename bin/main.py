#!/usr/bin/env python
#
# main.py
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
""" Continuously reporting data from fplug.
"""
import os
import sys
ROOTPATH = os.path.dirname(__file__)
LIBPATH = os.path.join(ROOTPATH, "../lib/pyfplug/")
sys.path.append(LIBPATH)

import argparse
import contextlib
import json
import pyfplug
import time

DEFAULT_DEVICE = "/dev/rfcomm0"
DEFAULT_INTERVAL = 60


def run(path=DEFAULT_DEVICE, interval=DEFAULT_INTERVAL, output=sys.stdout):
    """ Continuously output data.

    Args:
      path: Path for a device. (default: /dev/rfcomm0)
      interval: Reporting interval. Unit is second. (default: 60sec)
      output: Writable object to output. (default: stdout)
    """
    with contextlib.closing(pyfplug.FPlugDevice(path)) as dev:
        while True:
            json.dump(dict(
                temperature=dev.get_temperature(),
                power=dev.get_power_realtime(),
                humidity=dev.get_humidity(),
                illuminance=dev.get_illuminance()
            ), output)
            output.write("\n")
            time.sleep(interval)


def main():
    """ The main function.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", nargs="?", default=DEFAULT_DEVICE,
        help="Path to an RFCOMM device. (default: /dev/rfcomm0)")
    parser.add_argument(
        "--interval", type=int, default=DEFAULT_INTERVAL,
        help="interval seconds of reporting.")
    parser.add_argument(
        "--output", type=argparse.FileType("w"), default=sys.stdout,
        help="Output. (default: stdout)")

    run(**vars(parser.parse_args()))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
