import random

L = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';

for i in range(10):
    for j in range(8):
        s = random.randint(0, len(L)-1)
        print(L[s], end="")
    print()
