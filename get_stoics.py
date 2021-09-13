#!/usr/bin/python3
from code1 import MAXLEN
import json
import requests
import time

# Use this utility to create a new backup_stoics files.  backup_stoics.py will be imported
# into dad_jokes.py and used to 'seed' the quote to be displayed while the quote site 
# is check.  It also serves as a backuop incase the network connection fails


#DEBUG
# from backup_stoics import backup_stoics
# # print(backup_stoics)
# for i, quote in enumerate(backup_stoics):
#   print(quote)
# print("===============================")

MAXLEN = 150

NUM = 100
backup_stoics = []

i = 0
while i < NUM:
  try:
    response = requests.get("https://stoicquotesapi.com/v1/api/quotes/random")
    temp = response.json()['body'] + " - " + ['author']
    print(temp)
    # if "Too many requests" in temp:
    #     raise Exception("Too many requests") 
    if len(temp) > MAXLEN:
        raise Exception("Too long") 
    backup_stoics.append(temp)
    i = i + 1
  except Exception as e:
    print(e)

  # # Requests are restricted to 5 per 30 second period
  # print("sleep 5s")
  # time.sleep(5)

with open('backup_stoics.py', 'w') as writer:
  writer.write("backup_stoics = " + json.dumps(backup_stoics, indent=2))


# TODO test idea:  replace ? ... with \r\n