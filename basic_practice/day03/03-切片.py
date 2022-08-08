# 切片可以获取一段数据，多个数据，下标(索引只能获得一个数据)
# 切片语法：变量[start:end:step],会得到一个新的字符串
# start表示开始位置的下标
# end表示结束位置的下标,不包含end对应的下标
# step表示步长，下标之间的间隔，默认是1
my_str = 'hello'
my_str1 = my_str[2:4:1]  #ll
print(my_str1)
# step 如果是1，即默认值，可以不写
my_str2 = my_str[2:4]  #ll
print(my_str2)

# end 位置不写，表示len(),既可以取到最后一个元素
my_str3 = my_str[2:]  # llo
print(my_str3)
# start 位置也可以省略不写,表示是0
my_str4 = my_str[:3]  # hel
print(my_str4)

# start 和end 都不写，但是冒号需要写
my_str5 = my_str[:]
print(my_str5)  # hello

print(my_str[-4:-1])  # ell
print(my_str[3:1])  # 没有数据
# 步长可以是负数
print(my_str[3:1:-1], '2')  # ll

print(my_str[::-1])  # 字符串的逆置,olleh

print(my_str[::2])  # 0 2 hlo my
