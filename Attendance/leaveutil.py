import datetime
import Data as globaldata


def comparetime_min(t1: datetime, t2: datetime):
    if t1.time.hour == t2.time.hour and t1.time.minute == t2.time.minute and comparetime_day(t1, t2):
        return True
    return False


def comparetime_day(t1: datetime, t2: datetime):
    if t1.date.year == t2.date.year and t1.date.month == t2.date.month and t2.date.day == t1.date.day:
        return True
    return False

def subtime(t1,t2):
    return datetime.datetime.combine(datetime.datetime.today(), t1) - datetime.datetime.combine(
        datetime.datetime.today(), t2)


def getretaketime(_person):
    jointime = _person.JoinDateTime
    onwork = _person.OnWorkTime
    offwork = _person.OffWorkTime

    standardonworktime = datetime.time(hour=10, minute=0, second=0)
    standardoffworktime = datetime.time(hour=18, minute=30, second=0)
    for _time in globaldata.SpecialOnworkTime:
        if comparetime_day(jointime, _time):
            standardonworktime = datetime.time(hour=_time.time.hour, minute=_time.time.minute, second=_time.time.second)
            break
    for _time in globaldata.SpecialOffWorkTime:
        if comparetime_day(jointime, _time):
            standardoffworktime = datetime.time(hour=_time.time.hour, minute=_time.time.minute,
                                                second=_time.time.second)
            break
    onworkdelta = subtime(standardonworktime,onwork)
    offworkdelta = subtime(offwork,standardoffworktime)
    return onworkdelta + offworkdelta
def converdeltatimetodatetime(delta):
    return  datetime.datetime.strptime(str(delta), "%H:%M:%S")

def converttimetofloat(_time:datetime.timedelta):
    strtime = str(_time).split(':')
    hour=int(strtime[0])
    minu = int(strtime[1])
    return hour+minu*0.1
def NormalDateFilter():
    for person in globaldata.AllDataList:
        today = person.JoinDateTime.weekday()
        if today < 5:
            globaldata.HolidayList.append(person)
