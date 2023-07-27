import pyperclip
from Myconfig import *
import re
import ctypes

androidparent="(?<=p\()\S+(?=\))"
IOSparent="(?<=,@\")\S+(?=\"])"
IOSNumparent="(?<=@\")\S+(?=\",@)"
androidcount=32
def ConcatenateString(Android,IOS,IOSNumber):
     resultStr=f"{{\"AndroidKey\":\"{Android}\",\"IOSKey\":\"{IOS}\",\"IOSNumber\":\"{IOSNumber}\"}}"
     pyperclip.copy(resultStr)

def OnButtonClick():
    try :
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
        print(f"{androidresult} + lens: {len(androidresult)}")
        print(f"{IOSresult} + lens: {len(IOSresult)}")
        print(f"{IOSNumresult} + lens: {len(IOSNumresult)}")
        ConcatenateString(androidresult,IOSresult,IOSNumresult)
        if len(androidresult) != 32 or len(IOSresult) != 64 or len(IOSNumresult) != 9:
            raise Exception("格式错误")
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0,str(e),"错误",0)


if __name__ == '__main__':
    OnButtonClick();
