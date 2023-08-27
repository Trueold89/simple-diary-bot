# -*- coding: utf-8 -*-

# Modules
import datetime
import pickle
from env import USERS
from create import dict_dir, file
from translations import LANG as translate
lang = translate.get("messagespy")

# Load diary
with open(f"{dict_dir}/{file}", "rb") as save:
    diary = pickle.load(save)

# Functions

##Authorize
def auth(id):
    if str(id) in USERS:
        return True

def welcome(tid, user):
    if auth(tid):
        msg = lang.get('welcome')
        return msg.format(user)
    else:
        return lang.get('deny')

## Reurn current day id
def currentday():
    days = { 'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6 }
    date = datetime.datetime.now()
    day = date.strftime("%A")
    id = days.get(day)
    return id

## Return output message
def message(id):
    if not(id in diary):
        return lang.get('empty')
    else:
        output = ""
        for i in diary[id]:
            output = output + i + '\n'
        return output

## Select message
def output(action):
    if isinstance(action,(int)):
        if action > 7:
            msg = lang.get('notexist')
            return msg.format(action)
        else:
            id = action - 1
            return message(id)
    if action == 'today':
        return message(currentday())
    if action == 'next':
        id = currentday()
        while True:
            if not(id in diary):
                id = id + 1
                if id > 6:
                    id = 0
            else:
                break
        return message(id)

## Execution
def exec(tid,action):
    if auth(tid):
        return output(action)
    else:
        return lang.get('deny')
