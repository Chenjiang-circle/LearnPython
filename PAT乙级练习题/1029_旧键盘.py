input_str = input() # 输入的内容
result_str = input() # 实际显示的内容

sets = set() # 创建一个集合，用来存放坏掉的“键”

# 需要考虑到空格坏掉的情况
for i in input_str:
    if i not in result_str:
        if 'a' <= i <= 'z':
            if i.upper() not in sets:
                print(i.upper(), end='')
                sets.add(i.upper())
        elif i == '_':
            if i not in sets:
                print('_', end='')
                sets.add(i)
        else:
            if i not in sets:
                print(i, end='')
                sets.add(i)
