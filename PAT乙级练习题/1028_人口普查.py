number = eval(input())

population = 0 # 有效生日的个数
most_old_name = ""
most_old_age = "2014/09/06"
most_young_name = ""
most_young_age = "1814/09/06"
all_people = []

for i in range(number):
    lists = input().split()
    # 首先判断是否合法
    if lists[1] > "2014/09/06" or lists[1] < "1814/09/06":
        continue
    population += 1
    if lists[1] > most_young_age:
        most_young_age = lists[1]
        most_young_name = lists[0]
    if lists[1] < most_old_age:
         most_old_age = lists[1]
         most_old_name = lists[0]
    
if population == 0:
    print(0)
else:
    print("{} {} {}".format(population, most_old_name, most_young_name))
