my_list = [1, 3.14, 'issac', True]
# index() 根据数据值，查找元素所在的下标，找到返回元素的下标，没有找到，程序报错
# 列表中没有find方法，只有index()方法
# 查找3.14在列表中下标
num = my_list.index(3.14)  # 1
print(num)

# num1 = my_list.index(100) # 程序报错，因为数据不存在
# count() 统计出现的次数
num3 = my_list.count(1)  # 1
print(num3)   # True会被当成1计算，所以是2
# in/not in   判断是否存在，存在是True，不存在是False
num4 = 3.14 in my_list  # True
print(num4)

num5 = 3.14 not in my_list  # False
print(num5)
