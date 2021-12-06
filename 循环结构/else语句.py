# 开发者: wang
# 开发时间：2021/12/6 0006 15:32

# for 中使用else当条件执行完成时 进入else
for item in range(1, 4):
    paw = input('请输入您的密码:')
    if paw == '9899':
        print('登录成功')
        break
    else:
        print('密码不正确')
else:
    print('您已经输入三次请稍后重试')

# while 循环中的 else
a = 0
while a < 3:
    pad = input('请输入您的密码:')
    if pad == '22121':
        print('登录成功')
        break
    else:
        print('密码不正确')
    a += 1
# 下面的else 是当 a == 3的时候会进来 你也可以看做循环结束后进来
else:
    print('您已经输入三次请稍后重试')
