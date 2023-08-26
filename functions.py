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
        return f'Добро пожаловать, {user}\n\nЧтобы просмотреть расписание воспользуйтесь меню ниже или отправьте номер дня\n\n(понедельник - 1, вторник -2, и т.д)'
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
        return 'Сегодня нет занятий'
    else:
        days = { 0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница' }
        output = str(days.get(id)) + ':\n'
        for i in diary[id]:
            output = output + i + '\n'
        return output

## Select message
def output(action):
    if isinstance(action,(int)):
        if action > 5:
            return f'Дня недели под номером {action} не существует'
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
        return 'Этот бот запривачен, гнида блять'
