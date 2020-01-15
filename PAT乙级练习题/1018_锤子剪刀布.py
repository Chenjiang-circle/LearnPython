## 一个测试用例过不去
import random

items = ['C', 'J', 'B']
times = eval(input())
win = ["C J", "J B", "B C"]
win_times_a = 0
win_state_a = {'B':0, 'C':0, 'J':0}
win_times_b = 0
win_state_b = {'B':0, 'C':0, 'J':0}
draw_times = 0
while times > 0:
    input_str = input()
    if input_str[0] == input_str[-1]:
        draw_times += 1
    else:
        if input_str in win:
            win_times_a += 1
            win_state_a[input_str[0]] = win_state_a.get(input_str[0]) + 1
        else:
            win_times_b += 1
            win_state_b[input_str[-1]] = win_state_b.get(input_str[-1]) + 1
    times -= 1

ls1 = list(win_state_a.items())
ls2 = list(win_state_b.items())
ls1.sort(key=lambda x:x[1], reverse=True)
ls2.sort(key=lambda x:x[1], reverse=True)
print(win_times_a, draw_times, win_times_b)
print(win_times_b, draw_times, win_times_a)
print(ls1[0][0], ls2[0][0])

