# 向列表中添加数据的方法，都是直接在原列表中进行添加的，不会返回新的列表
# 列表.append(数据) 向列表尾部追加数据
my_list =['郭德纲', '于谦', '小岳岳', '孙越']
my_list.append('aa')
print(my_list)
result = my_list.append(12)  # 不要这样书写
print(result)   # None 关键字，表示空
print(my_list)
# 列表.insert(下标，数据)在指定的下标位置进行添加数据
my_list.insert(0, 'issac')
print(my_list)
print(my_list.insert(5, 3.14)) # 不能这样写，None，因为他打印的是返回值，我们想要的是列表
# 列表.extend(可迭代对象)  # str 列表，会将可迭代对象中的数据逐个添加到原列表的末尾
my_list.extend('hel')
print(my_list)
my_list.extend([1, 'python', 3])
print(my_list)
