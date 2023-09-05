import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import warnings
attendanceSheetPath=""
import windnd
import ExcelParse
import ConfigParse as config
import Data as globaldata

def printname(fiel):
    print(fiel)

def showcalc():
    window = ttk.Toplevel(title="Time")
    print(config.Calculator(window))
    window.mainloop()
def showdialog():
    window = ttk.Toplevel(title="Time")
    print(config.LeaveDataDialog(window))
    window.mainloop()
x = 1
group1 = 1
def AddLeave():
    global x
    global  group1
    for personal in globaldata.PersonalLeaveList:
        ttk.Checkbutton(group1, text=f'{personal.Name}').pack(fill=X)
    x = x+1

if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    tk = ttk.Window(themename="superhero",title="工具",size=[1000,500])
    ttk.Button(command=showdialog,bootstyle="success",text="添加病事年假").pack(anchor=ttk.N,pady=5,side=LEFT)
    ttk.Button(command=showcalc,bootstyle="success",text="打开计算器").pack(anchor=ttk.N,pady=5,side=RIGHT)

    cf=config.CollapsingFrame(tk)
    group1=ttk.Frame(cf,padding=10)
    cf.add(child=group1,title="banner1")
    ttk.Button(command=AddLeave,bootstyle="success",text="刷新").pack(anchor=ttk.S,pady=5,side=TOP)

    cf.pack()
    right_frame = ttk.Frame(tk,bootstyle="info",height=50,width=50)
    right_frame.pack()
    left_frame = ttk.Frame(tk,bootstyle="info",height=50,width=50)
    left_frame.pack()
    if sys.platform == 'win32':
        windnd.hook_dropfiles(left_frame,func=ExcelParse.ParseAttendanceSheet)
        windnd.hook_dropfiles(right_frame,func=printname)
    tk.mainloop()
