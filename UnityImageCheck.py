from Myconfig import *
from PIL import Image
import os

def CheckImageSize(filepath):
    try:
        global ImageCount
        ImageCount += 1
        img = Image.open(filepath)
        if os.stat(filepath).st_size > 89478485:
            raise Exception("Max Size");
        if img.width % 4 != 0 or img.height % 4 !=0:
            print( f"{bcolors.WARNING}{filepath}{bcolors.ENDC}'s size not multiple of 4 | {bcolors.FAIL}Width: {img.width % 4}, Height: {img.height % 4} Size: {os.stat(filepath).st_size/1024}KB{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.FAIL}Can not open file {filepath}{bcolors.ENDC}")

def LoopAllImage(Floderpath):
    for root,ds,fs,in os.walk(Floderpath):
        for f in fs:
            yield os.path.join(root,f)
def test(path):
    for i in LoopAllImage(path):
        if "png" in i and "meta" not in i :
            CheckImageSize(i)
if __name__ == '__main__':
    ImageCount = 0
    test("C:\\fangdong\simulator_landlord_GB\simulator_landlord\Game\Assets")
    print(ImageCount)
    # CheckImageSize('E:\WorkLog\\20230731\\xiugai\\dt3_cj2_sl_4_1_4.png')
