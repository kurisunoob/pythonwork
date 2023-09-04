from Myconfig import *
from openpyxl import load_workbook
from tkinter import *
from persondata import *
import windnd
import ctypes
import warnings
attendanceSheetPath=""
AllDataList=[]
NoOnWorkTimeList=[]
NoOffWorkTimeList=[]
LateList=[]
LeaveEarlyList=[]

#需要包含的日期
ContainInfoDate=[]
#需要跳过的日期
SkipInfoDate=[]

NameKey = "A"
JoinKey = "D"
OnWorkKey = "E"
OffWorkKey = "F"
BeginNumber = 3
# 跳过或者添加特定日期
def SkipDate(JoinDateTime:datetime):
    for date in ContainInfoDate:
       if date == JoinDateTime:
           return True
    for date in SkipInfoDate:
        if date == SkipInfoDate:
            return False

    if JoinDateTime.weekday() == 6 or JoinDateTime.weekday() == 7:
        return True
    return False


def ParseAttendanceSheet(path):
    path = str(path)[3:-2].replace("\\\\","\\").replace("\\\\","\\")
    print(f"{bcolors.OKCYAN}{type(path)}考勤表路径为:{path}{bcolors.ENDC}")
    if "xlsx" not in path:
        ctypes.windll.user32.MessageBoxW(0, "请拖入Excel表格", "错误", 0)
    temp = load_workbook(path).active
    if temp is None:
        ctypes.windll.user32.MessageBoxW(0, "表格数据有问题 请检查", "错误", 0)
    for index in range(BeginNumber,temp.max_row):
        NowIndex = str(index)
        name = temp[NameKey + NowIndex]
        join = temp[JoinKey + NowIndex]
        onwork = temp[OnWorkKey + NowIndex]
        offwork = temp[OffWorkKey + NowIndex]
        person=PersonData(name.value,join.value,onwork.value,offwork.value)
        person.print()

        if SkipDate(person.JoinDateTime):
           continue;

        AllDataList.append(person)
        if  type(person.OnWorkTime) is str:
            NoOnWorkTimeList.append(person)
        elif IsNormalDayBeLate(person):
            LateList.append(person)
        if type(person.OffWorkTime) is str:
            NoOffWorkTimeList.append(person)
        elif(IsNormalDayLeaveEarly(person)):
            LeaveEarlyList.append(person)

def printname(fiel):
    print(fiel)

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
tk = Tk()
right_frame = Frame(tk,bg="Blue",height=50,width=50)
right_frame.grid(row=0, column=1,padx=20,pady=20)

left_frame = Frame(tk,bg="Red",height=50,width=50)
left_frame.grid(row=0, column=0,padx=20,pady=20)
windnd.hook_dropfiles(left_frame,func=ParseAttendanceSheet)
windnd.hook_dropfiles(right_frame,func=printname)
tk.mainloop()