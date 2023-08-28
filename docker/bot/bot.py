#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Import
import telebot
import messages
import env
from translations import LANG as translate
lang = translate.get("botpy")

#Setup bot
TOKEN = env.env('TOKEN')
diary_bot = telebot.TeleBot(TOKEN)

#Init buttons
@diary_bot.message_handler(commands=['start', 'help'])
def welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    today = telebot.types.KeyboardButton(lang.get('today'))
    next = telebot.types.KeyboardButton(lang.get('tomorrow'))
    keyboard.add(today)
    keyboard.add(next)
    diary_bot.reply_to(message, messages.welcome(message.from_user.id, message.from_user.first_name), reply_markup=keyboard)

#Send functions
@diary_bot.message_handler(func=lambda message: message.text == lang.get('today'))
def today(message):
    diary_bot.send_message(message.chat.id, messages.exec(message.from_user.id, 'today'))

@diary_bot.message_handler(func=lambda message: message.text == lang.get('tomorrow'))
def next(message):
    diary_bot.send_message(message.chat.id, messages.exec(message.from_user.id, 'next'))

@diary_bot.message_handler(func=lambda message: message.text.isdigit())
def week(message):
    id = int(message.text)
    diary_bot.send_message(message.chat.id, messages.exec(message.from_user.id, id))
    
#Start bot
diary_bot.polling()
