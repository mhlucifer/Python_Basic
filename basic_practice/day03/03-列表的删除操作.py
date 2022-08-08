my_list = [1, 2, 4, 5, 6, 9]
# 1.根据元素的数据值删除 remove(数据值)，直接原列表中的数据
my_list.remove(4)
print(my_list)
# my_list.remove  # 程序报错，因为要删除的数据不存在


# 2.根据下表删除
# 2.1 pop()默认删除最后一个数据，会返回删除的内容
num = my_list.pop() # 删除最后一个数据 9
print(num)
print(my_list)  # [1,2,5,6]

num = my_list.pop(2)  # 删除下标为2的数据即5
print(num)
print(my_list)
# my_list.pop(10) # 删除的下标不存在，会报错

# 2.2 del 列表[下标]
del my_list[1] # 删除下标为1的数据2
print(my_list)

# del my_list[10] # 删除不存在的下标会报错
