import os
import shutil
import time


def git_pull():
    path = "D:\\simulator\\PureObject\\gn\\simulator_landlord"
    os.chdir(path)
    self_commands = "git.exe pull --progress -v --no-rebase \"origin\""
    os.system(self_commands)


def copy():
    try:
        localtime = time.localtime(time.time())
        Strftime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        print("开始时间为 :", Strftime)
        shutil.rmtree(destination_dir, True)
        shutil.copytree(source_dir, destination_dir, dirs_exist_ok = True)
        print('Directory copied successfully.')
        localtime = time.localtime(time.time())
        Strftime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        print ("结束时间为 :", Strftime)
    except Exception as e:
        print('Directory not copied.')
        print(e)
if __name__ == '__main__':
    git_pull()
    source_dir = 'D:\\simulator\\PureObject\\gn\\simulator_landlord\\ExDataHome\\Excel\\Excel'
    destination_dir = 'D:\\SVN\\trunk\\game\\simulator_landlord\\ExDataHome\\Excel\\Excel'
    copy()
    source_dir = 'D:\\simulator\\PureObject\\gn\\simulator_landlord\\Game\\Assets'
    destination_dir = 'D:\\SVN\\trunk\\game\\simulator_landlord\\Game\\Assets'
    copy()
    source_dir = 'D:\\simulator\\PureObject\\gn\\simulator_landlord\\Game\\Packages'
    destination_dir = 'D:\\SVN\\trunk\\game\\simulator_landlord\\Game\\Packages'
    copy()
    source_dir = 'D:\\simulator\\PureObject\\gn\\simulator_landlord\\Game\\ProjectSettings'
    destination_dir = 'D:\\SVN\\trunk\\game\\simulator_landlord\\Game\\ProjectSettings'
    copy()
    path= "D:\\SVN\\trunk\\game\\simulator_landlord";
    self_commands = f"TortoiseProc.exe /command:commit /path:{path}"
    os.system(self_commands)
