import os
import time
import win32gui
import win32api
import win32con
import sys
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
    "D:\\simulator\\PureObject\\simulator_landlord_GB_android",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_ios",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_ios_EN",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_ios_JP",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_ios_KR",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_android_ONESTORE",
]
merge_commands = [
    "git.exe pull --progress --no-edit --no-rebase \"origin\" sim2_oversea_master",
    "git.exe pull --progress --no-edit --no-rebase \"origin\" sim2_oversea_master",
    "git.exe pull --progress --no-edit --no-rebase \"origin\" sim2_oversea_mater_ios",
    "git.exe pull --progress --no-edit --no-rebase \"origin\" sim2_oversea_mater_ios",
    "git.exe pull --progress --no-edit --no-rebase \"origin\" sim2_oversea_mater_ios",
    "git.exe pull --progress --no-edit --no-rebase \"origin\" sim2_oversea_master_android"
]
# push_commands = [
#     "TortoiseGitProc.exe /command:push /closeonend:2",
#     "TortoiseGitProc.exe /command:push /closeonend:2",
#     "TortoiseGitProc.exe /command:push /closeonend:2",
#     "TortoiseGitProc.exe /command:push /closeonend:2",
#     "TortoiseGitProc.exe /command:push /closeonend:2",
#     "TortoiseGitProc.exe /command:push /closeonend:2"
# ]

push_commands = [
    "git.exe push -v --progress -- \"origin\" sim2_oversea_master_android:sim2_oversea_master_android",
    "git.exe push -v --progress -- \"origin\" sim2_oversea_mater_ios:sim2_oversea_mater_ios",
    "git.exe push -v --progress -- \"origin\" sim_oversea_mater_ios_en:sim_oversea_mater_ios_en",
    "git.exe push -v --progress -- \"origin\" sim2_oversea_master_ios_jp:sim2_oversea_master_ios_jp",
    "git.exe push -v --progress -- \"origin\" sim2_oversea_master_ios_kr:sim2_oversea_master_ios_kr",
    "git.exe push -v --progress -- \"origin\" sim2_oversea_master_android_onestore:sim2_oversea_master_android_onestore",
]
logpath = "D:\\simulator\\PureObject\\gitdiff.log"
def self_pull():
    os.remove(logpath)
    for path in paths:
        os.chdir(path)

        print(f"{bcolors.OKBLUE}path: {os.getcwd()}{bcolors.ENDC}")
        self_commands = "git.exe pull --progress --no-rebase \"origin\""
        os.system(self_commands)
        with open(logpath, 'a') as file:
            file.write(f"{path}:\n")
        self_commands = f"git.exe log --oneline -5 >> {logpath}"
        os.system(self_commands)
        self_commands = f"git.exe diff HEAD >> {logpath}"
        os.system(self_commands)
        with open(logpath, 'a') as file:
            file.write(f"\n========================================================================\n")


def merge_pull():
    for index, path in enumerate(paths):
        try:
            os.chdir(path)
            print("path: ", os.getcwd())
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
        hbutton = win32gui.FindWindowEx(wh, 0, 'Button', 'Ok')
        print(f"{bcolors.HEADER}{win32gui.GetWindowText(wh)}{bcolors.ENDC}")
        if hbutton != 0:
            win32api.PostMessage(hbutton, win32con.WM_LBUTTONDOWN, 0, 0)
            win32api.PostMessage(hbutton, win32con.WM_LBUTTONUP, 0, 0)


if __name__ == "__main__":
    self_pull()
    merge_pull()
