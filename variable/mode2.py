# 开发者: wang
# 开发时间：2021/11/24 0024 11:12
name = '王德发'
print(name)
name = '李云龙'
print(name)
print('标识', id(name))  # 内存 地址 name 指向的就是id 的内存地址
print('类型', type(name))
print('值', name)

# 当一个变量 重新赋值 的时候 会指向一个新的内存地址


# 比如 第一个 变量 指向的地址 是 id为 11111111的地址
# 当 name 被重新赋值 的时候 name 指向的地址 就不会是 id为 1111111的地址而是另外一个新的内存地址 同时 第一个 地址 会成为 内存垃圾


# 跟JavaScript 一样 Python 的数据类型 也是 分为四种常用的类型

# 整数类型 int  98
# 浮点数类型 float 3.1426
# 布尔类型 bool true false
# 字符串类型 str  '人生苦短我学Python'


# 整数类型 包括 整数 负数 0
a = 1,
b = -1,
c = 0,
print(a)
print(b)
print(c)
