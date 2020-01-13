input_str = input()
input_numbers = input()
input_str_list = input_str.split()
N = int(input_str_list[0])
M = int(input_str_list[1])
input_number_list = input_numbers.split()
m = M % N
for i in range(N):
    if i < N-1:
        print(input_number_list[((N-m)+i)%N], end=' ')
    else:
        print(input_number_list[((N-m)+i)%N])
