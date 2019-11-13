TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F', 'f']:
    c = (eval(TempStr[0:-1]) - 32) / 18
    print("转换后的温度是{:.2f}C".format(c))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("格式错误")