import os
import time
import win32gui
import win32api
import win32con
import sys
#import  msvcrt
import threading

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

paths = [
    "E:\\fd\simulator2_landlord_android\\android_ads\simulator_landlord",
    "E:\\fd\simulator2_landlord_ios\simulator_landlord_ios\simulator_landlord",
    "E:\\fd\simulator2_landlord_android\\android_ads_taptap\simulator_landlord",
    "E:\\fd\simulator2_landlord_android\\android_ads_parent\simulator_landlord",
    "E:\\fd\simulator2_landlord_android\\android_ads_xiaomi",
]
merge_commands = [
    "git.exe pull --progress -v --no-rebase \"origin\" sim2_master",
    "git.exe pull --progress -v --no-rebase \"origin\" sim2_master",
    "git.exe pull --progress -v --no-rebase \"origin\" sim2_android_ads",
    "git.exe pull --progress -v --no-rebase \"origin\" sim2_android_ads",
    "git.exe pull --progress -v --no-rebase \"origin\" sim2_android_ads"
]
push_commands = [
        "TortoiseGitProc.exe /command:push /closeonend:2",
        "TortoiseGitProc.exe /command:push /closeonend:2",
        "TortoiseGitProc.exe /command:push /closeonend:2",
        "TortoiseGitProc.exe /command:push /closeonend:2",
        "TortoiseGitProc.exe /command:push /closeonend:2"
]

def self_pull():
    for path in paths:
        os.chdir(path)

        print(f"{bcolors.OKBLUE}path: {os.getcwd()}{bcolors.ENDC}")
        self_commands = "git.exe pull --progress -v --no-rebase \"origin\""
        os.system(self_commands)
def merge_pull():
    for index, path in enumerate(paths):
        try:
            os.chdir(path)
            print("path: ",os.getcwd())
            command = merge_commands[index]
            result = 0;
            result = os.system(command)
            print(f"{bcolors.HEADER} 合并结果: {result}{bcolors.ENDC}")
            if result != 0:
                raise Exception("合并出现冲突请解决!")
            command = push_commands[index]
            threading.Thread(target=Click, args=()).start()
            os.system(command)
        except Exception as e:
            print(f"{bcolors.HEADER}{e}{bcolors.ENDC}")
            os.system("TortoiseGitProc.exe /command:resolve")
            sys.exit()

# 筛选需要的窗口句柄
def get_mesh_windows(hWndList, name):
    winhwnd = []
    for hWnd in hWndList:
        title = win32gui.GetWindowText(hWnd)
        clsname = win32gui.GetClassName(hWnd)

        if name in title:
            winhwnd.append(hWnd)
    return winhwnd
def Click():
    time.sleep(1)
    print(f"{bcolors.OKBLUE}path: Click(){bcolors.ENDC}")
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    name = ' - TortoiseGit'
    winhwnds = get_mesh_windows(hWndList, name)
    hWndcList = []
    for wh in winhwnds:
        hbutton = win32gui.FindWindowEx(wh, 0, 'Button', '确定')
        print(f"{bcolors.HEADER}{win32gui.GetWindowText(wh)}{bcolors.ENDC}")
        if hbutton != 0:
            win32api.PostMessage(hbutton, win32con.WM_LBUTTONDOWN, 0, 0)
            win32api.PostMessage(hbutton, win32con.WM_LBUTTONUP, 0, 0)


if __name__ == "__main__":
    self_pull()
    merge_pull()
    #test()