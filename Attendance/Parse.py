import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import warnings
import windnd
import ExcelParse
import UI as ui
import Data as globaldata

# globa data
group1: ttk.Frame

attendanceSheetPath = ""


def printname(fiel):
    print(fiel)


def showlist():
    global group1
    window = ttk.Toplevel(title="Time")
    cf = ui.CollapsingFrame(window)
    group1 = ttk.Frame(cf, padding=10)
    refreshleavelist()
    cf.add(child=group1, title="banner1")
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


def refreshleavelist():
    global group1
    for item in group1.winfo_children():
        item.destroy()
    for personal in globaldata.PersonalLeaveList:
        ttk.Button(group1, text=f'{personal.Name}',
                   command=(lambda: globaldata.PersonalLeaveList.remove(personal))).pack(fill=X)


if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    tk = ttk.Window(themename="superhero", title="工具", size=[1000, 500])
    ttk.Button(command=showdialog, text="添加病事年假").pack(anchor=ttk.N, pady=5, side=LEFT)
    ttk.Button(command=showcalc, text="打开计算器").pack(anchor=ttk.N, pady=5, side=RIGHT)
    ttk.Button(command=showlist, text="刷新").pack(anchor=ttk.S, pady=5, side=TOP)

    right_frame = ttk.Frame(tk, height=50, width=50)
    right_frame.pack()
    left_frame = ttk.Frame(tk, height=50, width=50)
    left_frame.pack()
    if sys.platform == 'win32':
        windnd.hook_dropfiles(left_frame, func=ExcelParse.ParseAttendanceSheet)
        windnd.hook_dropfiles(right_frame, func=printname)
    tk.mainloop()
