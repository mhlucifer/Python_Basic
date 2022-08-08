my_list =['郭德纲', '于谦', '小岳岳', '孙越']

for i in my_list:  # i 就是列表中的每一个数据
    print(i)

print('*' * 30)

j = 0 # j 表示下标
while j < len(my_list):
    print(my_list[j])
    j += 1
    