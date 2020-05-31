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

TODO

## Assembling and Wiring

See [PiPocketGeiger](https://github.com/MonsieurV/PiPocketGeiger) instructions for wiring your Raspberry Pi to your Radiation Watch Pocket Geiger.

## Installating the Gamma Box application

TODO pip package for gammabox?

```sh
# Ensure RPi.GPIO library is installed.
# Instruction here for Raspbian. See https://sourceforge.net/p/raspberry-gpio-python/wiki/install/
sudo apt-get install python3-rpi.gpio
sudo pip3 install PiPocketGeiger
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

## TODO

* Website
    ** GitHub Pages and/or https://gammabox.ytotech.com
* Cloud relay for Gamma Box
    * allows to acces to readings from everywhere
        * create simple owner app with React-Native
    * simple sensor page to be shared
    * transmitting settings
    * community readings aggregation and open-access to data flux

-------


### Contact

[Yoan](mailto:yoan@ytotech.com)

