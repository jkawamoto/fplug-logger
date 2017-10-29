# A Logger for F-Plug
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![Code Climate](https://codeclimate.com/github/jkawamoto/fplug-logger/badges/gpa.svg)](https://codeclimate.com/github/jkawamoto/fplug-logger)
[![Release](https://img.shields.io/badge/release-0.9.0-brightgreen.svg)](https://github.com/jkawamoto/fplug-logger/releases/)
[![Dockerhub](https://img.shields.io/badge/dockerhub-jkawamoto%2Ffplug--logger-blue.svg)](https://hub.docker.com/r/jkawamoto/fplug-logger/)
[![Image information](https://images.microbadger.com/badges/image/jkawamoto/fplug-logger.svg)](http://microbadger.com/images/jkawamoto/fplug-logger)
[![Dockerhub](https://img.shields.io/badge/dockerhub-jkawamoto%2Frpi--fplug--logger-blue.svg)](https://hub.docker.com/r/jkawamoto/rpi-fplug-logger/)
[![Image information](https://images.microbadger.com/badges/image/jkawamoto/rpi-fplug-logger.svg)](http://microbadger.com/images/jkawamoto/rpi-fplug-logger)


Continuously reporting data from Fujitsu's
[fplug](http://www.fujitsu.com/jp/group/bsc/services/f-plug/).

## Dependencies
  - python-serial
  - [pyfplug](https://github.com/hasegaw/pyfplug)

## Install with Docker

```sh
$ docker pull jkawamoto/fplug-logger
```

For Raspberry Pi,

```sh
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
This software is released under the MIT License, see [LICENSE](LICENSE).
