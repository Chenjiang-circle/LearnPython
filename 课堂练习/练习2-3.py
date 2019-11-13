import turtle

# 彩色的蟒蛇
colors = ['red', 'blue', 'green', 'grey', 'gold', 'violet', 'purple', 'black']
turtle.setup(650, 350, 200, 200)
turtle.pu()
turtle.fd(-250)
turtle.pd()
turtle.pensize(25)
turtle.pencolor("yellow")
turtle.seth(-40)
for i in range(4):
    turtle.pencolor(colors[i])
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)