basicInfo = input().split()
dict_node = dict() # 定义一个空的字典，字典中以“节点的地址”为键，以“节点的值和下一个节点的地址”为值
for i in range(int(basicInfo[1])):
    node = input()
    dict_node[node[:5]] = node[6:] # 将每一个节点都存到字典中

linklist = [] # 定义一个空的列表，其中每个元素也为一个列表，每个元素代表要反转的子链表
linklist_child = [] # 该列表用于存储一个子链表，子链表中的节点信息在列表中用一个元组表示

pointer = basicInfo[0] # 定义一个“指针”，用于顺链查找
count = 0 # 计数器，每找到一个完整的子链表，count 归零
while pointer != '-1': # 当“指针”没有到达最后一个节点时
    node_info = dict_node[pointer]
    node_info_list = node_info.split()
    node_info_list.insert(0, pointer)
    linklist_child.append(tuple(node_info_list))
    pointer = node_info_list[-1]
    count += 1
    
    if count == int(basicInfo[2]): # 如果子链表的节点数到达指定数目，计数器归零，将子链表添加到 linklist 中
        count = 0
        linklist.append(linklist_child.copy())
        linklist_child.clear()

# 循环完毕之后判断一下是否有剩余元素
if len(linklist_child) != 0:
    linklist.append(linklist_child)

#print(linklist)
flag = False # 表示是否打印的不是第一行
for linklistChild in linklist:
    #print(linklistChild)
    if len(linklistChild) == int(basicInfo[2]):
        index = -1
        for i in linklistChild:
            node = linklistChild[index]
            if flag:
                print(node[0])
                print("{} {} ".format(node[0], node[1]), end='')
            else:
                print("{} {} ".format(node[0], node[1]), end='')
                flag = True
            index -= 1
    else:
        for node in linklistChild:
            if flag:
                print(node[0])
                print("{} {} ".format(node[0], node[1]), end='')
            else:
                print("{} {} ".format(node[0], node[1]), end='')
                flag = True
print("-1")
