for i in 'hello':
    # i一次循环是字符串中的一个字符
    print(i)

# range(n)  会生成[0,n)的数据序列，不包含n
for i in range(5):
    print(i)
for i in range(5):
    print('操场跑五圈')

# range(a,b) 会生成[a,b)的整数序列
for i in range(3,7):
    print(i)

# range(a,b,step)   会生成[a,b)的整数序列,但是每个数字之间的间隔（步长）是step
for i in range(1,10,3):
    print(i)