import openpyxl

from week import *

nums = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]


def get_weeks(file="Raspisanie.xlsx"):
    wb = openpyxl.load_workbook(filename=file)
    sheet = wb['Лист1']

    weeks = [Week([Day() for _ in range(6)]) for _ in range(6)]

    week_names = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]

    column = "AB"

    string_num = -1
    for week in weeks:
        if column == "DE":
            pass
        elif not weeks[2].is_empty() and weeks[3].is_empty():
            string_num = -1
            column = "DE"
        else:
            column = "AB"
        string_num += 3
        for day in week.get_days():
            while True:
                if str(sheet[f"{column[0]}{string_num}"].value).split()[
                    0] in week_names and day.get_date() == "":
                    day.set_date(sheet[f"{column[0]}{string_num}"].value.split()[1])
                    string_num += 1
                    continue
                elif len(str(sheet[f"{column[0]}{string_num}"].value).split("-")) == 2:
                    lesson = Lesson(' '.join(sheet[f"{column[1]}{string_num}"].value.split()[:-2]),
                                    sheet[f"{column[0]}{string_num}"].value,
                                    ' '.join(sheet[f"{column[1]}{string_num}"].value.split()[-2:]))
                    day.add_lesson(lesson)
                    string_num += 1
                elif day.get_date() != "":
                    break

    weeks[1], weeks[2], weeks[3], weeks[4] = weeks[3], weeks[1], weeks[4], weeks[2]

    return weeks


def get_day_by_date(weeks, date):
    for week in weeks:
        for day in week.get_days():
            if day.get_date() == date:
                return day

    return "День не найден"


def get_beautiful_timetable(day):
    text = ""
    if day == "День не найден":
        return day
    text += '📅' + day.get_date() + '\n\n'
    for lesson in range(day.get_lessons_count()):
        text += nums[lesson] + ' ' + day.get_lessons()[lesson].name + '\n'
        text += '🚪 ' + day.get_lessons()[lesson].get_classroom() + '\n'
        text += '🕒 ' + day.get_lessons()[lesson].get_time() + '\n\n'

    return text
