Raspberry Pi Wiegand RFID controller
====================================

Python code to connect an Wiegand RFID Card Reader on _Raspberry Pi_ using the _RPIO_ library.

**Due to performance issues, we decided to rewrite the [program in C](https://github.com/LukeMarlin/Rpi-RFID-Reader-C "version C") with wiringPi lib.**

##Connection diagram

![Connection diagram](https://github.com/LukeMarlin/pmiCardReader/blob/master/diagram.png?raw=true "Connection diagram")


##Links

* [RPIO Library](https://pypi.python.org/pypi/RPIO "Link to the RPIO Library")
```sudo pip install RPIO```
* [Raspberry Pi](http://www.raspberrypi.org "Link to the Raspberry Pi projet home page")

###good article about how Wiegand card readers function
http://www.thegategeek.com/how-do-wiegand-card-readers-and-devices-work/
