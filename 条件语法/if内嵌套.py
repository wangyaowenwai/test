# 开发者: wang
# 开发时间：2021/12/2 0002 15:23
# 或者 if
# money = int(input('请输入你的金额'))
# if money >= 100 or money < 90:
#     print('金额为1', money)
# elif money >= 89 or money <= 80:
#     print('金额为2', money)
# else:
#     print('金额为3', money)

a = 10
b = 20
# print中使用if判断条件输出
print(str(a)+'大于'+str(b) if a >= b else str(b)+'大于'+str(a))

member = input('您是会员吗？是(y)否(n)')
money = int(input('请输入你的消费金额'))
if member == 'y':
    if money >= 1000:
        print('打五折')
    elif money >= 900:
        print('打六折')
    elif money >= 800:
        print('打七折')
    elif money >= 700 or money >= 200:
        print('打八折')
    else:
        print('打九折')

else:
    print('可以享受9.9折')
