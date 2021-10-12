import telebot
import logging
from datetime import date

from key import token
from excel_parser import get_weeks, get_day_by_date

# logging.basicConfig(level=logging.DEBUG)
bot = telebot.TeleBot(token)

weeks = get_weeks()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    logging.debug("Welcome")
    bot.send_message(message.chat.id, "Hello, World!")


@bot.message_handler(content_types=['text'])
def send_timetable(message):
    today = date.today().strftime("%d.%m")
    timetable = get_day_by_date(weeks, today)
    bot.send_message(message.chat.id, timetable)
