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
    text = message.text
    if text.lower() == "неделя":
        timetable = get_week_timetable()
    else:
        timetable = get_day_timetable(text)

    bot.send_message(message.chat.id, timetable)


def get_day_timetable(text):
    today = date.today()
    day = text

    match day.lower():
        case "сегодня":
            day = today.strftime("%d.%m")

        case "завтра":
            day = (today + timedelta(days=1)).strftime("%d.%m")

        case day if day.lower() in week_names:
            try:
                return get_day_by_weekday(weeks, today.strftime("%d.%m"), day.lower())

            except Exception:
                return day

    return get_beautiful_timetable(get_day_by_date(weeks, day))


def get_week_timetable():
    today = date.today().strftime("%d.%m")
    week = get_week_by_day(weeks, today)
    text = str(week)

    try:
        text = '\n\n'.join([get_beautiful_timetable(day) for day in week.get_days()])
    except Exception:
        pass

    return text
