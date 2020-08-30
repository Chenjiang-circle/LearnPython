# judge方法用于判断字符串是否合法，如果合法返回true，否则返回false。
def judge(input_str):
    P_position = -1; # 字母P的下标
    T_position = -1; # 字母T的下标
    P_num = 0; # 字母P的数量
    T_num = 0; # 字母T的数量
    A_num = 0;
    leftA_num = 0; # 字母P左边的字母A的数量
    midA_num = 0; # 字母P右边字母T左边的字母A的数量
    rightA_num = 0; # 字母T右边的字母A的数量
    # 遍历字符串，检查是否“只包含PAT三个字母”，并确定字母P
    for i in range(len(input_str)):
        if(input_str[i] != str('P') and input_str[i] != str('A') and input_str[i] != "T"):
            # print("{},1", input_str)
            return False
        if(input_str[i] == "P"):
            P_position = i
            P_num += 1;
        if (input_str[i] == "T"):
            T_position = i;
            T_num += 1;
        if(input_str[i] == "A"):
            A_num += 1;
    # 如果P在T的右边，或者P和T的数量大于1，或者没有A，则返回False
    if(P_position > T_position or P_num > 1 or T_num > 1 or A_num < 1):
        # print("{},2", input_str)
        return False
    # 统计P左边A的数量，中间A的数量，T右边A的数量
    if P_position != 0:
        leftA_num = P_position;
    if T_position != len(input_str):
        rightA_num = len(input_str) - T_position - 1;
    midA_num = T_position - P_position - 1;
    # 如果右边A的数量的左边A的数量*中间A的数量，则返回True；否则返回False
    if (rightA_num == leftA_num * midA_num):
        return True
    else:
        # print("{0},3,左边：{1}，中间：{2}，右边：{3}".format(input_str, leftA_num, midA_num, rightA_num))
        return False
num = eval(input())
result_list = []
for i in range(num):
    result_list.append("")
for i in range(num):
    result_list[i] = str(judge(input()))
# print(result_list)
for i in range(num):
    if result_list[i] == "True":
        print("YES")
    else:
        print("NO")
