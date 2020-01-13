times = eval(input())
result = []
i = 0
while i < times:
    input_str = input()
    ls = input_str.split()
    i += 1
    if int(ls[0]) + int(ls[1]) > int(ls[2]):
        result.append('true')
    else:
        result.append('false')
i = 1
for n in result:
    print("Case #{}: {}".format(i, n))
    i += 1
