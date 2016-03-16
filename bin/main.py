#!/usr/bin/env python
#
# main.py
#
# Copyright (c) 2015-2016 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
""" Continuously reporting data from fplug.
"""
import argparse
import contextlib
import json
import pyfplug
import sys
import time
from logging import getLogger, StreamHandler, DEBUG

DEFAULT_DEVICE = "/dev/rfcomm0"
DEFAULT_INTERVAL = 60

logger = getLogger(__name__)


def run(path=DEFAULT_DEVICE, interval=DEFAULT_INTERVAL, output=sys.stdout):
    """ Continuously output data.

    Args:
      path: Path for a device. (default: /dev/rfcomm0)
      interval: Reporting interval. Unit is second. (default: 60sec)
      output: Writable object to output. (default: stdout)
    """
    while True:
        try:
            with contextlib.closing(pyfplug.FPlugDevice(path)) as dev:
                while True:
                    json.dump(dict(
                        temperature=dev.get_temperature(),
                        power=dev.get_power_realtime(),
                        humidity=dev.get_humidity(),
                        illuminance=dev.get_illuminance(),
                        time=int(time.time())
                    ), output)
                    output.write("\n")
                    time.sleep(interval)

        except KeyboardInterrupt:
            raise

        except Exception: # pylint: disable=broad-except
            logger.exception("Untracked exception occurred.")


def main():
    """ The main function.
    """
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "path", nargs="?", default=DEFAULT_DEVICE,
        help="Path to an RFCOMM device. (default: /dev/rfcomm0)")
    parser.add_argument(
        "--interval", type=int, default=DEFAULT_INTERVAL,
        help="interval seconds of reporting. (default: 60sec)")
    parser.add_argument(
        "--output", type=argparse.FileType("w"), default=sys.stdout,
        help="Output. (default: stdout)")

    run(**vars(parser.parse_args()))


if __name__ == "__main__":
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    try:
        main()
    except KeyboardInterrupt:
        pass
