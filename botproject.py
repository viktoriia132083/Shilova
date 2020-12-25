from typing import Tuple

import schedule
import telebot
from telebot import types
import schedule
import time

# 1482915007:AAFbKsXGDRJF2-BkfUcT6T09dq8lF3Rs0iE

bot = telebot.TeleBot("1482915007:AAFbKsXGDRJF2-BkfUcT6T09dq8lF3Rs0iE")

hangout = []


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 'Привет! Я - твой бот. Я помогу тебе установить уведомления, которые будут приходить каждый час:)')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to('Приветики-пистолетики!')
    elif message.text == 'Как дела?':
        bot.reply_to('Отлично, какое напоминание тебе установить?')
        if message.text == '':
            hangout.append(message)
            bot.reply_to(message, 'Напоминание установлено')

@bot.message_handler(func=lambda message: True)
def job(message):
    bot.send_message(hangout)


schedule.every(1).hour.do(job)


bot.polling()
