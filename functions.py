#!/usr/bin/python3

# Modules
import datetime
from env import diary
from env import users

# Functions

##Authorize
def auth(id):
    if str(id) in users:
        return True

def welcome(tid, user):
    if auth(tid):
        return f"Welcome, {user}\n\nTo view the schedule use the menu below or send the day's number\n\n(Monday is 1, Tuesday is 2, etc.)"
    else:
        return 'Этот бот запривачен, гнида блять'

## Reurn current day id
def currentday():
    days = { 'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6 }
    date = datetime.datetime.now()
    day = date.strftime("%A")
    id = days.get(day)
    return id

## Return output message
def message(id):
    if id > 4:
        return "There's no schedule today"
    else:
        days = { 0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday' }
        output = str(days.get(id)) + ':\n'
        for i in diary[id]:
            output = output + i + '\n'
        return output

## Select message
def output(action):
    if isinstance(action,(int)):
        if action > 5:
            return f'Day number {action} does not exist'
        else:
            id = action - 1
            return message(id)
    if action == 'today':
        return message(currentday())
    if action == 'next':
        id = currentday()
        if id < 3:
            id = id + 1
        else:
            id = 0
        return message(id)

## Execution
def exec(tid,action):
    if auth(tid):
        return output(action)
    else:
        return 'Access denied'
