import os
import re
from tkinter import Tk

from openpyxl import load_workbook
import json
from tkinter import *
sheetmap = {}
configfile = []
configstr = []
UsingCount = 0
def LoadJson():
    xlsx = 'xlsx'
    str = 'str'
    f = open('LanguageConfig.json')
    config = json.load(f)
    f.close()
    print(config[xlsx])
    for i in config[xlsx]:
        configfile.append(i)
    for i in config[str]:
        configstr.append(i)
    global UsingCount
    UsingCount = config['count']
def LoadXlsl():
    Language_Path="C:\\fangdong\simulator_landlord_GB\simulator_landlord\ExDataHome\Excel\Excel";
    Lafile = []
    sheetlist = []
    os.chdir(Language_Path)
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
def _Searchs(name , _str):
    dirc = sheetmap[name]
    templist = []
    for temp in dirc.items():
        if re.search(str(_str),str(temp[0])):
            templist.append(temp)

    templist = sorted(templist,key=lambda x:len(x[1]),reverse=True)

    os.remove("retult.txt")
    f = open ("retult.txt","a+", encoding='utf-8')
    f.write(f"{name} [{_str}] \n")
    for tem in templist[:UsingCount]:
        f.write(f"{tem[0]} {tem[1]} {len(tem[1])} \n")
    f.close()

def Searchs():
    for filename in configfile:
        for strs in configstr:
            _Searchs(filename, strs)
if __name__ == '__main__':
    LoadJson()
    LoadXlsl()
    #Searchs()
    tempdic = {}
    root = Tk()
    root.title("te")
    root.config(bg="skyblue")
    left_frame = Frame(root)
    left_frame.grid(row=0,column=0,padx=10,pady=5)
    for roots, dirs, file in os.walk('.', topdown=False, followlinks=False):
        for fi in file:
            if "Language" in fi and "csv" not in fi and '~' not in fi:
                CheckVar = IntVar()
                Checkbutton(master=left_frame,text=fi,variable=CheckVar,onvalue=1,offvalue=0,height=1,width=50).pack()
                tempdic[fi] = CheckVar
    right_frame = Frame(root)
    right_frame.grid(row=1,column=0)
    Button(right_frame,text="ck").pack()
    root.mainloop()