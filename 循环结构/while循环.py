# 开发者: wang
# 开发时间：2021/12/6 0006 13:44
# Python 中的循环 while,for in
a = 1
# 判断条件表达式
# while a <= 10:  # 条件体
#     # 循环体
#     print(a)
#     a += 1

# 计算1到100之间的偶数的和
sun = 0
while a <= 100:
    if a % 2 == 0:  # not bool(a%2)
        sun += a
    a += 1

print('1到100的偶数之和是', sun)
