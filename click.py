from tkinter import *
import os
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

    root = Tk()
    root.title("测试框")
    root.config(bg="skyblue")

    left_frame = Frame(root, width = 400, height=400)
    left_frame.grid(row = 3,column = 0,padx=10,pady=5)
    root.mainloop()
