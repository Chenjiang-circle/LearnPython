import turtle


# 绘制叠加三角形
# Twith:三角形的宽度
# angle:turtle的绝对角度
# num:画的边数
def paint_triangle(Twith, angle, num):
    for i in range(num):
        turtle.seth((angle + i * 120) % 360)
        turtle.fd(Twith)


paint_triangle(100, 240, 2)
paint_triangle(100, 0, 2)
paint_triangle(100, 120, 2)
paint_triangle(100, 300, 3)
