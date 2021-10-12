import telebot
import logging
from datetime import date, timedelta

from key import token
from excel_parser import *

# logging.basicConfig(level=logging.DEBUG)
bot = telebot.TeleBot(token)

weeks = get_weeks()


@bot.message_handler(content_types=['text'])
def send_timetable(message):
    today = date.today()
    day = message.text
    if message.text.lower() == "сегодня":
        day = date.today().strftime("%d.%m")
    elif message.text.lower() == 'завтра':
        day = (today + timedelta(days=1)).strftime("%d.%m")
    timetable = get_day_by_date(weeks, day)
    bot.send_message(message.chat.id, get_beautiful_timetable(timetable))
