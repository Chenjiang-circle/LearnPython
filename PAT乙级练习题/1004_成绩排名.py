times = eval(input())
i = 1
max_list = []
min_list = []
info_str = input()
max_list = info_str.split()
min_list = info_str.split()
while i < times:
    info_str = input()
    new_list = info_str.split()
    if int(max_list[2]) < int(new_list[2]):
        max_list = new_list
    if int(min_list[2]) > int(new_list[2]):
        min_list = new_list
    i += 1

print("{} {}\n{} {}".format(max_list[0], max_list[1], min_list[0], min_list[1]))
    
