def juge_palindrome(str):
    length = len(str)
    print(length)
    for i in range(int(length / 2)):
        if not str[i] == str[0-i-1]:
            print("{}不是回文数".format(str))
            return
    print("{}是回文数".format(str))


num = input("请输入一个整数：")
juge_palindrome(num)