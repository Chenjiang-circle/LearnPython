import turtle
## 五角星的绘制
# turtle.fillcolor("red")
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.right(144)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.end_fill()

## 太阳花的绘制
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.left(170)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.end_fill

## 1-1
# str1 = input("请输入一个人的名字：")
# str2 = input("请输入一个国家的名字：")
# print("世界这么大，{}想去看看{}".format(str1, str2))

## 1-2 证书序列求和
# n = input("请输入一个整数n：")
# sum = 0
# for i in range(int(n)): # range(3)是0到2
#     sum = sum + i + 1
# print("1加到n的结果为：", sum)

## 1-3 九九乘法表
# for i in range(10):
#     for j in range(1, i+1):
#         print("{}*{}={:2}".format(i, j, i*j), end=' ')
#     print('')

## 1-4 阶乘相加
# n = input("请输入一个整数：")
# sum = 0
# tmp = 1
# for i in range(1, int(n)+1):
#     tmp = tmp * i
#     sum = sum + tmp
# print("1到{}的阶乘为{}".format(n, sum))

## 1-6 list
diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
for x in range(0, 5):
    for y in range(0, 5):
        if not(x == y):
            print("{}{}".format(diet[x], diet[y]))
