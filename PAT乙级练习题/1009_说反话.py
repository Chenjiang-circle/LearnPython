input_str = input()
input_list = input_str.split()
for i in range(len(input_list)):
    if i < len(input_list)-1:
        print(input_list[-1*(i+1)], end=' ')
    else:
        print(input_list[-1*(i+1)])
