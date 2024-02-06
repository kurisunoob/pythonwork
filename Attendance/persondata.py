import datetime
import time

class PersonData:
    def __init__(self, name, JoinTime, OnTime, OffTime):
        self.Name = name
        self.JoinDateTime = StrToTime_Day(JoinTime)
        self.OnWorkTime = StrToTime_Hour(OnTime)
        self.OffWorkTime = StrToTime_Hour(OffTime)

    Name = ''
    JoinDateTime = time.time()
    OnWorkTime = time.time()
    OffWorkTime = time.time()

    def __str__(self):
        return f"姓名 : {self.Name};加入日期 : {self.JoinDateTime};上班时间 : {self.OnWorkTime};下班时间 : {self.OffWorkTime}"
    def __eq__(self, other):
        return self.Name == other.Name and self.JoinDateTime == other.JoinDateTime and self.OnWorkTime == other.OnWorkTime and self.OffWorkTime == other.OffWorkTime

    def comparetime_day(t1: datetime, t2: datetime):
        if t1.date.year == t2.date.year and t1.date.month == t2.date.month and t2.date.day == t1.date.day:
            return True
        return False

    def bPersonDataWithNameAndData(self,_name:str,Data:datetime):
        if self.Name == _name and self.comparetime_day(self.JoinDateTime,Data):
            return True
        return False

    #todo 得到迟到时间
        #todo 处理特殊的上班时间
    #todo 得到早退时间
        #todo 处理特殊的下班时间


class PersonalLeaveData:
    def __init__(self,
                 name: str,
                 JoinTime: datetime,
                 completetime: datetime,
                 leavehours: int):
        self.Name = name
        self.LeaveTime = JoinTime
        self.CompleteTime = completetime
        self.LeaveHours = leavehours

    Name = ''
    LeaveTime = time.time()
    CompleteTime = time.time()
    LeaveHours = 1

    def __eq__(self, other):
        return (self.Name == other.Name and
                self.LeaveTime == other.LeaveTime and
                self.CompleteTime == other.LeaveTime and
                self.LeaveTime == other.LeaveTime)

    def __str__(self):
            f"{self.Name} : {type(self.Name)};{self.LeaveTime} : {type(self.LeaveTime)};{self.CompleteTime} : {type(self.CompleteTime)};{self.LeaveHours} : {type(self.LeaveHours)}"


class YearLeavaData:
    def __init__(self,
                 name: str,
                 JoinTime: datetime,
                 completetime: datetime,
                 leavehours: int):
        self.Name = name
        self.LeaveTime = JoinTime
        self.CompleteTime = completetime
        self.LeaveHours = leavehours

    Name = ''
    LeaveTime = time.time()
    CompleteTime = time.time()
    LeaveHours = 1

    def __eq__(self, other):
        return (self.Name == other.Name and
                self.LeaveTime == other.LeaveTime and
                self.CompleteTime == other.LeaveTime and
                self.LeaveTime == other.LeaveTime)

    def __str__(self):
            f"{self.Name} : {type(self.Name)};{self.LeaveTime} : {type(self.LeaveTime)};{self.CompleteTime} : {type(self.CompleteTime)};{self.LeaveHours} : {type(self.LeaveHours)}"


class SickLeavaData:
    def __init__(self,
                 name: str,
                 JoinTime: datetime,
                 completetime: datetime,
                 leavehours: int):
        self.Name = name
        self.LeaveTime = JoinTime
        self.CompleteTime = completetime
        self.LeaveHours = leavehours

    Name = ''
    LeaveTime = time.time()
    CompleteTime = time.time()
    LeaveHours = 1

    def __eq__(self, other):
        return (self.Name == other.Name and
                self.LeaveTime == other.LeaveTime and
                self.CompleteTime == other.LeaveTime and
                self.LeaveTime == other.LeaveTime)

    def __str__(self):
            f"{self.Name} : {type(self.Name)};{self.LeaveTime} : {type(self.LeaveTime)};{self.CompleteTime} : {type(self.CompleteTime)};{self.LeaveHours} : {type(self.LeaveHours)}"


def StrToTime_Day(strtime):
    try:
        if "-" not in strtime:
            return datetime.datetime.strptime(strtime, '%Y%m%d').date()
        else:
            return "-"
    except:
        return '-'


def StrToTime_Hour(strtime):
    try:
        if "-" not in strtime:
            return datetime.datetime.strptime(strtime, '%H:%M')
        else:
            return "-"
    except:
        return "-"


def IsNormalDayBeLate(person: PersonData):
    return CompareHours_IsBeLate(StrToTime_Hour("10:00"), person)


def IsNormalDayLeaveEarly(person: PersonData):
    return CompareHours_LeaveEarly(StrToTime_Hour("18:30"), person)


def CompareHours_IsBeLate(LimitTime: datetime, persondate: PersonData):
    return persondate.OnWorkTime > LimitTime


def CompareHours_LeaveEarly(LimitTime: datetime, persondate: PersonData):
    return persondate.OffWorkTime < LimitTime
