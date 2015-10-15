#!/bin/bash
#
# entrypoint.sh
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
if [[ $# = 0 || $1 = -* ]]; then
  exec ./main.py $@
fi
exec $@
