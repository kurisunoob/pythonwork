# import turtle              # 导入turtle库（模块）
# turtle.bgcolor("#ffffff")  # 设置背景颜色为
# turtle.speed(7)
# # turtle.speed(10)        # 可减慢画正方形和写字的速度
#
# ### ②画灰色阴影
# turtle.color("#404040")   # 同时设置画笔和填充颜色都为#404040，一种深灰色。
# a=100                     # 正方形内等腰直角三角形的直角边为a
# b=2**0.5*a                # 斜边为b ，等腰直角三角形的斜边=√2倍的直角边
#
# turtle.penup()
# turtle.goto(-210,180)             # 步骤1光束画完后，让海龟返回原点，即海龟移动至坐标(0,0)，并设置朝向为初始方向(向右)。
# turtle.forward(a)
# turtle.pendown()
#
# turtle.begin_fill()
# turtle.left(135)
# turtle.forward(b)
# turtle.left(90)
# turtle.forward(b)
# turtle.left(90)
# turtle.forward(b)
# turtle.left(90)
# turtle.forward(b)
# turtle.end_fill()
#
# ### ③ 画正方形红纸
# turtle.color("#ea182a")   # 同时设置画笔和填充颜色都为#ea182a，一种红色。
# a=100
# b=2**0.5*a
#
# turtle.penup()
# turtle.home()     # 第2步灰色阴影画完后，让海龟返回原点，即海龟移动至坐标(0,0)，并设置朝向为初始方向(向右)。
# turtle.goto(-205,180)
# turtle.forward(a)
# turtle.pendown()
#
# turtle.begin_fill()
# turtle.left(135)
# turtle.forward(b)
# turtle.left(90)
# turtle.forward(b)
# turtle.left(90)
# turtle.forward(b)
# turtle.left(90)
# turtle.forward(b)
# turtle.end_fill()
#
# ### ④ 写文字“福”
# turtle.color("black")
# turtle.penup()
# turtle.goto(-210,175)            # 让海龟返回原点
# turtle.setheading(-90)   # 让海龟头部朝下
# turtle.forward(50)      # 让海龟向下移动150个像素。这个数字需要不断调试。
# turtle.pendown()
# turtle.write("福", align="center",font=("黑体",90,"bold"))
#
# ### 海龟绘图结束，隐藏海龟
# turtle.hideturtle()
# turtle.done()
# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
#
# def open_new_window():
#     new_window = ttk.Window()
#     new_window.title("New Window")
#     new_window.geometry("400x300")
#
#     label = ttk.Label(new_window, text="Hello from the new window!", bootstyle=PRIMARY)
#     label.pack(pady=20)
#
#     new_window.mainloop()
#
# root = tk.Tk()
# root.title("Main Window")
# root.geometry("400x300")
#
# button = ttk.Button(root, text="Open New Window", command=open_new_window, bootstyle=SUCCESS)
# button.pack(pady=20)
#
# root.mainloop()
# import random
#
# ROCK, SCISSOR, PAPER = range(3)
#
# # 构建“赢”的基础规则：“我：对手”
# WIN_RULE = {
#     ROCK: SCISSOR,
#     SCISSOR: PAPER,
#     PAPER: ROCK,
# }
#
# def build_rules():
#     """构建完整的游戏规则"""
#     rules = {}
#     for k, v in WIN_RULE.items():
#         rules[(k, v)] = True
#         rules[(v, k)] = False
#     return rules
#
# def game_v2(rules):
#     """生成一局随机游戏，并打印游戏结果。"""
#     a = random.choice([ROCK, SCISSOR, PAPER])
#     b = random.choice([ROCK, SCISSOR, PAPER])
#     print(f"玩家 A：{a}，玩家 B：{b}")
#
#     if a == b:
#         print("平局")
#     elif rules[(a, b)]:
#         print("玩家 A 获胜")
#     else:
#         print("玩家 B 获胜")
#
# if __name__ == '__main__':
#     rules = build_rules()
#     for num in range(10):
#         print(f">>> Game #{num}")
#         game_v2(rules)
import re
def _f(r):
    t = r.group()
    if len(t) <= 2:
        return t
    return f'{t[0]}{len(t)-2}{t[-1]}'


def i18n(s: str) -> str:
    s = re.sub(r'\w+', _f, s)
    return s

print(i18n("sadoifja osidjfoia"))