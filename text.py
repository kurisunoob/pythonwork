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

