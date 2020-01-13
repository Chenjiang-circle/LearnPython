input_str = input()
input_number = input_str.split()
A1 = 0
A2 = 0
flag_A2 = False
A2_pre = 1
A3 = 0
A4_times = 0
A4 = 0
A5 = 0
for index in range(int(input_number[0])):
    i = input_number[index+1]
    n = int(i) % 5
    if n == 0:
        if int(i) %  2 == 0:
            A1 += int(i)
    elif n == 1:
        flag_A2 = True
        A2 += A2_pre * int(i)
        A2_pre *= -1
    elif n == 2:
        A3 += 1
    elif n == 3:
        A4 += int(i)
        A4_times += 1
    elif n == 4:
        if A5 < int(i):
            A5 = int(i)

if A1 > 0:
    print(A1, end=' ')
else:
    print('N', end=' ')
if flag_A2:
    print(A2, end=' ')
else:
    print('N', end=' ')
if A3 > 0:
    print(A3, end=' ')
else:
    print('N', end=' ')
if A4_times > 0:
    print("{:.1f}".format(A4/A4_times), end=' ')
else:
    print("N", end=' ')
if A5 > 0:
    print(A5)
else:
    print('N')
