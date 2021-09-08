
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

https://learn.adafruit.com/adafruit-magtag/overview<br>
https://learn.adafruit.com/adafruit-magtag/shipping-demo<br>
https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip<br>
https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard<br>
https://icanhazdadjoke.com/api<br>