# -*- coding: utf-8 -*-

# Modules
import datetime
import pickle
from env import users
from create import dict_dir, file

# Load diary
with open(f"{dict_dir}/{file}", "rb") as save:
    diary = pickle.load(save)

# Functions

##Authorize
def auth(id):
    if str(id) in users:
        return True

def welcome(tid, user):
    if auth(tid):
        return f"Welcome, {user}\n\nTo view the schedule use the menu below or send the day's number\n\n(Monday is 1, Tuesday is 2, etc.)"
    else:
        return 'Access denied'

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
        return "there's no schedule that day."
    else:
        output = ""
        for i in diary[id]:
            output = output + i + '\n'
        return output

## Select message
def output(action):
    if isinstance(action,(int)):
        if action > 7:
            return f'Day number {action} does not exist in your diary'
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
        return 'Access denied'
