#!/usr/bin/python3
import json
import requests
import time
from bs4 import BeautifulSoup

# Use this utility to create a new backup_bruce files.  backup_bruce.py will be imported
# into dad_jokes.py and used to 'seed' the quote to be displayed while the quote site 
# is check.  It also serves as a backuop incase the network connection fails


#DEBUG
# from backup_bruce import backup_bruce
# # print(backup_bruce)
# for i, quote in enumerate(backup_bruce):
#   print(quote)
# print("===============================")

MAXLEN = 150

NUM = 100
backup_bruce = []


try:
  response = requests.get("https://en.wikiquote.org/wiki/Bruce_Lee")
  # print(response.text)
  soup = BeautifulSoup(response.text, "html.parser")
  lines = soup.select('#mw-content-text > div.mw-parser-output > ul > li')
  for i, line in enumerate(lines):
    if i <= 100:
      text = line.text
      text = text.split('p.')[0]
      text = text.split('P.')[0]
      text = text.strip()
      backup_bruce.append(text)
      print(str(i) + ": " + text)
      print(len(text))

  print(len(backup_bruce))

except Exception as e:
  print(e)


with open('backup_bruce.py', 'w') as writer:
  writer.write("backup_bruce = " + json.dumps(backup_bruce, indent=2))

