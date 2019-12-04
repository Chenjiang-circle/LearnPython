import turtle


def paint_two_line(Lwith, angle):
    i = 0
    while Lwith!= 0:
        turtle.seth((angle - i * 90) % 360)
        turtle.fd(Lwith)
        i = i + 1
        turtle.seth((angle - i * 90) % 360)
        turtle.fd(Lwith)
        Lwith = Lwith - 5
        i = i + 1

def paint_two_line2(Lwith, angle):
    i = 0
    iniWith = 5
    while iniWith!= Lwith:
        turtle.seth((angle - i * 90) % 360)
        turtle.fd(iniWith)
        i = i + 1
        turtle.seth((angle - i * 90) % 360)
        turtle.fd(iniWith)
        iniWith = iniWith + 5
        i = i + 1


paint_two_line2(200, 45)