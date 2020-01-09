# 读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

numPinyin = ["ling",  "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
nums  = eval(input())
# print(type(nums))
number_sum = 0
# print(type(number_sum))
while nums != 0:
    number_sum += nums%10
    nums //= 10

number_sum = str(number_sum)
for i in range(len(number_sum)):
    if i != len(number_sum)-1:
        print(numPinyin[int(number_sum[i])], end=" ")
    else:
        print(numPinyin[int(number_sum[i])])
