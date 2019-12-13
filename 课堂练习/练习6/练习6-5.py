import random


def prodfuctBirthday():
    # 没必要生成月和日,一年就365天,在1到365中,随机生成一个数就可以了
    # mouth = random.randint(1, 12)
    # days = 0
    # if mouth in [1, 3, 5, 7, 8, 10, 12]:
    #     days = random.randint(1, 31)
    # elif mouth in [4, 6, 9, 11]:
    #     days = random.randint(1, 30)
    # else:
    #     days = random.randint(0, 29)
    #
    # return mouth, days
    day = random.randint(1, 365)
    return day

def haveSame(L):
    L = list(L)
    L2 = set(L)
    if len(L) == len(L2):
        return False
    else:
        return True

trys = 1000
hits = 0
for i in range(trys):
    L = []
    for j in range(23):
        L.append(prodfuctBirthday())
    if haveSame(L):
        hits = hits + 1
    else:
        hits = hits
    # print(L)

print(hits/trys)