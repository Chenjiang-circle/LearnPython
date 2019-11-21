import random

# print(random.random())
# # 随机生成一个a到b的整数
# print(random.randint(1, 3))
# # 生成一个k比特长度的随机整数
# print(random.getrandbits(15))
# # randrange(start, stop[, step])生成一个[start, stop)之间一step为步数的随机整数
# print(random.randrange(0, 100, 4))
# # 生成一个[a, b]之间的随机小数
# print(random.uniform(1, 2))
from math import sqrt
import time

DARTS = 10000000
hits = 0.0
a = time.perf_counter()
for i in range(1, DARTS + 1):
    x, y = random.random(), random.random()
    dist = sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)
b = time.perf_counter()
print("pi的值是：{}".format(pi))
print("用时是：{:.5f}".format(b-a))