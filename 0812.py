print '你好'
# for循环
L = [75, 92, 59, 68]
sum = 0.0
for num in L:
	print num

# while循环
N = 10
x = 0
while x < N:
	print x
	x = x + 1

# break退出循环
print 'break退出循环++++++++'
sum = 0
x = 1
while True:
	sum = sum + x
	x= x + 1
	if x > 100:
		break
print sum
print 'break退出循环--------'

# continue继续循环
L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
	if  x < 60:
		continue
	sum = sum + x
	n = n + 1
print sum

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