# 绘制田字格


def paint(num):
    # 先循环打印出来n个下面的图型
    # + - - - - + - - - - + - - - - + - - - - +
    # |         |         |         |         |
    # |         |         |         |         |
    # |         |         |         |         |
    # |         |         |         |         |
    # 最后打印出来
    # + - - - - + - - - - + - - - - + - - - - +
    for i in range(num):
        for j in range(num):
            print("+ - - - - ", end="")
        print("+")
        for k in range(num):
            for j in range(num):
                print("|         ", end="")
            print("|")
    for j in range(num):
        print("+ - - - - ", end="")
    print("+")


paint(5)