import os
import re
from time import strftime, localtime
from Myconfig import *
from openpyxl import load_workbook
from tkinter import *
sheetmap = {}
configfile = []
configstr = []
UsingCount = 0
fileFD = []
resultfilename ="result_ui"
def SetPath():
    Language_Path = "C:\\fangdong\simulator_landlord_GB\simulator_landlord\ExDataHome\Excel\Excel";
    os.chdir(Language_Path)


def LoadXlsl():
    Lafile = []
    sheetlist = []
    for root,dirs,file in os.walk('.',topdown=False,followlinks=False):
        for fi in file:
            if "Language" in fi and "csv" not in fi and '~' not in fi:
                for name in  configfile:
                    if name in fi:
                        Lafile.append(fi)

    for name in Lafile:
       temp = load_workbook(name).active
       sheetlist.append(temp)
       tempdic = {}
       usedvale = temp['B6:'+'B'+str(temp.max_row)]
       Values = []
       for vale in usedvale:
           for v in vale:
               Values.append(v.value)
       usedvale = temp['A6:' + 'A' + str(temp.max_row)]
       Keys = []
       for vale in usedvale:
           for v in vale:
               Keys.append(v.value)

       for index in range(len(Keys)):
           _key = Keys[index]
           _value = Values[index]
           tempdic[_key] = _value
       sheetmap[temp.title] = tempdic
def GetConfig():
    configfile.clear()
    configstr.clear()
    for strs in strtext.get().split(','):
        configstr.append(strs)
    global UsingCount
    UsingCount = str(strcount.get())
    for strs in CheckVarDic.items():
        if strs[1].get() == 1:
            configfile.append(strs[0].split(".")[0])
    LoadXlsl()

def Searchs():
    print(f"{bcolors.OKBLUE}Work path: {nowpath}{bcolors.ENDC}")
    if os.path.exists(resultfilename):
        os.remove(resultfilename)
    fileFD = open(resultfilename,"a+", encoding='utf-8')
    for filename in configfile:
        for strs in configstr:
            _Searchs(filename, strs,fileFD)
    fileFD.close()
    self_commands = f"EmEditor.exe {resultfilename}"
    os.system(self_commands)
def _Searchs(name , _str,_fileFD):
    dirc = sheetmap[name]
    templist = []
    for temp in dirc.items():
        if re.search(str(_str),str(temp[0])):
            templist.append(temp)

    templist = sorted(templist,key=lambda x:len(x[1]),reverse=True)

    _fileFD.write(f"{name} [{_str}] \n")
    for tem in templist[:int(UsingCount)]:
        _fileFD.write(f"{tem[0]} {tem[1]} {len(tem[1])} \n")
def ButtonClick():
    GetConfig()
    Searchs()
if __name__ == '__main__':
    nowpath = os.getcwd()
    resultfilename = f"{nowpath}\\{resultfilename}{strftime('%Y_%m_%d_%H_%M_%S',localtime())}.txt"
    SetPath()
    CheckVarDic = {}
    root = Tk()
    root.title("te")
    root.config(bg="skyblue")
    #======================================
    left_frame = Frame(root)
    left_frame.grid(row=0,column=0,padx=10,pady=5)
    for roots, dirs, file in os.walk('.', topdown=False, followlinks=False):
        for fi in file:
            if "Language" in fi and "csv" not in fi and '~' not in fi:
                CheckVar = IntVar()
                Checkbutton(master=left_frame,text=fi,variable=CheckVar,onvalue=1,offvalue=0,height=1,width=50).pack()
                CheckVarDic[fi] = CheckVar
    #======================================
    right_frame = Frame(root)
    right_frame.grid(row=0,column=1)
    Label(right_frame,text="匹配文本:").grid(row=0)
    Label(right_frame,text="展示数量:").grid(row=1)

    strtext = Entry(right_frame)
    strtext.grid(row=0, column=1)
    strcount = Entry(right_frame)
    strcount.grid(row=1, column=1)


    #====================================
    down_frame = Frame(root)
    down_frame.grid(row=1,column=0)
    Button(down_frame, text="查询", command=ButtonClick).pack()
    root.mainloop()
