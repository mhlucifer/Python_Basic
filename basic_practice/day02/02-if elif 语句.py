score = eval(input('请输入你的成绩'))
if score >= 90:
    print('优秀')
elif (score >= 80) and score < 90:
    print('良好')
elif score >= 60:
    print('及格')
# 想要执行这个判断的前提，前边两个都不满足才行，所以score一定小于80
else:
    print('不及格')

