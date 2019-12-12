def judge(L):
    L = list(L)
    len1 = len(L)
    L2 = set(L)
    len2 = len(L2)
    if len1 == len2:
        return False
    else:
        return True

print(judge([1, 2, 3, 4, 5, 6, 7, 7]))
print(judge(["nihao", 'nihao', 3, 4, 5, 6, 7, 7]))