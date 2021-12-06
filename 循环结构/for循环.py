# 开发者: wang
# 开发时间：2021/12/6 0006 14:13

for item in 'wangbaba':
    print(item)

a = list(range(1, 10))
print(a)

for item in a:
    print('我是range和list的值', item)

for _ in range(1, 10):  # 如果只是单纯的循环 只需要把item 改成_
    print('人生苦短,我学Python', _)

# 计算1到100之间的偶数的和
ob = 0
for it in range(1, 101):  # 这里要写101 因为range 不包含100 所以写101 长度-1
    if it % 2 == 0:
        ob += it
print('1到100的偶数和为', ob)

# 练习 100 到 999 之间的水仙花数
for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print('水仙花数为', item)
