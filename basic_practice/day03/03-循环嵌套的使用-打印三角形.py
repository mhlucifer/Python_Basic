# 2.定义变量，记录打印的行数
n = 5
j = 0  # 将要打印第一行
while j < n:
    # 1.定义变量记录一行打印的*个数
    i = 0
    while i < j + 1:
        print('*', end=' ')
        i += 1
    print()
    j += 1


# for循环打印三角形
for i in range(n):
    for j in range(i + 1):  # i range(i) 不包含i
        print('* ', end='')
    print()
