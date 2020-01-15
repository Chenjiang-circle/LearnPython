str_one = input()
str_two = input()
str_three = input()
str_four = input()

DAY = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
hours = "0123456789ABCDEFGHIJKLMN"
flag_day = False
flag_hour = False
flag_minute = False
day = ""
hour = 0
minute = 0
for i in range(min(len(str_one), len(str_two))):
    # 如果字符相等
    if str_one[i] == str_two[i]:
        # 如果字符相等，并且day还没确定，就去判断相等的字符是否是大写字母
        if not flag_day:
            if ord('A') <= ord(str_one[i]) <= ord('Z'):
                # print(str_one[i])
                if ord(str_one[i]) - ord('A') <= 6:
                    day = DAY[ord(str_one[i]) - ord('A')]
                    flag_day = True
        elif not flag_hour:
            if ord('0') <= ord(str_one[i]) <= ord('9'):
                # print(str_one[i])
                hour = ord(str_one[i]) - ord('0')
                flag_hour = True
            elif ord('A') <= ord(str_one[i]) <= ord('N'):
                # print(str_one[i])
                hour = ord(str_one[i]) - ord('A') + 10
                flag_hour = True
        elif not flag_minute:
            if ord('a') <= ord(str_one[i]) <= ord('z') or ord('A') <= ord(str_one[i]) <= ord('Z'):
                minute = i

for i in range(min(len(str_three), len(str_four))):
    if str_three[i] == str_four[i]:
        if not flag_day:
            if ord('A') <= ord(str_three[i]) <= ord('Z'):
                # print(str_one[i])
                if ord(str_three[i]) - ord('A') <= 6:
                    day = DAY[ord(str_three[i]) - ord('A')]
                    flag_day = True
        elif not flag_hour:
            if ord('0') <= ord(str_three[i]) <= ord('9'):
                # print(str_one[i])
                hour = ord(str_three[i]) - ord('0')
                flag_hour = True
            elif ord('A') <= ord(str_three[i]) <= ord('N'):
                # print(str_one[i])
                hour = ord(str_three[i]) - ord('A') + 10
                flag_hour = True
        elif not flag_minute:
            if ord('a') <= ord(str_three[i]) <= ord('z') or ord('A') <= ord(str_three[i]) <= ord('Z'):
                minute = i

print("{} {:0>2}:{:0>2}".format(day, hour, minute))
