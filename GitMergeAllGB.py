import os
import time
import win32gui
import win32api
import win32con
import sys
# import  msvcrt
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
    "D:\\simulator\\PureObject\\simulator_landlord_GB",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_android",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_ios",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_ios_EN",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_ios_JP",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_ios_KR",
    "D:\\simulator\\PureObject\\simulator_landlord_GB_android_ONESTORE",
    "D:\\simulator\\PureObject\\gn\\simulator_landlord",
    "D:\\simulator\\PureObject\\gn\\simulator_landlord_android",
    "D:\\simulator\\PureObject\\gn\\simulator_landlord_android_parent",
    "D:\\simulator\\PureObject\\gn\\simulator_landlord_android_taptap",
    "D:\\simulator\\PureObject\\gn\\simulator_landlord_android_xiaomi",
    "D:\\simulator\\PureObject\\gn\\simulator_landlord_ios",
    "D:\\simulator\\simulator_landlord",
    "D:\\simulator\\simulator_landlord_android_TAPTAP",
    "D:\\simulator\\simulator_landlord_GB",
    "D:\\simulator\\simulator_landlord_GB_android",
    "D:\\simulator\\simulator_landlord_GB_ios",
]
def self_pull():
    for path in paths:
        os.chdir(path)
        print(f"{bcolors.OKBLUE}path: {os.getcwd()}{bcolors.ENDC}")
        self_commands = "git.exe pull -v --prune --no-rebase \"origin\""
        os.system(self_commands)

if __name__ == "__main__":
    self_pull()
