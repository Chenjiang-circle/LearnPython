import math
# 判断是否是素数，是素数就返回True，否则返回False
def is_prime(n, prime_list):
    if n < 3:
        return n > 1
    if n == 3:
        prime_list.append(n)
        return True
    if n % 6 != 1 and n % 6 != 5:
        return False
    up_limit = int(math.sqrt(n)) + 1
    for i in prime_list:
        if i > up_limit:
            break
        if n % i == 0:
            return False
    prime_list.append(n)
    return True
    
    
times = eval(input())
if times == 1 or times == 2:
    print(0)
else:
    #  当输入的正整数大于2时，定义一个变量用来记录有多少个素数对（初始值为0）
    N = 0
    # 定义一个变量用来存储“当前”最大的素数A，
    # 如果发现一个素数B，就与“当前”最大的素数做差（B-A）
    # 结果为2，N就加一，“当前”最大素数更新为新的素数的值（A = B）
    pre_prime = 2
    prime_list = [2]
    for i in range(3, times+1, 2):
        if is_prime(i, prime_list):
            if (i - pre_prime) == 2:
                N += 1
            pre_prime = i

    print(N)
