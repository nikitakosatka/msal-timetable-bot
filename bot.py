import telebot
import logging
from datetime import date, timedelta

from key import token
from excel_parser import *

# logging.basicConfig(level=logging.DEBUG)
bot = telebot.TeleBot(token)

weeks = get_weeks()


@bot.message_handler(commands=["start", "help"])
def send_help(message):
    text = "Привет! Это бот с расписанием МГЮА\n" \
           "Команды:\n" \
           "\"Сегодня\" - расписание на сегодняшний день\n" \
           "\"Завтра\" - расписание на завтра\n" \
           "\"MM.DD\" - раписание на указанную дату, например \"12.10\"\n" \
           "\"День недели\" - расписание на указанный день недели (в текущей неделе), например " \
           "\"Вторник\"\n"
    bot.send_message(message.chat.id, text)


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
