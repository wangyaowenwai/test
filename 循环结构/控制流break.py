# 开发者: wang
# 开发时间：2021/12/6 0006 14:52
# break 退出当前循环
for item in range(1, 4):
    pwa = input('请输入您的密码:')
    if pwa == '888':
        print('登录成功')
        break
    else:
        print('密码错误')
