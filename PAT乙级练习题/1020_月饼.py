input_str = input()
types = input_str.split()[0] # 市面上存在的月饼的种类
needs = int(input_str.split()[1]) # 市场总的需求量

stores = input()
stores_list = stores.split()
total_price = input()
total_price_list = total_price.split()

price = [] # 列表，每个元素是一个元组类型（单价，在原列表中的索引值）
j = 0 
danjia = 0 # 单价，懒得想单词了
for i in stores_list:
    danjia = float(total_price_list[j]) / float(stores_list[j])
    price.append((danjia, j))
    j += 1
price.sort(reverse=True ,key=lambda a:a[0]) # 对列表按单价值，降序排列

sum_price = 0 # 总收益
for i in price:
    if float(stores_list[i[1]]) >= needs: # 如果当前种类的月饼的数量大于等于需求量
        sum_price += i[0] * needs
        break
    else:
        sum_price += float(total_price_list[i[1]])
        needs -= float(stores_list[i[1]])

print("{:.2f}".format(sum_price))
