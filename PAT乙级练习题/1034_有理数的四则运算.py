# 化简分数
def reduced_fraction(fraction):
    numerator = 0 # 分子
    denominator = 0 # 分母
    flag = True # 表示是否为负数
    list = fraction.split('/')
    if '-' not in list[0]:
        flag = False
    if flag:
        numberator = int(list[0][1:])
    else:
        numberator = int(list[0])
    denominator = int(list[1])

