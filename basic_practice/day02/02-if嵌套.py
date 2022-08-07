money = int(input('请输入你拥有的零钱'))

if money >= 2:
    print('我上车了')
    seat = int(input('车上空盒的个数：'))
    if seat > 1:
        print('有座位')
    else:
        print('没有座位')
else:
    print('没钱，只能走路')
