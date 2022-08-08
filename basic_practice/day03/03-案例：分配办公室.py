import random
# 1.定义一个列表用于保存3个办公室 ，定义学校及其办公室，所以需要嵌套列表
schools = [[], [], []]  # 三个小列表就是三个办公室
# 2.定义一个列表用来存储8位老师的名字
teachers = ["A", "B", "C","D", "E", "F", "G", "H"]
# 3.用随机来分配老师，即抓阄。for遍历老师列表：抓阄，产生随机数，进入对应办公室
# 3.1 遍历老师列表
for teacher in teachers:
    # 3.2抓阄，产生随机数
    num = random.randint(0, 2)  # randint是唯一一个包含结束位置的。产生的随机数，相当于办公室的下标
    # 3.3 老师进入办公室，将老师名字添加到办公室列表中
    schools[num].append(teacher)

print(schools)
for office in schools:
    print(f'该办公室老师的个数为{len(office)},办公室老师名字为')
    for teacher in office:
        print(teacher, end='')
    print()

