import math
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

input_str = input()
M = int(input_str.split()[0])
N = int(input_str.split()[1])
prime_list = []
i = 2
times = 0
while True:
    if is_prime(i, prime_list):
        times += 1
        if times >= M and times < N:
            if (times-M+1) % 10 != 0:
                print(i, end=' ')
            else:
                print(i)
        elif times == N:
            print(i)
            break
    i += 1

