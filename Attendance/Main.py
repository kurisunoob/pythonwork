import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import windnd
import ExcelParse
import UI as ui
import TimePickerUI as TimePicker
import Data as globaldata
import persondata
import leaveutil as util


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


# 查询事假超过天数的人
def __personalleavedatapross_overdays():
    temppersonlist = globaldata.PersonalLeaveList.copy()
    oklist = []
    notoklist = []
    for _data in temppersonlist:
        hourcount = 0;
        if _data.Name in oklist or _data.Name in notoklist:
            continue
        for __data in temppersonlist:
            if _data.Name == __data.Name:
                hourcount += _data
                if hourcount >= 4 * 24:
                    notoklist.append(_data.Name)
                    break
        oklist.append(_data.Name)
    messagestr = ''
    for _date in notoklist:
        messagestr = messagestr + f"{_date} 这个月超过了事假期限需要核查\n"
    ui.show_message(messagestr)


# 查询病假超过天数的人
def __sickleavedatapross_overdays():
    temppersonlist = globaldata.SickLeaveList.copy()
    oklist = []
    notoklist = []
    for _data in temppersonlist:
        hourcount = 0;
        if _data.Name in oklist or _data.Name in notoklist:
            continue
        for __data in temppersonlist:
            if _data.Name == __data.Name:
                hourcount += _data
                if hourcount >= 3 * 24:
                    notoklist.append(_data.Name)
                    break
        oklist.append(_data.Name)
    messagestr = ''
    for _date in notoklist:
        messagestr = messagestr + f"{_date} 这个月超过了病假假期限需要核查\n"
    ui.show_message(messagestr)


# 查询年假超过天数的人
def __yearleavedatapross_overdays():
    # 年假需要特殊处理
    pass


def __personalleavedatapross():
    __personalleavedatapross_overdays()
    leaveperson_data = 0;
    complete_data = 0;
    for leavedata in globaldata.PersonalLeaveList:
        name = leavedata.Name
        leavetime = leavedata.LeaveTime
        completetime = leavedata.CompleteTime
        hours = leavedata.LeaveHours
        for person in globaldata.AllDataList:
            if person.bPersonDataWithNameAndData(name, leavetime):
                leaveperson_data = person
            if person.bPersonDataWithNameAndData(name, completetime):
                complete_data = person
            if leaveperson_data != 0 and complete_data != 0:
                break
        if complete_data == 0 or leaveperson_data == 0:
            ui.show_message("数据出错")
        retaketime = util.getretaketime(complete_data)
        if util.converttimetofloat(retaketime) < hours:
            pass
        # globaldata.ErrorList = leavedata.print()
        else:
            globaldata.PersonalLeaveList.remove(leavedata)


def __sickleavedatapross():
    __sickleavedatapross_overdays()
    leaveperson_data = 0;
    complete_data = 0;
    for leavedata in globaldata.SickLeaveList:
        name = leavedata.Name
        leavetime = leavedata.LeaveTime
        completetime = leavedata.CompleteTime
        hours = leavedata.LeaveHours
        for person in globaldata.AllDataList:
            if person.bPersonDataWithNameAndData(name, leavetime):
                leaveperson_data = person
            if person.bPersonDataWithNameAndData(name, completetime):
                complete_data = person
            if leaveperson_data != 0 and complete_data != 0:
                break
        if complete_data == 0 or leaveperson_data == 0:
            ui.show_message("数据出错")
        retaketime = util.getretaketime(complete_data)
        if util.converttimetofloat(retaketime) < hours / 2:
            pass
        # globaldata.ErrorList = leavedata.print()
        else:
            globaldata.SickLeaveList.remove(leavedata)


# 年假需要特殊处理
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

def showdata():
    # window = ttk.Toplevel(title="数据")
    window = ttk.Toplevel(title="数据")
    print(ui.ShowData(window))
    window.mainloop()


def adddate():
    window = ttk.Toplevel(title="时间")
    print(TimePicker.AddDate(window))
    window.mainloop()


if __name__ == '__main__':
    DEBUG = 1
    globaldata.AllDataList.clear()
    globaldata.ResultList.clear()
    globaldata.ContainInfoDate.clear()
    # test
    if DEBUG == 1:
        ExcelParse.ParseAttendanceSheet('D:\\WorkLog\\20240201\\attendance.xlsx', DEBUG)
    # warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    tk = ttk.Window(themename="superhero", title="工具", size=[500, 500])
    # ttk.Button(command=showdialog, text="添加病事年假").pack(anchor=ttk.N, pady=5, side=LEFT)
    # ttk.Button(command=showcalc, text="打开计算器").pack(anchor=ttk.N, pady=5, side=RIGHT)
    # ttk.Button(command=showlist, text="刷新").pack(anchor=ttk.S, pady=5, side=TOP)
    # ttk.Button(command=datapross, text="数据处理").pack(anchor=ttk.S, pady=5, side=TOP)
    style = ttk.Style()
    style.configure("red.TFrame", background='red')
    style.configure("blue.TFrame", background='blue')
    left_frame = ttk.Frame(tk, height=50, width=50, style="blue.TFrame")
    left_frame.grid(column=0, row=0, padx=10, pady=10)
    if sys.platform == 'win32':
        windnd.hook_dropfiles(left_frame, func=ExcelParse.ParseAttendanceSheet)
    ttk.Button(command=showdata, text="显示数据").grid(column=1, row=0, padx=10, pady=10)
    ttk.Button(command=adddate, text="添加时间").grid(column=1, row=1, padx=10, pady=10)

    tk.mainloop()
