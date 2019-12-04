a, b = eval(input("请输入两个整数(用逗号隔开)："))
maxNum = max(a, b)
minNum = min(a, b)
while maxNum % minNum != 0:
    temp = maxNum % minNum
    maxNum = minNum
    minNum = temp
print("{}和{}的最大公约数为:{}，最小公倍数为{}".format(a, b, minNum, int(a*b/minNum)))