input_lists = input().split()
number_list = input().split()

for i in range(int(input_lists[0])):
    number_list[i] = int(number_list[i])

count = 0
list.sort(number_list) # 默认升序排序

m = -1

for j in range(int(input_lists[0])):
    if int(input_lists[0]) - j <= count:
        break
    tmp_m = number_list[j]
    if tmp_m == m:
        continue
    else:
        m = tmp_m
    for i in range(j+count, int(input_lists[0])):
        if number_list[j] * int(input_lists[1]) >= number_list[i]:
            count += 1
print(count)
