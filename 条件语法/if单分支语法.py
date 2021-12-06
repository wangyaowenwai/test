# 开发者: wang
# 开发时间：2021/12/1 0001 18:23
a = 1000
money = int(input('请输入你需要取出的金额'))
if money <= a:
    a = a - money
    print('取款成功')
    print('您剩余余额' + str(a) + '元')
else:
    print('您的余额不足')

# 写一个案例 输入一个数判断是偶数 还是奇数 注意 能被2整除的是偶数
integer = int(input('请输入你要判断的数字'))
if integer % 2 == 0:
    print(str(integer) + '是一个偶数')
else:
    print(str(integer) + '是一个奇数')
