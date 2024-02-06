import datetime
from typing import List
from persondata import *

# 所有记录列表
AllDataList = [PersonData]
# 没有上班时间列表
NoOnWorkTimeList = [PersonData]
# 没有下班记录列表
NoOffWorkTimeList = [PersonData]
# 迟到记录列表
LateList = [PersonData]
# 早退记录列表
LeaveEarlyList = [PersonData]
# 被跳过的记录列表
SkipedList = [PersonData]

# 需要包含的日期
ContainInfoDate = [datetime]
# 需要跳过的日期
SkipInfoDate = [datetime]

#特殊的上班时间
SpecialOnworkTime = [datetime]
#特殊的下班时间
SpecialOffWorkTime = [datetime]

NameKey = "A"
DateKey = 'B'
OnWorkKey = "C"
OffWorkKey = "D"
BeginNumber = 3

PersonalLeaveList = []
SickLeaveList = []
YearLeaveList = []

ErrorList=[]
ResultList = [PersonData]
