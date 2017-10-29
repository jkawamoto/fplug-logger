---
title: A Logger for F-Plug
type: homepage
date: 2016-04-20
lastmod: 2017-10-28
weight: 1
description: >-
  Continuously reporting data from Fujitsu's fplug.
---
[{{%img "https://img.shields.io/badge/license-MIT-blue.svg?style=flat" "MIT License" 78 20 %}}](https://github.com/jkawamoto/fplug-logger/blob/master/LICENSE)
[{{%img "https://codeclimate.com/github/jkawamoto/fplug-logger/badges/gpa.svg" "Code Climate" 110 20 %}}](https://codeclimate.com/github/jkawamoto/fplug-logger)
[{{%img "https://img.shields.io/badge/release-0.9.0-brightgreen.svg" "Release" 88 20 %}}](https://github.com/jkawamoto/fplug-logger/releases/)
[{{%img "https://img.shields.io/badge/dockerhub-jkawamoto%2Ffplug--logger-blue.svg" "Dockerhub" 210 20 %}}](https://hub.docker.com/r/jkawamoto/fplug-logger/)
[{{%img "https://images.microbadger.com/badges/image/jkawamoto/fplug-logger.svg" "Image information" 130 20 %}}](http://microbadger.com/images/jkawamoto/fplug-logger)
[{{%img "https://img.shields.io/badge/dockerhub-jkawamoto%2Frpi--fplug--logger-blue.svg" "Dockerhub" 230 20 %}}](https://hub.docker.com/r/jkawamoto/rpi-fplug-logger/)
[{{%img "https://images.microbadger.com/badges/image/jkawamoto/rpi-fplug-logger.svg" "Image information" 130 20 %}}](http://microbadger.com/images/jkawamoto/rpi-fplug-logger)

Continuously reporting data from Fujitsu's
[fplug](http://www.fujitsu.com/jp/group/bsc/services/f-plug/).

{{%img "img/fplug.png" "Fplug Logger" 666 346 true %}}

## Dependencies
  - python-serial
  - [pyfplug](https://github.com/hasegaw/pyfplug)

## Install with Docker

```
$ docker pull jkawamoto/fplug-logger
```

For Raspberry Pi,

```
$ docker pull jkawamoto/rpi-fplug-logger
```

## Useage
```
$ docker run -d -v /dev/rfcomm0:/dev/rfcomm0 --privileged \
    jkawamoto/fplug-logger [--interval INTERVAL] [--output OUTPUT] [path]
```
where

* positional arguments:
  * path: Path to an RFCOMM device. (default: /dev/rfcomm0)
* optional arguments:
  * --interval INTERVAL: Interval seconds of reporting. (default: 60sec)
  * --output OUTPUT: Output. (default: stdout)

If you run this on Raspberry Pi, use `jkawamoto/rpi-fplug-logger` instead of `jkawamoto/fplug-logger`.

## License
This software is released under the MIT License, see [LICENSE](https://github.com/jkawamoto/fplug-logger/blob/master/LICENSE).
