
import board
import analogio
# import json
import time
import random
import alarm
import terminalio
from adafruit_magtag.magtag import MagTag

sleep_level = 2
message_type = "JOKE"
# message_type = "QUOTE"
# message_type = "STOIC1"
# message_type = "BRUCE"

# https://en.wikiquote.org/wiki/Bruce_Lee
# #mw-content-text > div.mw-parser-output > ul > li

MAXLEN = 150

MAGTAG = MagTag(status_neopixel=None)
MAGTAG.peripherals.neopixel_disable = False

adc = analogio.AnalogIn(board.A1)

def get_online_joke(count):
    try:
        DATA_SOURCE = "https://icanhazdadjoke.com/"
        print("trying: ", DATA_SOURCE)
        MAGTAG.network.connect()
        RESPONSE = MAGTAG.network.requests.get(
            DATA_SOURCE, headers={"accept": "application/json"}
        )
        VALUE = RESPONSE.json()
        temp = VALUE["joke"]
        print(temp)
        if len(temp) > MAXLEN:
            raise Exception("Too long") 
        MAGTAG.set_text(temp, 2, False)
        count = count + 1
        if sleep_level != 2:
            MAGTAG.set_text(f"online: {count}", 3)

    except Exception as e:
        print("Some error occured, retrying! -", e)
        message = messages[random.randint(0, len(messages) - 1)]
        MAGTAG.set_text(message, 2, False)
        MAGTAG.set_text(f"", 3)
    return count

def get_online_quote(count):
    try:
        DATA_SOURCE = "https://zenquotes.io/api/random"
        print("trying: ", DATA_SOURCE)
        MAGTAG.network.connect()
        RESPONSE = MAGTAG.network.requests.get(
            DATA_SOURCE
        )
        VALUE = RESPONSE.json()
        temp = VALUE[0]['q'] + " - " + VALUE[0]['a']
        print(temp)
        if "Too many requests" in temp:
            raise Exception("Too many requests") 
        if len(temp) > MAXLEN:
            raise Exception("Too long") 
        MAGTAG.set_text(temp, 2, False)
        count = count + 1
        if sleep_level != 2:
            MAGTAG.set_text(f"online: {count}", 3)

    except Exception as e:
        print("Some error occured, retrying! -", e)
        message = messages[random.randint(0, len(messages) - 1)]
        MAGTAG.set_text(message, 2, False)
        MAGTAG.set_text(f"", 3)
    return count


def get_online_stoic1(count):
    try:
        DATA_SOURCE = "https://stoicquotesapi.com/v1/api/quotes/random"
        print("trying: ", DATA_SOURCE)
        MAGTAG.network.connect()
        RESPONSE = MAGTAG.network.requests.get(
            DATA_SOURCE
        )
        VALUE = RESPONSE.json()
        # {"id":42,"body":"If a man knows not to which port he sails, no wind is favorable.","author_id":2,"author":"Seneca"}
        temp = VALUE['body'] + " - " + VALUE['author']
        print(temp)
        # if "Too many requests" in temp:
        #     raise Exception("Too many requests") 
        if len(temp) > MAXLEN:
            raise Exception("Too long") 
        MAGTAG.set_text(temp, 2, False)
        count = count + 1
        if sleep_level != 2:
            MAGTAG.set_text(f"online: {count}", 3)

    except Exception as e:
        print("Some error occured, retrying! -", e)
        message = messages[random.randint(0, len(messages) - 1)]
        MAGTAG.set_text(message, 2, False)
        MAGTAG.set_text(f"", 3)
    return count

    return count

def get_online_bruce(count):
    # all quotes in backup
    message = messages[random.randint(0, len(messages) - 1)]
    MAGTAG.set_text(message, 2, False)
    MAGTAG.set_text(f"", 3)
    return count


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

# message
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

default_messages = ["Your message here."]
backup_messages = []
messages = []
message = ""


# HACK check potentiometer
# if moving in first 5 seconds, skip deep sleep
# use range to determine message_type
value1 = adc.value
print(value1)
for i in range(5):
    time.sleep(1.0)
    value2 = adc.value
    print(value2)
    if abs(value2 - value1) > 500:
        sleep_level = 1
        break
print(f'sleep_level: {sleep_level}')

# range 5000 - 52000
if value1 < 5000:
    message_type = "JOKE"
elif value1 < 20000:
    message_type = "QUOTE"
elif value1 < 40000:
    message_type = "STOIC1"
else:
    message_type = "BRUCE"
print(f'message_type: {message_type}')





# initialize based on message type
if message_type == "JOKE":
    MAGTAG.set_text("Bad-Dad-Joke Machine", 0, False)
    messages = ["We only tell these to our kids to help them learn...really!"]
    try:
        from backup_jokes import backup_jokes
        messages = backup_jokes
    except ImportError:
        print("Default backup_jokes.py not found on CIRCUITPY") 
if message_type == "QUOTE":
    MAGTAG.set_text("Quote Machine", 0, False)
    messages = ["Quotes..."]
    try:
        from backup_quotes import backup_quotes
        messages = backup_quotes
    except ImportError:
        print("Default backup_quotes.py not found on CIRCUITPY")
if message_type == "STOIC1":
    MAGTAG.set_text("Clasical Stoic Quotes", 0, False)
    messages = ["Clasical Stoic Quotes..."]
    try:
        from backup_stoics1 import backup_stoics1
        messages = backup_stoics1
    except ImportError:
        print("Default backup_stoics1.py not found on CIRCUITPY")
if message_type == "BRUCE":
    MAGTAG.set_text("Bruce Lee Wisdom", 0, False)
    messages = ["Bruce was the man!"]
    try:
        from backup_bruce import backup_bruce
        messages = backup_bruce
    except ImportError:
        print("Default backup_bruce.py not found on CIRCUITPY")

MAGTAG.set_text("battery: ---%", 1, False)

loops = 0
count = 0
light_count = 0

while True:
    if loops == 0:
        message = messages[random.randint(0, len(messages) - 1)]
        print(message)
        MAGTAG.set_text(message, 2, False)
        MAGTAG.set_text(f".", 3)

    time.sleep(1)

    # button A - next message
    if MAGTAG.peripherals.button_a_pressed:
        loops = -1

    # button B - default joke
    if MAGTAG.peripherals.button_b_pressed:
        MAGTAG.set_text(default_messages[0], 2, False)
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
            batt = batt - 3.3
            batt = max(0.0, batt)
            batt = 100 * batt / (4.2 - 3.3)
            if batt < 10.0:
                sleep_level = 2
            MAGTAG.set_text(f"battery: {batt:.0f}%", 1, False)
        except:
            pass

    # by not doing this in the first minute, the user
    # has a chance to use button and change sleep_level to 0
    if (loops % 60) == 0:
        if message_type == "JOKE":
            count = get_online_joke(count)
        if message_type == "QUOTE":
            count = get_online_quote(count)
        if message_type == "STOIC1":
            count = get_online_stoic1(count)
        if message_type == "BRUCE":
            count = get_online_bruce(count)

        # put the board to sleep
        if sleep_level == 2:
            print("Deep sleep 1 hour")
            MAGTAG.set_text(f"sleep: 1hr", 3)
            PAUSE = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60 * 60)
            MAGTAG.peripherals.neopixel_disable = True
            alarm.exit_and_deep_sleep_until_alarms(PAUSE)

    loops = loops + 1
