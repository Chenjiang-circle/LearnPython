import random

hide = random.randint(0, 100)
print(hide)
guess = input("请输入你猜测的数字：")
i = 1
while guess != hide:
    if not '0' <= guess <= '9':
        print("输入的内容必须是整数！")
        guess = input("请输入你猜测的数字：")
        i = i + 1
        continue
    if int(guess) < hide:
        print("遗憾，太小了")
    elif int(guess) > hide:
        print("遗憾，太大了")
    else:
        break
    guess = input("请输入你猜测的数字：")
    i = i + 1
if int(guess) == hide:
    print("预测{}次后，你猜中了！".format(i))
