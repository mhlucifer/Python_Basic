# 想要对列表中的数据进行排序，前提是列表中的数据类型是一样的
my_list = [1, 5, 3, 7, 9, 6]

# 列表.sort() 直接在原列表中进行排序
# my_list.sort()  # 默认是从小到大排序，即升序
my_list.sort(reverse=True)  # 通过reverse=True，从大到小排序
print(my_list)

# 补充：sorted(列表) 排序，不会在原列表中进行排序，会得到一个新的列表

my_list1 = sorted(my_list)
my_list2 = sorted(my_list,reverse=True)
print(my_list)
print(my_list1)
print(my_list2)

print("=" * 30)
my_list3 = ['a', 'b', 'c', 'd', 'e']
# 逆置
my_list4 = my_list3[::-1]  # 得到一个新的列表
print(my_list3)
print(my_list4)

# 在原列表中直接逆置，列表.reverse()
my_list3.reverse()
print(my_list3)
