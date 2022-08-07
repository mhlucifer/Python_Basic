# python中的输出使用print函数
# 基本输出
print('hello')
print(123)


print("issac", 18)
# 书写表达式
print(1 + 2)  # 会输出1+2
name = "issac"
print("我的名字是%s，我很开心." % name)

age =18
# 需求：输出 我的年龄是18岁
print("我的年龄是%d岁" % age)

height = 170.6
print("我的身高%f cm" % height)
# %.nf保留n位小数
print("我的身高%.2f cm" % height)

print("我的名字是%s,年龄是%d,身高是%.2f cm" % (name, age, height))

# 输出50%
print('及格人数占比为%d%%' % 50)

# python3.6版本开始支持f-string ，占位符统一使用{}占位
print(f"我的名字是{name}，年龄是{age}，身高是{height}cm")