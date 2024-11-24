# Gamma Box

[![Build Status](https://travis-ci.org/MonsieurV/GammaBox.svg?branch=master)](https://travis-ci.org/MonsieurV/GammaBox)

> Your home radiation sensor

The Gamma Box monitors your home background radiation level, allowing you to share your Geiger Counter readings and get notified in case of high background radiations levels.

The Gamma Box aims to educate - to give a sense of how and when radiations occur and vary in a daily, weekly or monthly basis. You can easily transport it to experiment and learn how background radiation levels change with the nature of the environment (for example going to high elevation montains or rocky and granite rich lands).

It may also contribute to constitute a dense network of real-time Gamma ray sensors, for the joy of [hobbyists](http://radmon.org/) as for the gathering of [open-data](http://safecast.org/).

![](/misc/RadBox3.PNG?raw=true "RadBox main page")

Technically Gamma Box is a box currently composed of a [Raspberry Pi](https://www.raspberrypi.org/) ([RPi 2](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/) or more recent) interfaced with the [Radiation Watch Pocket Geiger counter](http://www.radiation-watch.co.uk/) (using [PiPocketGeiger](https://github.com/MonsieurV/PiPocketGeiger) driver).

# Getting started

## Shopping list

The Pocket Geiger is not sold anymore by Radiation Watch, neither by [Sparkfun](https://www.sparkfun.com/products/retired/14209). There remains some units to be sold by [RoboDyne](https://www.robo-dyne.com/prodotto/pocket-geiger-radiation-sensor-type-5/?lang=it) and [Hellas Digital](https://www.hellasdigital.gr/electronics/sensors/radiation/pocket-geiger-radiation-sensor-type-5/?sl=en).

## Assembling and Wiring

See [PiPocketGeiger](https://github.com/MonsieurV/PiPocketGeiger) instructions for wiring your Raspberry Pi to your Radiation Watch Pocket Geiger.

## Installating the Gamma Box application

First install the GPIO library and its dependencies.
Follow [PiPocketGeiger](https://github.com/MonsieurV/PiPocketGeiger) instructions.

We'll also use pipenv:

```sh
pip install pipenv --user --break-system-packages
```

(Follow the instructions to add pipenv to PATH)

Install the repository dependencies (mainly `PiPocketGeiger`):

```sh
pipenv install
```

You can try launching the server with

```sh
make run
```

This launch the web server on port `9898`.
You can access it (replacing your RPi host):

http://raspberrypi:9898

### Systemd installation

Follow the template in `misc/gamma-box.service` (modify `WorkingDirectory`, `ExecStart` and `User` following your installation). You can then install and activate the service to runs as a daemon:

```sh
sudo cp ./misc/gamma-box.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable gamma-box.service --now
```

Check its logs:

```sh
sudo journalctl -u gamma-box.service -f -n 100
```

-------

# Gamma Box Owner Handbook

--> [Consult the Gamma Box Owner Handbook](/handbook.md)

TODO Help wanted + publish on a GitHub pages website + PDF version with pandoc

-------

# FAQ

## Does the Gamma Box support other radiation sensors?

It may support other sensors by creating appropriate drivers. Contributions are welcome!

[Ask gently](https://github.com/MonsieurV/GammaBox/issues) to get help for making it work. :-)


-------


### Contact

[Yoan](mailto:yoan@ytotech.com)

