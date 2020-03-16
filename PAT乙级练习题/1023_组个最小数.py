input_str = input()
input_list = input_str.split()

result = ""

for i in range(1, 10):
    if int(input_list[i]) != 0:
        result = str(i) + result
        input_list[i] = str(int(input_list[i]) - 1)
        break
result = result + str(0)*int(input_list[0])
for i in range(1, 10):
    if input_list[i] != 0:
        result = result + str(i)*int(input_list[i])
print(result)
