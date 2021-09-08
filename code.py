# Started from https://learn.adafruit.com/google-graveyard-with-adafruit-magtag/code-the-google-graveyard

# import board
# import json
import time
import random
import alarm
import terminalio
from adafruit_magtag.magtag import MagTag


DATA_SOURCE = "https://icanhazdadjoke.com/"

MAGTAG = MagTag(status_neopixel=None)
MAGTAG.peripherals.neopixel_disable = False

# title
MAGTAG.add_text(
    text_font=terminalio.FONT,
    text_position=(
        7,
        2,
    ),
    text_wrap=30,
    text_anchor_point=(0, 0),
    text_scale=1,
    line_spacing=0.9,
    is_data=False,
)

# battery
MAGTAG.add_text(
    text_font=terminalio.FONT,
    text_position=(
        205,
        2,
    ),
    text_anchor_point=(0, 0),
    text_scale=1,
    is_data=False,
)

# joke
MAGTAG.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(
        5,
        20,
    ),
    text_wrap=34,
    text_anchor_point=(0, 0),
    text_scale=1.0,
    line_spacing=1.0,
    is_data=False,
)

# offline/online
MAGTAG.add_text(
    text_font=terminalio.FONT,
    text_position=(
        215,
        110,
    ),
    text_wrap=40,
    text_anchor_point=(0, 0),
    text_scale=1.0,
    line_spacing=1.0,
    is_data=False,
)
MAGTAG.preload_font()  # preload characters

MAGTAG.set_text("Bad-Dad-Joke Machine", 0, False)
MAGTAG.set_text("battery: ---%", 1, False)

loops = 0
count = 0
light_count = 0
sleep_level = 0  # TODO use level 1 if wake-from-button works
default_jokes = ["We only tell these to our kids to help them learn...really!"]

while True:
    time.sleep(1)

    # button A - next joke
    if MAGTAG.peripherals.button_a_pressed:
        MAGTAG.set_text(f"next...", 3)
        loops = -1

    # button B - default joke
    if MAGTAG.peripherals.button_b_pressed:
        MAGTAG.set_text(default_jokes[0], 2, False)
        MAGTAG.set_text(f"", 3)

    # button D - night light
    if MAGTAG.peripherals.button_d_pressed:
        if light_count == 0:
            light_count = 30
        else:
            light_count = 0

    # keep light on for 30 seconds
    if light_count > 0:
        MAGTAG.peripherals.neopixel_disable = False
        MAGTAG.peripherals.neopixels.fill((255, 255, 255))
    else:
        MAGTAG.peripherals.neopixel_disable = True
        MAGTAG.peripherals.neopixels.fill((0, 0, 0))

    if (loops % 60) == 0:
        try:
            batt = MAGTAG.peripherals.battery
            print(batt)
            batt = min(batt, 4.2)
            batt = 100 * batt / 4.2
            if batt < 10.0:
                sleep_level = 2
            MAGTAG.set_text(f"battery: {batt:.0f}%", 1, False)
        except:
            pass

    if loops == 0:
        jokes = default_jokes
        try:
            from backup_jokes import backup_jokes

            jokes = backup_jokes
        except ImportError:
            print("Default backup_jokes.py not found on CIRCUITPY")
            pass
        joke = jokes[random.randint(0, len(jokes) - 1)]
        MAGTAG.set_text(joke, 2, False)
        MAGTAG.set_text(f"", 3)

    if loops > 0 and (loops % 60) == 0:
        try:
            print("trying: ", DATA_SOURCE)
            MAGTAG.network.connect()
            RESPONSE = MAGTAG.network.requests.get(
                DATA_SOURCE, headers={"accept": "application/json"}
            )
            VALUE = RESPONSE.json()
            print(VALUE["joke"])
            MAGTAG.set_text(VALUE["joke"], 2, False)
            count = count + 1
            if sleep_level != 2:
                MAGTAG.set_text(f"online: {count}", 3)

        except Exception as e:
            print("Some error occured, retrying! -", e)
            joke = jokes[random.randint(0, len(jokes) - 1)]
            MAGTAG.set_text(joke, 2, False)
            MAGTAG.set_text(f"", 3)

        # put the board to sleep
        if sleep_level == 1:
            print("Light sleep 1 minute")
            MAGTAG.set_text(f"online: {count}", 3)
            PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60)
            MAGTAG.peripherals.neopixel_disable = True
            alarm.light_sleep_until_alarms(PAUSE)
            MAGTAG.peripherals.neopixel_disable = False
            loops = 0
            # TODO: complains that board.BUTTON_A in use
            # BUTTONA = alarm.touch.TouchAlarm(pin=board.BUTTON_A)
            # BUTTOND = alarm.touch.TouchAlarm(pin=board.BUTTON_D)
            # alarm.light_sleep_until_alarms(PAUSE, BUTTONA, BUTTOND)
        if sleep_level == 2:
            print("Deep sleep 1 minute")
            MAGTAG.set_text(f"sleep: 1min", 3)
            PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60)
            MAGTAG.peripherals.neopixel_disable = True
            alarm.exit_and_deep_sleep_until_alarms(PAUSE)

    loops = loops + 1
