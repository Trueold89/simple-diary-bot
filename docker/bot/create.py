# -*- coding: utf-8 -*-

# Modules
import pickle
import os
from translations import LANG as translate
lang = translate.get("createpy")

# Vars
dict_dir = "/etc/dbot"
file = "diary.pkl"
# days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday" }
days = lang.get('days')

# Functions

##Check
def check():
    ###Check for save file
    if os.path.exists(f"{dict_dir}/{file}"):
        return True
    else:
        ### Call create function
        return create()

##Ask
def ask(day):
    msg = lang.get('add')
    ans = input(msg.format(day))
    if ans == 'y':
        return True
    elif ans == 'n': 
        return False
    else:
        print(lang.get('inval'))
        ask(day)

def lescount(nday):
    msg = lang.get('number')
    count = input(msg.format(nday))
    if count.isdigit():
        if int(count) > 0:
            return True, int(count)
        else:
            return False
    else:
        return False

##Add lessons to day
def add(day):
    nday = days.get(day) 
    if ask(nday) == True:
        list = []
        list.append(f"{nday}:")
        count = ()
        count = lescount(nday)
        if count:
            for lessonid in range(count[1]):
                lessonid = lessonid + 1
                msg = lang.get('lesson')
                les = f"{lessonid}. " + input(msg.format(lessonid))
                list.append(les)
            return list
        else:
            print(lang.get('inval'))
            add(day)
    else:
        return False

##Create
def create():
    diary = {}
    if os.path.exists(f"{dict_dir}") == False:
        os.makedirs(dict_dir)
    for day in days.keys():
        sched = (add(day))
        if sched == False:
            continue
        else:
            diary.setdefault(day,sched)
    with open(f"{dict_dir}/{file}","wb") as save:
        pickle.dump(diary, save)
        return True

check()
