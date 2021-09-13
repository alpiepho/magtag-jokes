#!/usr/bin/python3
import json
import requests
import time

# Use this utility to create a new backup_quotes files.  backup_quotes.py will be imported
# into dad_jokes.py and used to 'seed' the quote to be displayed while the quote site 
# is check.  It also serves as a backuop incase the network connection fails


#DEBUG
# from backup_quotes import backup_quotes
# # print(backup_quotes)
# for i, quote in enumerate(backup_quotes):
#   print(quote)
# print("===============================")

MAXLEN = 150

NUM = 100
backup_quotes = []

i = 0
while i < NUM:
  try:
    response = requests.get("https://zenquotes.io/api/random")
    temp = response.json()[0]['q'] + " - " + response.json()[0]['a']
    print(temp)
    if "Too many requests" in temp:
      time.sleep(10)
      raise Exception("Too many requests") 
    if len(temp) > MAXLEN:
        raise Exception("Too long") 
    backup_quotes.append(temp)
    i = i + 1
  except Exception as e:
    print(e)

  # Requests are restricted to 5 per 30 second period
  print("sleep 5s")
  time.sleep(5)

with open('backup_quotes.py', 'w') as writer:
  writer.write("backup_quotes = " + json.dumps(backup_quotes, indent=2))


# TODO test idea:  replace ? ... with \r\n