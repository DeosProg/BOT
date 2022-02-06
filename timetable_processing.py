import timetable1
import timetable2
from datetime import datetime, timedelta


def get_timetable():
    pass


def get_timetable_today():
    d = datetime.today().isoweekday()
    if get_week_num() == 1:
        if d == 1:
            return timetable1.mo
        elif d == 2:
            return timetable1.tu
        elif d == 3:
            return timetable1.we
        elif d == 4:
            return timetable1.th
        elif d == 5:
            return timetable1.fr
        elif d == 6:
            return timetable1.sa
        elif d == 7:
            return timetable2.su

    elif get_week_num() == 2:
        if d == 1:
            return timetable2.mo
        elif d == 2:
            return timetable2.tu
        elif d == 3:
            return timetable2.we
        elif d == 4:
            return timetable2.th
        elif d == 5:
            return timetable2.fr
        elif d == 6:
            return timetable2.sa
        elif d == 7:
            return timetable2.su


def get_timetable_tomorrow():
    d = datetime.today().isoweekday()
    #d = 1
    if get_week_num() == 1:
        if d == 1:
            return timetable1.tu
        elif d == 2:
            return timetable1.we
        elif d == 3:
            return timetable1.th
        elif d == 4:
            return timetable1.fr
        elif d == 5:
            return timetable1.sa
        elif d == 6:
            return timetable2.su
        elif d == 7:
            return timetable2.mo

    elif get_week_num() == 2:
        if d == 1:
            return timetable2.tu
        elif d == 2:
            return timetable2.we
        elif d == 3:
            return timetable2.th
        elif d == 4:
            return timetable2.fr
        elif d == 5:
            return timetable2.sa
        elif d == 6:
            return timetable2.su
        elif d == 7:
            return timetable1.mo


def get_week_num():
    now = datetime.now()
    sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)

    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())

    parity = ((d2 - d1).days // 7) % 2
    return itn(2) if parity else (1)


