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
    keyboard = get_keyboard()

    text = "Привет! Это бот с расписанием МГЮА\n" \
           "Команды:\n" \
           "\"Сегодня\" - расписание на сегодняшний день\n" \
           "\"Завтра\" - расписание на завтра\n" \
           "\"Неделя\" - расписание на всю текущую неделю" \
           "\"MM.DD\" - раписание на указанную дату, например \"12.10\"\n" \
           "\"День недели\" - расписание на указанный день недели (в текущей неделе), например " \
           "\"Вторник\"\n"

    bot.send_message(message.chat.id, text, reply_markup=keyboard)


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
                return get_beautiful_timetable(
                    get_day_by_weekday(weeks, today.strftime("%d.%m"), day.lower()))

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


def get_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    weekdays_keys = [telebot.types.KeyboardButton(text=day.capitalize()) for day in week_names]

    for key in range(0, len(weekdays_keys), 3):
        keyboard.add(weekdays_keys[key], weekdays_keys[key + 1], weekdays_keys[key + 2])

    week_key = telebot.types.KeyboardButton(text="Неделя")
    keyboard.add(week_key)

    return keyboard
