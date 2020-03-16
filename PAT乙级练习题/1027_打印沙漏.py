lists = input().split()
number = int(lists[0])
n = int(((number + 1)/2)**0.5)
no_used = number - (2 * n**2 -1)

top = 1 + (n-1) * 2
tmp_top = top
space = -1 # 表示空格数
for i in range(n):
    print("{}{}".format(" "*i, lists[1]*tmp_top))
    tmp_top -= 2
    space += 1

tmp_top += 4
space -= 1
while tmp_top <= top:
    print("{}{}".format(" "*space, lists[1]*tmp_top))
    tmp_top += 2
    space -= 1
print(no_used)
