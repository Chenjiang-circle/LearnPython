# 羊车门问题
import random

tryNumber = 10000
doors = [True, False, False]
changeHits = 0
keepHits = 0
for i in range(tryNumber):
    num = random.randint(0, 2)
    print(num)
    # 先说不更换自己的选择
    if doors[num]:
        keepHits += 1
    # 再说更换自己选择的情况
    else:
        changeHits += 1

print("如果不更换自己的选择，其选到车的概率为{}".format(keepHits/tryNumber))
print("如果更换自己的选择，其选到车的概率为{}".format(changeHits/tryNumber))