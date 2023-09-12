import datetime
from typing import List
from persondata import *

# 所有记录列表
AllDataList = List[PersonData]
# 没有上班时间列表
NoOnWorkTimeList = List[PersonData]
# 没有下班记录列表
NoOffWorkTimeList = List[PersonData]
# 迟到记录列表
LateList = List[PersonData]
# 早退记录列表
LeaveEarlyList = List[PersonData]
# 被跳过的记录列表
SkipedList = List[PersonData]

# 需要包含的日期
ContainInfoDate = []
# 需要跳过的日期
SkipInfoDate = []

#特殊的上班时间
SpecialOnworkTime = []
#特殊的下班时间
SpecialOffWorkTime = []

NameKey = "A"
JoinKey = "D"
OnWorkKey = "E"
OffWorkKey = "F"
BeginNumber = 3

PersonalLeaveList = []
SickLeaveList = []
YearLeaveList = []

ErrorList=[]