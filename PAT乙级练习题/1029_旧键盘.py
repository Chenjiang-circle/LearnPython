input_str = input().split("_")
result_str = input().split("_")

sets = set()

for i in range(len(input_str)):
    input_str_tmp = input_str[i]
    result_str_tmp = result_str[i]
    for i in input_str_tmp:
        if i not in result_str_tmp:
            if 'a' <= i <= 'z':
                if i.upper() not in sets:
                    print(i.upper(), end='')
                    sets.add(i.upper())
            else:
                if i not in sets:
                    print(i, end='')
                    sets.add(i)

