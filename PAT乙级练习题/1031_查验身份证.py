def check(number):
    if len(number) != 18:   # 首先判断输入的字符串长读是否为18
        print(number)
        return False
    try:                    # 判断前17个字符是否是数字。如果不是，输出
        eval(number[:-1])
    except BaseException:
        print(number)
        return False
    tmp = 0                 # 加权和
    list1 =[7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    list2 = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(17):     # 循环遍历求加权和
        tmp = tmp + int(number[i]) * list1[i]
    z = tmp % 11
    # 判断校验位
    if str(list2[z]) == str(number[-1]):
        return True
    else:
        print(number)
        return False

flag = True                 # 用来判断是否全对
number = eval(input())
for i in range(number):
    num = input()
    flag = flag & check(num)

if flag:
    print("All passed")
