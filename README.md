
This project was inspired by the following examples:

https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard<br>

https://icanhazdadjoke.com/api<br>


Everyone needs a good bad-dad-joke, and what better way than a gadget like the Magtag on 
the refridgerator to allow "sharing" them daily?

<br>
<br>
<img src="./machine1.jpg" width="300">
<br>
<br>

A slider was added to the left side (Picture update pending) to select various options:
1. Dad Jokes
2. Quotes
3. Stoic Quotes
4. Bruce Lee Quotes
5. (also Bruce Lee Quotes)

<br>
Files:<br>

- code.py: main code file
- backup_jokes.py: set of jokes to show before online jokes found
- get_jokes.py: script to build new backup_jokes.py
- libs: CircuitPython libraries required
- sample_secrets.py: place at root of CIRCUITPY, contains wifi credentials, DO NOT COMMIT
- code1.py: alternative that can show other quotes WARNING: must alter message_type
- backup_quotes.py: quotes from zenquotes
- get_quotes.py: script to build new backup_quotes.py
- backup_stoics1.py: quotes from stoicquotesapi.com, classical authors
- get_stoics1.py: script to build new backup_stoics1.py
- backup_bruce.py: quotes from bruce lee
- get_bruce.py: script to build new backup_bruce.py


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

By default, if battery level drops to 80%, the device will enter deep sleep for 1 minute between online attempts. This has
the effect of disabling the buttons and leds.  This feature is disbled if any button is pressed within the first minute, and 
can be re-enabled by resetting the board.

The slider (resistor) attached to the left, uses one of the STEMMA 3 pin JST connectors for ground, 5v and Analog input.  The analog input is
measured on each wake to determine which set of data to show.


## Learnings

- Using e-Ink device is a challenge because it is slow to update
- Connecting to web api is also a challenge, since it blocks the main loop 2-10 seconds
- as of 9/11, power with led is 100 -> 84% in 24hrs
- [done] try removing green led - physically removed, actually shattered when I pulled it off :(
- [done] try direct to sleep

## TODO List

- [done] code dad joke from offline
- [done] turn on dad joke
- [fail] idea: split lines with extra \r\n
- [done] battery as a percent
- [done] fix battery percent
- [done] fix fonts
- [done] add next button to dad joke, enabled while awake
- [done] add light button to dad joke
- [done] copy libs to repo
- [done] finish repo and README
- [done] fix wake on button and use light sleep
- [done] add more jokes
- if too long, scroll
- set font based on string length
- add picture with slider
- create background panel to mark sliders and instructions



## Ideas

- [needs realtime clock] add use of WorldTimeAPI (http://worldtimeapi.org/api/timezone/America)
- [needs realtime clock] specify time time zone in secrets.py
- [done] refactor to handle quotes too
- [done] paramters in secrets.py
- [done] refactor variables etc
- [done] get quotes
- [done] get stoic
- [done] get bruce
- [done] check jumpers
- create flutter app with same look and random from backup*
- create Github action to update backups


## Reference

Using CP bootloader:
- adafruit-circuitpython-adafruit_magtag_2.9_grayscale-en_US-6.3.0.uf2

Using bundle:
- https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip

Other Links:
- https://learn.adafruit.com/adafruit-magtag/overview
- https://learn.adafruit.com/adafruit-magtag/shipping-demo
- https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210903/adafruit-circuitpython-bundle-6.x-mpy-20210903.zip
- https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard
- https://icanhazdadjoke.com/api
