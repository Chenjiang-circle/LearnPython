# 数字黑洞

def product_big_number(input_str1):
    input_str1 = "{:0>4}".format(input_str1)
    input_str = list(input_str1)
    input_str.sort(reverse=True)
    big_number = 0
    for i in input_str:
        big_number *= 10
        big_number += int(i)
    return big_number

def product_small_number(input_str1):
    input_str1 = "{:0>4}".format(input_str1)
    input_str = list(input_str1)
    input_str.sort(reverse=False)
    small_number = 0
    for i in input_str:
        small_number *= 10
        small_number += int(i)
    return small_number

input_str = input()
big_number = product_big_number(input_str)
small_number = product_small_number(input_str)
diff_two_number = big_number - small_number
if diff_two_number == 0:
    print("{:0>4} - {:0>4} = {:0>4}".format(big_number, small_number, diff_two_number))
else:
    print("{:0>4} - {:0>4} = {:0>4}".format(big_number, small_number, diff_two_number))
    while diff_two_number != 6174:
        big_number = product_big_number(str(diff_two_number))
        small_number = product_small_number(str(diff_two_number))
        diff_two_number = big_number - small_number
        if diff_two_number == 0:
            print("{:0>4} - {:0>4} = {:0>4}".format(big_number, small_number, diff_two_number))
            break
        print("{:0>4} - {:0>4} = {:0>4}".format(big_number, small_number, diff_two_number))


