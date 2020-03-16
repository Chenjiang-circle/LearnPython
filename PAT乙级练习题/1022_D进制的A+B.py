# 任意进制转换
# 0 的 ASCII 码值为48
# 9 的 ASCII 码值为57

def change(number, D): # number 表示要转换十进制整数，D表示要转换成的进制
    result = ""
    tmp = 0
    while number != 0:
        tmp = number % D
        number = number // D
        result = str(tmp) + result
    if result == "":
        return "0"
    return result

input_str = input()
input_list = input_str.split()
A = int(input_list[0])
B = int(input_list[1])
D = int(input_list[2])

print(change(A+B, D))
