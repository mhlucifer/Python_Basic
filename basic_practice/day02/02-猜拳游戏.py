import random

# 1.用户输入自己出拳的内容
user = eval(input('请输入要出的拳：1（石头）2（剪刀）3（布）'))
# 2.让电脑随机出拳
computer = random.randint(1, 3)  # 随机产生1-3之间的随机数

# 3.判断胜负
# 3.1平局 输入内容一样 user==computer
# 3.2 uesr胜利 1.user==1 and computer ==2 2.user and computer == 3 3.user == 3 and computer==1
# 3.3 else 剩下都是电脑胜利
if user == computer:
    print('平局')
elif(user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    print('恭喜你，胜利了')
else:
    print("你输了")
