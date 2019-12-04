# 判断是否为数字的函数


def isFloatNum(str):
    list = str.split('.')
    # 首先判断是否是一个小数点，如果是一个小数点，则将字符串按点分割成的两部分分别判断是否全是数字
    if len(list) == 2:
        for i in list:
            if i.isnumeric():
                continue
            else:
                list2 = i.split('e')
                if len(list) != '2':
                    return False
                elif not list2[0].isnumeric():
                    return False
                elif not list2[1][0] in ['+', '-']:
                    return False
                elif not list2[1][1:].isnumeric():
                    return False
                else:
                    return True
        return True
    else:
        return False


def isPlurality(str):
    jorJ = ''
    # 先判断j的数量
    if 'j' in str:
        jorJ = 'j'
        if len(str.split('j')) != 2:
            return False
    elif 'J' in str:
        jorJ = 'J'
        if len(str.split('J')) != 2:
            return False


    list = str.split('+')
    new_list = []
    for i in range(len(list)):
        if '-' in list[i]:
            new_list += list[i].split('-')
        else:
            new_list.append(list[i])
    # 如果出现连续的+-号，则返回False
    if "" in new_list:
        print("1")
        return False

    # if new_list[-1][-1] not in ['j', 'J']:
    #     print("2")
    #     return False
    # else:
    #     new_list[-1] = new_list[-1][:-1]

    for i in range(len(new_list)):
        if new_list[i].isnumeric():
            continue
        if jorJ in new_list[i]:
            small_list = new_list[i].split(jorJ)
            print("1", small_list)
            if len(small_list) != 2:
                print(3)
                return False
            elif '' not in small_list:
                print(4)
                return False
            elif not small_list[0].isnumeric():
                if small_list[0] == '':
                    continue
                print(5)
                return False
            else:
                continue

        small_list = new_list[i].split('e')
        print(small_list)
        if len(small_list) != 2:
            print(3)
            return False
        elif '' not in small_list:
            print(4)
            return False
        elif not (small_list[0].isnumeric() or isFloatNum(small_list[0])):
            print(5)
            return False
        else:
            continue

    return True


def isNum(str):
    if str[0] in ['-', '+']:
        str = str[1:]
    if str.isnumeric():
        return True

    a = isFloatNum(str)
    if a:
        return a

    b = isPlurality(str)
    if b:
        return b
    else:
        return False



print(isNum("12e+12j"))
