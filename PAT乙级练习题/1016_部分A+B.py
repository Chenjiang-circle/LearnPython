input_str = input()
ls = input_str.split()
A = ls[0]
Da = ls[1]
B = ls[2]
Db = ls[3]

pre_A = "0"
for i in A:
    if i == Da:
        pre_A += "1"

pre_B = "0"
for i in B:
    if i == Db:
        pre_B += "1"


sum_A = int(pre_A) * int(Da)
sum_B = int(pre_B) * int(Db)
print(sum_A + sum_B)
