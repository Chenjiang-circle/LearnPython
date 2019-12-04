import turtle


# 绘制无边正方形
def paint_no_corner_square(hide, appear, angle):
    for i in range(4):
        turtle.seth((angle + i * 90) % 360)
        turtle.pu()
        turtle.fd(hide)
        turtle.pd()
        turtle.fd(appear)
        turtle.pu()
        turtle.fd(hide)


paint_no_corner_square(29, 20, 0)