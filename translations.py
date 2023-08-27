# -*- coding: utf-8 -*-

# Import ENV
from env import LANG as set

# Languages

## Tuple of languages
languages = ('ENG', 'RU')

# English translation (Default)
ENG = {
        "botpy": {"today": "Today", "tomorrow": "Tomorrow"},
        "messagespy": {
            "empty": "There's no schedule that day",
            "notexist": "Day number {} does not exist in your diary",
            "deny": "Access denied",
            "welcome": "Welcome, {}\n\nTo view the schedule use the menu below or send the day's number\n\n(Monday is 1, Tuesday is 2, etc.)"
            },
        "createpy": {
            "add": "Add schedule for {} (y/n): ",
            "inval": "Invalid input",
            "number": "Enter the number of lessons for {}: ",
            "lesson": "Enter lesson number {}: ",
            "days": {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday" }
            }
        }

# Set bot language
for i in languages:
    if i == set:
        LANG = i
    else:
        LANG = ENG
