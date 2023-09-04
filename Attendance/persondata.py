import datetime
import time

class PersonData:
    def __init__(self,name,JoinTime,OnTime,OffTime):
        self.Name = name
        self.JoinDateTime = StrToTime_Day(JoinTime)
        self.OnWorkTime = StrToTime_Hour(OnTime)
        self.OffWorkTime = StrToTime_Hour(OffTime)
    Name=''
    JoinDateTime=time.time()
    OnWorkTime=time.time()
    OffWorkTime=time.time()
    def print(self):
        print(f"{self.Name} : {type(self.Name)};{self.JoinDateTime} : {type(self.JoinDateTime)};{self.OnWorkTime} : {type(self.OnWorkTime)};{self.OffWorkTime} : {type(self.OffWorkTime)}")
def StrToTime_Day(strtime):
    if "-" not in strtime:
        return datetime.datetime.strptime(strtime,'%Y%m%d')
    else:
        return "-"
def StrToTime_Hour(strtime):
    if "-" not in strtime:
        return datetime.datetime.strptime(strtime,'%H:%M')
    else:
        return "-"

def IsNormalDayBeLate(person:PersonData):
    return CompareHours_IsBeLate(StrToTime_Hour("10:00"), person)

def IsNormalDayLeaveEarly(person:PersonData):
    return CompareHours_LeaveEarly(StrToTime_Hour("18:30"),person)
def CompareHours_IsBeLate(LimitTime:datetime,persondate:PersonData):
   return( persondate.OnWorkTime > LimitTime)

def CompareHours_LeaveEarly(LimitTime:datetime,persondate:PersonData):
    return( persondate.OffWorkTime < LimitTime)
