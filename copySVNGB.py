import shutil
import os
import time


def copy():
    try :
        localtime = time.localtime(time.time())
        Strftime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        print("开始时间为 :", Strftime)
        shutil.copytree(source_dir, destination_dir,dirs_exist_ok = True)
        print('Directory copied successfully.')
        localtime = time.localtime(time.time())
        Strftime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        print ("结束时间为 :", Strftime)
    except Exception as e:
        print('Directory not copied.')
        print(e)

source_dir = 'C:\\fangdong\simulator_landlord_GB\simulator_landlord\ExDataHome\Excel\Excel'
destination_dir = 'E:\\fd\simulator_svn\game\simulator_landlord_GB\ExDataHome\Excel\Excel'
copy()
source_dir = 'C:\\fangdong\simulator_landlord_GB\simulator_landlord\Game\Assets'
destination_dir = 'E:\\fd\simulator_svn\game\simulator_landlord_GB\Game\Assets'
copy()