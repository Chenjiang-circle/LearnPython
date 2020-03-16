number = eval(input())

list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tmp = 10
while number!=0:
    tmp = number % 10
    number //= 10
    list[tmp] += 1

for i in range(len(list)):
    if list[i] != 0:
        print("{}:{}".format(i, list[i]))
