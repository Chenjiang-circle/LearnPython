import turtle


def paint_triangle(Twith, angle, num):
    for i in range(num):
        turtle.seth((angle - i * 120) % 360)
        turtle.fd(Twith)


paint_triangle(300, 30, 3)
turtle.seth(30)
turtle.fd(100)
paint_triangle(100, 90, 1)
paint_triangle(300, 330, 3)
