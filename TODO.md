## Code

* Create systemd service file + doc to install and enable
* Migrate backend to Go
    * Go install on RPi
        * https://gist.github.com/simoncos/49463a8b781d63b5fb8a3b666e566bb5
        * https://www.e-tinkers.com/2019/06/better-way-to-install-golang-go-on-raspberry-pi/
    * create a WiringPi based driver (in C/C++)
    * https://github.com/alexellis/rpi/
* Website
    ** GitHub Pages and/or https://gammabox.ytotech.com
* Cloud relay for Gamma Box
    * allows to acces to readings from everywhere
        * create simple owner app with React-Native
    * simple sensor page to be shared
    * transmitting settings
    * community readings aggregation and open-access to data flux

## Publicize

* Write a blog article
* Design a nice logo, neutral and non-offensive, even positive (cartoon-like)
* Create landing page for the project
* Create a better case, put a https://www.stickermule.com/fr on it
* Propose to sell some pre-assembled alpha-versions for enthusiasts ready to test it :)
* Add a plug-and-play display (DOT matrix or LED display) of measurements and ray hits
    * https://www.sparkfun.com/categories/51?filter_option%5Bsubcategory%5D%5B%5D=category_76&filter_option%5Bsubcategory%5D%5B%5D=category_89&filter_price_floor=&filter_price_ceil=
    * https://www.sparkfun.com/products/13304
    * https://www.sparkfun.com/products/14718
* Standardize data logging
    * See https://www.edf.org/sites/default/files/asw-date-timestamp-guidelines.pdf
* Work on Air quality extension/box
    * https://www.purpleair.com/map?module=AQI&conversion=C0&average=10&layer=standard&advanced=false&inside=true&outside=true&mine=true#5.18/43.826/-0.382
        * Closed source; black-box; not allowed by terms of service to change data reporting
    * https://aqdatacommons.org/faqs/software
    * https://github.com/Safecast/Safecast-Air / https://kithub.cc/safecast-air-quality-monitoring/ / https://blog.safecast.org/2016/08/air-quality-beta-kit/
    * https://openaq.org / https://openaq.org/#/map?_k=3uv6lb / https://docs.openaq.org/
    * https://www.eea.europa.eu/themes/air/air-quality-index
    * https://publiclab.org/notes/cfastie/11-28-2018/nano-particle-monitoring
    * http://aircasting.org/
* Safecast extension?
    * https://kithub.cc/safecast/
* Report to https://www.openradiation.org/?
