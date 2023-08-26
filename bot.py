#!/usr/bin/python3

#Import
import telebot
import functions
from env import TOKEN

#Setup bot
diary_bot = telebot.TeleBot(TOKEN)

#Init buttons
@diary_bot.message_handler(commands=['start', 'help'])
def welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    today = telebot.types.KeyboardButton('Сегодня')
    next = telebot.types.KeyboardButton('Завтра')
    keyboard.add(today)
    keyboard.add(next)
    diary_bot.reply_to(message, functions.welcome(message.from_user.id, message.from_user.first_name), reply_markup=keyboard)

#Send functions
@diary_bot.message_handler(func=lambda message: message.text == 'Сегодня')
def today(message):
    diary_bot.send_message(message.chat.id, functions.exec(message.from_user.id, 'today'))

@diary_bot.message_handler(func=lambda message: message.text == 'Завтра')
def next(message):
    diary_bot.send_message(message.chat.id, functions.exec(message.from_user.id, 'next'))

@diary_bot.message_handler(func=lambda message: message.text.isdigit())
def week(message):
    id = int(message.text)
    diary_bot.send_message(message.chat.id, functions.exec(message.from_user.id, id))
    
#Start bot
diary_bot.polling()

