# my_str.join(可迭代对象)
# 可迭代对象，str，列表(需要列表中的每一个数据都是字符串类型)
# 讲my_str 这个字符串添加到可迭代对象的两个元素之间
# 返回值：一个新的字符串

my_str = '_'.join('hello')  # 会把_加入到hello每两个元素之间 即h_e_l_l_o
print(my_str)
print('_*_'.join('hello'))  # h_*_e_*_l_*_l_*_o

# 定义列表
my_list = ['hello', 'cpp', 'python']  # hello_cpp_python
print("_".join(my_list))
print("_*_".join(my_list))  # hello_*_cpp_*_python
print(" ".join(my_list))   # hello cpp python



