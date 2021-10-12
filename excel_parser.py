import openpyxl

from week import *


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

    return "Day not found"
