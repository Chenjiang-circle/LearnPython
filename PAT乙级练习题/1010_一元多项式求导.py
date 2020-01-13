input_str = input()
input_number_list = input_str.split()
new_list = []
for i in range(0, len(input_number_list), 2):
    if int(input_number_list[i+1]) != 0:
        new_list.append(int(input_number_list[i]) * int(input_number_list[i+1]))
        new_list.append(int(input_number_list[i+1]) - 1)
    else:
        if i == 0:
            new_list.append(0)
            new_list.append(0)
            break

for i in range(len(new_list)):
    if i < len(new_list)-1:
        print(new_list[i], end=' ')
    else:
        print(new_list[i])
