#conding=utf8
import os
import pygit2
g = os.walk("D:\\simulator")
for path,dir_list,file_list in g:
    for dir_name in dir_list:
        if '.git' == dir_name:
            print(os.path.join(path, dir_name))
