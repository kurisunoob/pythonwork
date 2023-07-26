from Myconfig import *
from tkinter import *
from tkinter import scrolledtext
import sys
import pyperclip
import re

androidparent="(?<=p\()\S+(?=\))"
IOSparent="(?<=,@\")\S+(?=\"])"
IOSNumparent="(?<=@\")\S+(?=\",@)"
androidcount=32
def ConcatenateString(Android,IOS,IOSNumber):
     resultStr=f"{{\"AndroidKey\":\"{Android}\",\"IOSKey\":\"{IOS}\",\"IOSNumber\":\"{IOSNumber}\"}}"
     pyperclip.copy(resultStr)

def OnButtonClick():
    allstr=pyperclip.paste()

    pattern = re.compile(androidparent)
    temp=pattern.search(allstr)
    androidresult=temp.group()

    pattern = re.compile(IOSparent)
    temp=pattern.search(allstr)
    IOSresult = temp.group()

    pattern = re.compile(IOSNumparent)
    temp=pattern.search(allstr)
    IOSNumresult = temp.group()
    print(androidresult)
    print(IOSresult)
    print(IOSNumresult)

    ConcatenateString(androidresult,IOSresult,IOSNumresult)

if __name__ == '__main__':
    # root = Tk()
    # root.title("te")
    # root.config(bg="skyblue")
    # down_frame = Frame(root)
    # down_frame.grid(row=0, column=0)
    # Button(down_frame, text="解析", command=lambda:OnButtonClick()).pack()
    # root.mainloop()
    OnButtonClick();
