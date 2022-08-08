my_str = 'hello world itcast and itcastcpp'

# my_str.split(sub_str,count)  将my_str字符串按照sub_str 进行切割,
# sub_str:按照什么内容切割字符串,默认是空白字符，空格，tab键
# count 切割几次，默认是全部切割
# 返回值：列表 []

result = my_str.split()  # 按照空白字符，全部切割
print(result)
print(my_str.split('itcast'))
print(my_str.split('itcast', 1))  # 切割1次
print(my_str.rsplit('itcast', 1))

