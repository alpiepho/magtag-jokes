
This repo contains a number of the simple examples that are provided by the
Magtag Overview:
- https://learn.adafruit.com/adafruit-magtag/overview


The shipping demo code is in preloaded.ino and described here:
- https://learn.adafruit.com/adafruit-magtag/shipping-demo


Using CP bootloader:
- adafruit-circuitpython-adafruit_magtag_2.9_grayscale-en_US-6.3.0.uf2

Using bundle:
- https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip

## Files

The following is a list of the source files here.

- cpcode.py - default circuitpython from bundle (with stdout going to screen)
- dad_jokes.py - see below
- get_date_time.py - example from adafruit, <b>WARNING<b> This requires creating an account on https://accounts.adafruit.com/
- interent_test.py - example from adafruit, see below
- preloaded.ino - the pre loaded code on the hardware, see below
- preloaded.py - my port of preloaded to circuitpython
- sample_secret.py - example of secrets file that goes at root
- MagTag_Killed_By_Google - Google Graveyard example

Below are some more details about some of these files.
## Internet test

At minumum, need the following from bundle:

- adafruit_requests.mpy
- neopixel.mpy

This helps determine if you have the internet configured correctly on your board.

## Sample secrets

secrets.py saved in CIRCUITPY root along side code.py.  <b>WARNING<b> Be careful not to commit secret.py file.

secrets = {
    'ssid' : 'home_wifi_network',
    'password' : 'wifi_password',
    'aio_username' : 'my_adafruit_io_username',
    'aio_key' : 'my_adafruit_io_key',
    'timezone' : "America/New_York", # http://worldtimeapi.org/timezones
    }


## dad_jokes.py - Started Dad Joke

Mashup of Google Graveyard this Dad Joke api:

https://icanhazdadjoke.com/api

Rough outline:
- load random from offline jokes list
- display
- get battery
- wait 5 seconds
- attempt to get new joke from site
- display
- wait 5 seconds and go to deep sleep
- button press should start from top of file?

Offline or backup_jokes are created using the python script get_jokes.py.  These are useful to allow the 
app to seem like it's working while any online data is gathered.


## Learnings

TBD


## References

https://learn.adafruit.com/adafruit-magtag/overview<br>
https://learn.adafruit.com/adafruit-magtag/shipping-demo<br>
https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip<br>
https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard<br>
https://icanhazdadjoke.com/api<br>

## TODO List

- [done] Turn on internet_test.py
- [done] clean up README.md
- (optional) Signup for account and test time
- code preloaded.py from preloaded.ino
- turn on preloaded.py from preloaded.ino
- convert dad joke to a coffee pot watcher?


## Notes for magtag-dadjokes

This project was inspired by the following examples:

https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard<br>

https://icanhazdadjoke.com/api<br>

Everyone needs a good bad-dad-joke, and what better way than a gadget like the Magtag on 
the referidgerator to allow "sharing" them daily?

TODO: photo here

Files:
- code.py - main code file
- backup_jokes.py - set of jokes to show before online jokes found
- get_jokes.py - script to build new backup_jokes.py
- libs - CircuitPython libraries required
- sample_secrets.py - place at root of CIRCUITPY, contains wifi credentials, DO NOT COMMIT

Rough outline:
- set up text areas
- set title
- attempt to get current battery and display
- attempt open backup jokes and randomly display
- attempt to get online joke
- wait minimum of 1 minute (showing backup)
- show online joke
- if batt < 10%, enter deep sleep for 1 minutes (disables buttons)

## Setup

- run get_jokes.py to get your own set of backup_jokes.py.  Copy that to the CIRCUITPY drive.  
- use sample_secrets.py as template for secrets.py on CIRCUITPY drive.  I use guest wifi credentials
- copy libs to CIRCUITPY
- copy code.py to CIRCUITPY

At this point, the board should start and first display a backup jokes, and then later attempt to connect
and get  the next joke.

Board will check buttons every second:

- button A - next joke
- buttom B - default joke 
- button D - turn on leds for 30 seconds

If battery level drops to 10%, the device will enter deep sleep for 1 minute between online attempts. This has
the effect of disabling the buttons and leds.


## Learnings

- Using e-Ink device is a challenge because it is slow to update
- Connecting to web api is also a challenges, since it blocks the main loop 2-10 seconds

## TODO List

- [done] code dad joke from offline
- [done] turn on dad joke
- [fail] idea: split lines with extra \r\n
- [done] battery as a percent
- [done] fix battery percent
- [done] fix fonts
- [done] add next button to dad joke, enabled while awake
- [done] add light button to dad joke
- fix wake on button and use ligh sleep
- set font based on string length
- copy libs to repo
- finish repo and README

## Reference

Using CP bootloader:
- adafruit-circuitpython-adafruit_magtag_2.9_grayscale-en_US-6.3.0.uf2

Using bundle:
- https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip

