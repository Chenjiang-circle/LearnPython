str = input("请输入一串字符：")
charNumber = 0
intNumber = 0
spaceNumber = 0
otherNumber = 0
for i in str:
    if 'a' <= i <= 'z':
        charNumber += 1
    elif 'A' <= i <= 'Z':
        charNumber += 1
    elif '0' <= i <= '9':
        intNumber += 1
    elif i == ' ':
        spaceNumber += 1
    else:
        otherNumber += 1

print("您一共输入了{}个字母，{}个数字，{}个空格， {}个其他字符。".format(charNumber, intNumber, spaceNumber, otherNumber))