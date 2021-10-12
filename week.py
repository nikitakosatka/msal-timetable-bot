class Lesson:
    def __init__(self, name, time, classroom):
        self.name = name
        self.time = time
        self.classroom = classroom

    def __str__(self):
        return f"Name:{self.name}\nTime:{self.time}\nClassroom:{self.classroom}\n"

    def get_name(self):
        return self.name

    def get_classroom(self):
        return self.classroom

    def get_time(self):
        return self.time


class Day:
    def __init__(self, date="", lessons=None):
        if lessons is None:
            lessons = []
        self.date = date
        self.lessons = lessons

    def __str__(self):
        return '\n'.join([self.date] + list(map(str, self.lessons)))

    def is_empty(self):
        return not self.lessons

    def get_date(self):
        return self.date

    def get_lessons(self):
        return self.lessons

    def get_lessons_count(self):
        return len(self.lessons)

    def set_lessons(self, lessons):
        self.lessons = lessons

    def add_lesson(self, lesson, num=None):
        if num is None:
            self.lessons.append(lesson)
        else:
            self.lessons.insert(num - 1, lesson)

    def set_date(self, date):
        self.date = date


class Week:
    def __init__(self, days=None):
        if days is None:
            days = []
        self.days = days

    def is_empty(self):
        return not self.days or all(day.is_empty() for day in self.days)

    def get_days(self):
        return self.days

    def get_date(self):
        if self.days is not None:
            return self.days[0].get_date()

    def add_day(self, day, num=0):
        if num == 0:
            self.days.append(day)
        else:
            self.days.insert(num, day)
