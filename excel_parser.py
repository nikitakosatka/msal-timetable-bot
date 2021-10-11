import openpyxl

from week import *

wb = openpyxl.load_workbook(filename='Raspisanie.xlsx')
sheet = wb['Лист1']

week = Week()
monday = Day()
for i in range(3, 5):
    lesson = Lesson(' '.join(sheet[f"B{i}"].value.split()[:-2]),
                    sheet[f"A{i}"].value,
                    ' '.join(sheet[f"B{i}"].value.split()[-2:]))
    monday.add_lesson(lesson)

print(monday)