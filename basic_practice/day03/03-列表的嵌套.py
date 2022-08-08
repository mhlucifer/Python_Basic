school_names =[['清华大学', '北京大学'],
               ['南开大学', '天津大学', '天津师范大学'],
               ['山东大学', '中国海洋大学']]
print(school_names[1])  # ['南开大学', '天津大学', '天津师范大学']
print(school_names[1][1])  # 天津大学
print(school_names[1][1][1])  # 津

# 山东大学
print(school_names[2][0])

for schools in school_names:
    # print(schools)  # 列表
    for name in schools:
        print(name)

