import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import warnings
attendanceSheetPath=""
import windnd
import ExcelParse
import ConfigParse as config

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

if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    tk = ttk.Window(themename="superhero",title="工具",size=[1000,500])
    ttk.Button(command=showdialog,bootstyle="success",text="添加病事年假").pack(anchor=ttk.N,pady=5,side=LEFT)
    ttk.Button(command=showcalc,bootstyle="success",text="打开计算器").pack(anchor=ttk.N,pady=5,side=RIGHT)
    time=ttk.DateEntry(tk)
    time.pack();
    right_frame = ttk.Frame(tk,bootstyle="info",height=50,width=50)
    right_frame.pack()
    left_frame = ttk.Frame(tk,bootstyle="info",height=50,width=50)
    left_frame.pack()
    if sys.platform == 'win32':
        windnd.hook_dropfiles(left_frame,func=ExcelParse.ParseAttendanceSheet)
        windnd.hook_dropfiles(right_frame,func=printname)
    tk.mainloop()
