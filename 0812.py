import math
print '你好'
# for循环
L = [75, 92, 59, 68]
#sum = 0.0
#for num in L:
	#print num

# while循环
#N = 10
#x = 0
#while x < N:
	#print x
	#x = x + 1

# break退出循环
#print 'break退出循环++++++++'
#sum = 0
#x = 1
#while True:
	#sum = sum + x
	#x= x + 1
	#if x > 100:
		#break
#print sum
#print 'break退出循环--------'

# continue继续循环
#L = [75, 98, 59, 81, 66, 43, 69, 85]
#sum = 0.0
#n = 0
#for x in L:
	#if  x < 60:
		#continue
	#sum = sum + x
	#n = n + 1
#print sum

# 多重循环
for x in ['A', 'B', 'C', 'D']:
	for y in ['1', '2', '3']:
		print x + y

# dict 集合
d = {
	'age': 86,
	'Adam': 95,
	'Lisa': 85,
	'Bart': 59
}
print d['age']
print d.get('Age') # 使用get方法，在key不存在的时候，返回None
print len(d)
# dict特点：查找速度快，但是占用内存大，会浪费很多内容，但是list正好相反，占用内存小，但是查找速度慢

# 更新dict
d['Paul'] = 97 # 如果建已存在，则赋值会用新的value替换掉原来的value
print d

# 遍历dict
for key in d:
	print key
# 遍历键值对
for key in d:
	print key, d[key]
# set 方法
s = set(['A', 'B', 'C', 'D'])
print s
print 's的长度是', len(s)

# 使用in来判断某一元素是不是在set中
print 'a' in s
#  遍历set的元素
for name in s:
	print name
# 更新set

s.add('E')
print '添加E之后打印s',s
s.remove('D')
print '删除D之后打印s',s

# 函数调用
print abs(6.9)
print str(123)
print str(1.23)
print '你好'
L1 = []
for b in range(0, 101):
	a = b * 2
	L1.append(a)
print sum(L1)
# 比较函数
print cmp(1, 2)

# 自定义函数
def square_of_sum(L):
	a = 0.0
	for b in L:
		a = a + b * b
	return a
print square_of_sum([1, 2, 3, 4, 5])

# 计算一元二次方程的解
def quadratic_equation(a, b, c):
	de = b**2-4*a*c
	if de >= 0:
		x1 = (-b + math.sqrt(de))/(2*a)
		x2 = (-b - math.sqrt(de))/(2*a)
		return x1, x2
	else:
		return

print quadratic_equation(2, 3, 0)

# 递归函数
def fact(n):
	if n==1:
		return 1
	return n * fact(n-1)

print fact(10)

# 汉诺塔
# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到c柱子上面去
def move(n, a, b, c):
	if n == 1:
		print a,'-->',c
		return
	move(n-1, a, c, b)
	print a, '-->', c
	move(n-1, b, a, c)

move(4, 'A', 'B', 'C')

# 设定默认参数 由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必须参数的后面
def greet(s = 'world'):
	print 'Hello', s
greet()
greet('Da')

# 定义可变参数
def average(*args):
	if len(args) != 0:
		return sum(args)*1.0/len(args)
	else:
		return 0.0
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)

# 对list进行切片
list_1 = range(1, 101)
print list_1[0:10]
print list_1[2:101:3] #每三个取一个
print list_1[4:50:5] #不大于50的5的倍数

# 对list进行倒序切片
list_2 = range(1, 101)
print list_2[-10:] #打印最后10个
print list_2[4::5][-10:] #最后10个 5的倍数，需要现将5的倍数找出来，再将倒数10个找出来。（多次切片）
# 对字符串进行切片操作更对list操作一样
def firstCharUpper(s):
	return s[:1].upper()+s[-len(s)+1:]
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')

# 迭代
for i in range(1,101):
	if(i%7==0):
		print i
# 索引迭代
list_3 = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(list_3):
	print index+1, '-', name

# 迭代dict的value
d_1 = {
	'Adam':95,
	'Lisa':85,
	'Bart':98,
	'Paul':64
}
sum_1 = 0.0
for num in d_1.itervalues():
	sum_1 = sum_1 + num
print sum_1/len(d_1)

# 迭代dict的value和key
sum_2 = 0.0
for k, v in d_1.iteritems():
	sum_2 = sum_2 + v
	print k, ':', v
print 'average', ':', sum_2/len(d_1)