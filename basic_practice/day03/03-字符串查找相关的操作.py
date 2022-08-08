my_str = 'hello world itcast and itcastcpp'

# find() 在字符串中查找是否存在某个字符串
# my_str.find(sub_str,start,end)
# sub_str:要在字符串中查找的内容，类型str
# start：开始位置，从哪里开始查找，默认是0
# end：结束的位置，查找到哪里结束，默认是len()
# 返回值：即方法执行的结果是什么，如果找到sub_str，返回的sub_str在my_str的位置下标
# 如果没有找到，返回-1
index = my_str.find('hello') # 0
print(index)
# 从下标为3的位置，开始查找字符串hello
print(my_str.find('hello', 3))   # -1
print(my_str.find('itcast'))  # 12
print(my_str.find('itcast', 15))  # 23
# rfind() right find() 从右边（后边）开始查找
print(my_str.rfind('itcast'))  # 23

# index() 在字符串中查找是否存在某个字符串
# my_str.index(sub_str,start,end)
# sub_str:要在字符串中查找的内容，类型str
# start：开始位置，从哪里开始查找，默认是0
# end：结束的位置，查找到哪里结束，默认是len()
# 返回值：即方法执行的结果是什么，如果找到sub_str，返回的sub_str在my_str的位置下标
# 如果没有找到，index()会报错  （唯一和find()的区别！！）

print(my_str.index('hello'))  # 0
# print(my_str.index('hello', 5))  # 没有找到，代码会报错
# rindex() 从后边查找
print(my_str.index('itcast'))  # 12
print(my_str.rindex('itcast'))  # 23

# count() 统计出现的次数，
print(my_str.count('aaaa'))  # 0
print(my_str.count('hello'))  # 1
print(my_str.count('itcast'))  # 2
print(my_str.count('itcast', 20))  # 1

