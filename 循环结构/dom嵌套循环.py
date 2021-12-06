# 开发者: wang
# 开发时间：2021/12/6 0006 16:04
# 嵌套循环 双for
# 第一层循环是输出多少行 第二层循环是每行多少个

for item in range(1, 10):
    #  第一层循环打印的是 行数多少行
    for ite in range(1, item + 1):
        # print('*' + str(item) + str(ite), end=' ')  # 不换行 直角三角形
        print(str(item) + '*' + str(ite) + '=' + str(item * ite), end=' ')
    print()  # 第二层循环换行
