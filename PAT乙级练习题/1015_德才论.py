def sort_by_de(ls):
    flag = True
    index_start = 0
    index_end = 0
    for i in range(len(ls)-1):
        if ls[i][3] == ls[i+1][3]:
            if flag:
                index_start = i
                flag = False
            index_end = i+1
        else:
            if index_start == index_end:
                flag = True
                continue
            else:
                tmp = ls[index_start: index_end+1]
                tmp.sort(key=lambda de: de[1], reverse=True)
                ls[index_start: index_end+1] = tmp
                index_start = i+1
                index_end = i+1
                flag = True
        if index_end == len(ls)-1 and index_end != index_start:
            tmp = ls[index_start:]
            tmp.sort(key=lambda de: de[1], reverse=True)
            ls[index_start:] = tmp
def sort_by_id(ls):
    flag = True
    index_start = 0
    index_end = 0
    for i in range(len(ls)-1):
        if ls[i][1] == ls[i+1][1]:
            if flag:
                index_start = i
                flag = False
            index_end = i+1
        else:
            if index_start == index_end:
                flag = True
                continue
            else:
                tmp = ls[index_start: index_end+1]
                tmp.sort(key=lambda de: de[0], reverse=False)
                ls[index_start: index_end+1] = tmp
                index_start = i+1
                index_end = i+1
                flag = True
        if index_end == len(ls)-1 and index_end != index_start:
            tmp = ls[index_start:]
            tmp.sort(key=lambda de: de[1], reverse=False)
            ls[index_start:] = tmp
input_str = input()
N = int(input_str.split()[0])
L = int(input_str.split()[1])
H = int(input_str.split()[2])
qualification_number = 0
one_people = []
two_people = []
three_people = []
four_people = []
while N > 0:
    input_info = input()
    temp_list = input_info.split()
    temp_de = int(temp_list[1])
    temp_cai = int(temp_list[2])
    temp_sum = temp_de + temp_cai
    if temp_de < L or temp_cai < L: # 淘汰考生
        N -= 1
        continue
    elif temp_de >= H and temp_cai >= H: # 第一类考生
        qualification_number += 1
        temp_list.append(temp_sum)
        one_people.append(temp_list)
    elif temp_de >= H and temp_cai < H: # 第二类考生
        qualification_number += 1
        temp_list.append(temp_sum)
        two_people.append(temp_list)
    elif temp_de < H and temp_cai < H and temp_de >= temp_cai: # 第三类考生
        qualification_number += 1
        temp_list.append(temp_sum)
        three_people.append(temp_list)
    else: # 其他考生
        qualification_number += 1
        temp_list.append(temp_sum)
        four_people.append(temp_list)
    N -= 1
one_people.sort(key=lambda number: number[3], reverse=True)
sort_by_de(one_people)
sort_by_id(one_people)
two_people.sort(key=lambda number: number[3], reverse=True)
sort_by_de(two_people)
sort_by_id(two_people)
three_people.sort(key=lambda number: number[3], reverse=True)
sort_by_de(three_people)
sort_by_id(three_people)
four_people.sort(key=lambda number: number[3], reverse=True)
sort_by_de(four_people)
sort_by_id(four_people)
print(qualification_number)
for i in one_people:
    print(i[0], i[1], i[2])
for i in two_people:
    print(i[0], i[1], i[2])
for i in three_people:
    print(i[0], i[1], i[2])
for i in four_people:
    print(i[0], i[1], i[2])

