n = int(input('请输入正方形边长'))
n = 5
j = 0
# 1.打印一个*
# 1.1 记录一行中已经打印*的个数
while j < n:
    # 2.打印一行的*
    # 2.1记录一行中已经打印的*的个数
    i = 0
    while i < n:
        print('* ', end='')
        i += 1
    # 一行打印结束之后，需要让j+1，同时还需要换行
    print()  # print函数默认会输出换行
    j += 1
# 3.打印n行的*


# for循环实现打印正方形
# 1。打印一行
for j in range(n):
    for i in range(n):
        print('*', end='')
    print()
