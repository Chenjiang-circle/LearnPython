input_str = input()

result = [] # 用于存储结果
if input_str[0] == "-": # 如果是负数，就将负号输出
    result.append("-")


decimal_part = "" # 小数部分
direction = True # 小数点移动的方向，True 表示左移；False 表示右移
move_number = 0 # 小数点移动的位数
for i in range(1, len(input_str)):
    if input_str[i] == "E":
        decimal_part = input_str[3:i]
    if input_str[i] == "+":
        direction = False
        move_number = int(input_str[i+1:])
        break
    elif input_str[i] == "-":
        direction = True
        move_number = int(input_str[i+1:])
        break

if direction: # 如果是左移
    if move_number == 0: # 如果移动的位数为0
        result.append(input_str[1:3]) # 将小数点前面的数字输出
        result.append(decimal_part) # 将小数点后面的数字输出
    if move_number > 0:  # 如果移动的位数大于0
        result.append("0.") # 先将固定的格式输出
        result.append("0"*(move_number-1)) # 计算补零的个数
        result.append(input_str[1:2]) # 再将第一位数字输出
        result.append(decimal_part) # 将小数点后的数字输出
else:         # 如果小数点右移
    result.append(input_str[1:2]) # 先将原数种小数点前面的数字输出
    if move_number == 0: # 如果小数点移动的位数为0
        result.append(input_str[2:3]) # 将小数点输出
        result.append(decimal_part) # 将小数点后面的数字输出
    elif move_number < len(decimal_part):
        result.append(decimal_part[:move_number])
        result.append(".")
        result.append(decimal_part[move_number:])
    else:
        result.append(decimal_part)
        result.append("0"*(move_number-len(decimal_part)))
for i in result:
    print(i, end='')

        
