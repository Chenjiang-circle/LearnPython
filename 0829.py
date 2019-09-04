# 高阶函数
import math
def add(x, y, f):
	return f(x) + f(y)

print add(25, 9, math.sqrt)

# map()函数
def f(x):
	return x * x

print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def format_name(s):
	return s[0].upper() + s[1:].lower()

print map(format_name, ['adam', 'LIST', 'BARt'])
# reduce()函数
def prod(x, y):
	return x * y
# list求积
print reduce(prod, [2, 4, 5, 7, 12], 1)