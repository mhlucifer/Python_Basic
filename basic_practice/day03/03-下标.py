# 下标也成为索引，是一个整形数字，可以是正数，也可以是负数
# 正数下标是从0开始的，表示第一个字符，-1 表示最后一个字符
my_str = 'hello'
# 下标的使用语法 变量[下标]
print(my_str[0])  # h
print(my_str[1])  # e
print(my_str[-1])  # o
print(my_str[-3])  # l

# len()函数可以得到字符串的长度
print(len(my_str))  # 5
# 使用正数下标书写字符串中最后一个元素
print(len(my_str) - 1)
