﻿# 这是9月4号学习的Python
# filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
def is_odd(x):
	return x % 2 == 1

a = filter(is_odd, [1, 3, 4, 6, 7, 9, 12, 17])
print a

# 利用filter判断出1到100中能被整开方的数
import math
def is_sqr(x):
	return math.sqrt(x) % 1 == 0

print filter(is_sqr, range(1, 101))