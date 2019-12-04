# multi()函数

def multi(num1=1, *mun2):
    num = 1
    num = num * num1
    for i in mun2:
        num *= i

    return num

print(multi(2, 3))