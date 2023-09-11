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

    def __eq__(self, other):
        return self.Name == other.Name and self.JoinDateTime == other.JoinDateTime and self.OnWorkTime == other.OnWorkTime and self.OffWorkTime == other.OffWorkTime

    def bPersonDataWithNameAndData(self,_name:str,Data:datetime):
        if self.Name == _name and Data.time.weekday() == self.JoinDateTime.weekday():#todo 细化时间的比较 新建一个工具py
            return True
        return False

    def print(self):
        print(
            f"{self.Name} : {type(self.Name)};{self.JoinDateTime} : {type(self.JoinDateTime)};{self.OnWorkTime} : {type(self.OnWorkTime)};{self.OffWorkTime} : {type(self.OffWorkTime)}")
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

    def print(self):
        print(
            f"{self.Name} : {type(self.Name)};{self.LeaveTime} : {type(self.LeaveTime)};{self.CompleteTime} : {type(self.CompleteTime)};{self.LeaveHours} : {type(self.LeaveHours)}")


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

    def print(self):
        print(
            f"{self.Name} : {type(self.Name)};{self.LeaveTime} : {type(self.LeaveTime)};{self.CompleteTime} : {type(self.CompleteTime)};{self.LeaveHours} : {type(self.LeaveHours)}")


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

    def print(self):
        print(
            f"{self.Name} : {type(self.Name)};{self.LeaveTime} : {type(self.LeaveTime)};{self.CompleteTime} : {type(self.CompleteTime)};{self.LeaveHours} : {type(self.LeaveHours)}")


def StrToTime_Day(strtime):
    if "-" not in strtime:
        return datetime.datetime.strptime(strtime, '%Y%m%d')
    else:
        return "-"


def StrToTime_Hour(strtime):
    if "-" not in strtime:
        return datetime.datetime.strptime(strtime, '%H:%M')
    else:
        return "-"


def IsNormalDayBeLate(person: PersonData):
    return CompareHours_IsBeLate(StrToTime_Hour("10:00"), person)


def IsNormalDayLeaveEarly(person: PersonData):
    return CompareHours_LeaveEarly(StrToTime_Hour("18:30"), person)


def CompareHours_IsBeLate(LimitTime: datetime, persondate: PersonData):
    return persondate.OnWorkTime > LimitTime


def CompareHours_LeaveEarly(LimitTime: datetime, persondate: PersonData):
    return persondate.OffWorkTime < LimitTime
