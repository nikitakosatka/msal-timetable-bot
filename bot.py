import telebot
import logging

from key import token

logging.basicConfig(level=logging.DEBUG)
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    logging.debug("Welcome")
    bot.send_message(message.chat.id, "Hello, World!")


@bot.message_handler(content_types=['text'])
def send_timetable(message):
    # TODO: ...
    pass
