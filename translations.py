# -*- coding: utf-8 -*-

# Import ENV
from env import LANG as set

# Languages

## List of languages
languages = ['ENG', 'RU']

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

# Russian translation
RU = {
        "botpy": {"today": "Сегодня", "tomorrow": "Завтра"},
        "messagespy": {
            "empty": "Сегодня нет занятий",
            "notexist": "День {} не найден в вашем дневнике",
            "deny": "Этот бот запривачен, гнида, блять",
            "welcome": "Добро пожаловать, {}\n\nЧтобы просмотреть ваше расписание, воспользуйтесь меню ниже или отправьте номер дня\n\n(Понедельник - 1, Вторник - 2, и т.д.)"
            },
        "createpy": {
            "add": "Добавить расписание на {} (y/n): ",
            "inval": "Неверный ввод",
            "number": "Введите число занятий на {}: ",
            "lesson": "Введите занятие номер {}: ",
            "days": {0: "Понедельник", 1: "Вторник", 2: "Среда", 3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье" }
            }
        }

# Set bot language
for i in languages:
    if i == set:
        LANG = locals()[i]
    else:
        LANG = ENG
