import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import warnings
import windnd
import ExcelParse
import UI as ui
import Data as globaldata
import persondata

# globa data
LeaveListGroup: ttk.Frame
SickLeaveGroup: ttk.Frame
YearLeaveGroup: ttk.Frame

attendanceSheetPath = ""


def printname(fiel):
    print(fiel)

def datapross():
    __personalleavedatapross()
    __sickleavedatapross()
    __yearleavedatapross()
    pass
def __personalleavedatapross():
    for leavedata in globaldata.PersonalLeaveList:
        name = leavedata.Name
        leavetime = leavedata.LeaveTime
        completetime = leavedata.CompleteTime
        hours = leavedata.LeaveHours


    pass
def __sickleavedatapross():
    pass
def __yearleavedatapross():
    pass
def showlist():
    global LeaveListGroup
    global SickLeaveGroup
    global YearLeaveGroup
    window = ttk.Toplevel(title="Time")
    cf = ui.CollapsingFrame(window)
    LeaveListGroup = ttk.Frame(cf, padding=10)
    SickLeaveGroup = ttk.Frame(cf, padding=10)
    YearLeaveGroup = ttk.Frame(cf, padding=10)
    refreshleavelist()
    refreshsicklist()
    refreshyearlist()
    cf.add(child=LeaveListGroup, title="事假名单:")
    cf.add(child=SickLeaveGroup, title="病假名单:")
    cf.add(child=YearLeaveGroup, title="年假名单:")
    cf.pack()
    window.mainloop()


def showcalc():
    window = ttk.Toplevel(title="Time")
    print(ui.Calculator(window))
    window.mainloop()


def showdialog():
    window = ttk.Toplevel(title="Time")
    print(ui.LeaveDataDialog(window))
    window.mainloop()


def RemovePersonalLeaveData(data: persondata.PersonalLeaveData):
    for _data in globaldata.PersonalLeaveList:
        if _data == data:
            globaldata.PersonalLeaveList.remove(_data)
    refreshleavelist()


def refreshleavelist():
    global LeaveListGroup
    for item in LeaveListGroup.winfo_children():
        item.destroy()
    for personal in globaldata.PersonalLeaveList:
        button = ttk.Button(LeaveListGroup,
                            name=f'{personal.Name}|{personal.LeaveHours}|{personal.LeaveTime.strftime("%Y:%m:%d")}|{personal.CompleteTime.strftime("%Y:%m:%d")}',
                            text=f'姓名:{personal.Name},请假时间:{personal.LeaveHours},请假时间:{personal.LeaveTime.strftime("%Y:%m:%d")},完成时间:{personal.CompleteTime.strftime("%Y:%m:%d")}')
        button.configure(command=lambda b=personal: RemovePersonalLeaveData(b))
        button.pack(fill=X)


def RemoveSickLeaveData(data: persondata.SickLeavaData):
    for _data in globaldata.SickLeaveList:
        if _data == data:
            globaldata.SickLeaveList.remove(_data)
    refreshsicklist()


def refreshsicklist():
    global SickLeaveGroup
    for item in SickLeaveGroup.winfo_children():
        item.destroy()
    for personal in globaldata.SickLeaveList:
        button = ttk.Button(SickLeaveGroup,
                            text=f'姓名:{personal.Name},请假时间:{personal.LeaveHours},请假时间:{personal.LeaveTime.strftime("%Y:%m:%d")},完成时间:{personal.CompleteTime.strftime("%Y:%m:%d")}')
        button.configure(command=lambda b=personal: RemoveSickLeaveData(b))
        button.pack(fill=X)


def RemoveYearLeaveData(data: persondata.YearLeavaData):
    for _data in globaldata.YearLeaveList:
        if _data == data:
            globaldata.YearLeaveList.remove(_data)
    refreshyearlist()


def refreshyearlist():
    global YearLeaveGroup
    for item in YearLeaveGroup.winfo_children():
        item.destroy()
    for personal in globaldata.YearLeaveList:
        button = ttk.Button(YearLeaveGroup,
                            text=f'姓名:{personal.Name},请假时间:{personal.LeaveHours},请假时间:{personal.LeaveTime.strftime("%Y:%m:%d")},完成时间:{personal.CompleteTime.strftime("%Y:%m:%d")}')
        button.configure(command=lambda b=personal: RemoveYearLeaveData(b))
        button.pack(fill=X)


if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    tk = ttk.Window(themename="superhero", title="工具", size=[1000, 500])
    ttk.Button(command=showdialog, text="添加病事年假").pack(anchor=ttk.N, pady=5, side=LEFT)
    ttk.Button(command=showcalc, text="打开计算器").pack(anchor=ttk.N, pady=5, side=RIGHT)
    ttk.Button(command=showlist, text="刷新").pack(anchor=ttk.S, pady=5, side=TOP)
    ttk.Button(command=datapross, text="数据处理").pack(anchor=ttk.S, pady=5, side=TOP)

    right_frame = ttk.Frame(tk, height=50, width=50)
    right_frame.pack()
    left_frame = ttk.Frame(tk, height=50, width=50)
    left_frame.pack()
    if sys.platform == 'win32':
        windnd.hook_dropfiles(left_frame, func=ExcelParse.ParseAttendanceSheet)
        windnd.hook_dropfiles(right_frame, func=printname)
    tk.mainloop()
