#!/usr/bin/python3
import json
import requests

# Use this utility to create a new backup_jokes files.  backup_jokes.py will be imported
# into dad_joes.py and used to 'seed' the joke to be displayed while the joke site 
# is check.  It also serves as a backuop incase the network connection fails


#DEBUG
# from backup_jokes import backup_jokes
# # print(backup_jokes)
# for i, joke in enumerate(backup_jokes):
#   print(joke)
# print("===============================")

NUM = 100
backup_jokes = []

for i in range(NUM):
  try:
    response = requests.get("https://icanhazdadjoke.com/", headers={'Accept' : 'application/json'})
    backup_jokes.append(response.json()['joke'])
    #DEBUG
    # print(response.json()['joke'])
  except:
    pass


with open('backup_jokes.py', 'w') as writer:
  writer.write("backup_jokes = " + json.dumps(backup_jokes, indent=2))


# TODO test idea:  replace ? ... with \r\n