##number = eval(input())
##d = dict()
##big_number = 0
##big_score = 0
##for i in range(number):
##    list = input().split()
##    if list[0] in d:
##        d[list[0]] += int(list[1])
##    else:
##        d[list[0]] = int(list[1])
##    if d[list[0]] > big_score:
##        big_score = d[list[0]]
##        big_number = int(list[0])
##
##print(big_number, big_score)
number = eval(input())
list1 = []
for i in range(number+1):
    list1.append(int(0))

big_number = 0
big_score = 0
for i in range(number):
    inputs = input().split()
    list1[int(inputs[0])] += int(inputs[1])
    if list1[int(inputs[0])] > big_score:
        big_score = list1[int(inputs[0])]
        big_number = int(inputs[0])
print(big_number, big_score)
