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