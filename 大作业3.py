# 打字游戏

import random

def gameStart():
    times = eval(input("请输入打字次数："))
    print()
    i = 0 # 计数
    allHits = 0 # 记录总共正确的字符
    lengthSum = 0 # 记录生成的字符串的总长度
    while(i < times):
        thisHits = 0 # 记录当前回合正确的字符
        correctString = productString() # 随机生成一个字符串
        print(correctString)
        myString = input()
        if not len(correctString) >= len(myString): # 如果长度不相等，本回合不计数
            print("你输入的串长超长，无效\n")
            continue

        i += 1
        lengthSum += len(correctString)
        thisHits = comparetwoString(correctString, myString)
        allHits += thisHits
        print("本次的正确率是{0:.2f}%\n".format(thisHits/len(correctString) * 100))
    print("整体的正确率是：{0:.2f}%".format(allHits/lengthSum * 100))


# 随机生成一个长度为[1, 15]的字符串
def productString():
    charList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    randomLength = random.randint(1, 15)
    correctString = ""
    for i in range(randomLength):
        if randomLength == 1:
            randomInt = random.randint(0, len(charList)-2)
        elif i != randomLength: # 生成的字符串最后一个不能是空格
            randomInt = random.randint(0, len(charList)-1)
        else:
            randomInt = random.randint(0, len(charList)-2)
        correctString += charList[randomInt]

    return correctString


def comparetwoString(correctString, myString):
    hits = 0
    for i in range(len(myString)):
        if correctString[i] == myString[i]:
            hits += 1
    return hits


def main():
    gameStart()
    
main()
