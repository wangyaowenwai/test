# 开发者: wang
# 开发时间：2021/12/1 0001 16:21
# 布尔运算符


print('and 就是 JavaScript 中的 &&  需要满足全部条件 只要有一方为false 就为 false')
a, b = 1, 2
print(a == 1 and b == 2)  # True
print(a == 2 and b == 2)  # False
print('or 就是 JavaScript 中的 || 或者 只需要一方满足条件')
print(a == 2 or b == 2)  # True
print(a == 1 and b == 2)  # True

print('---------------not 取反对bool f不是true  为 false-----------------')
f = True
g = False
print(not f)
print(not g)

print('---------------in 与not in----------------')
#  in 表示 存在吗  not in 表示 不存在吗
s = 'holloword'
print('w' in s)  # 意思就是说 w 在 s中存在吗 存在 True 不存在 False
print('p' in s)  # False

print('w' not in s)  # 意思 w在 s 中 不存在吗 不确定的意思 是有的 所以 打印的是 False
print('b' not in s)  # True
