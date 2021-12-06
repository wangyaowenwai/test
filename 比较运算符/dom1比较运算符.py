# 开发者: wang
# 开发时间：2021/12/1 0001 15:51
a, b, c = 10, 20, 30
print('----比较比较运算符 > < >= <= == === != ----------------')
bu = 10
shi = 10
# 当bu=10 和 shi = 10 是 指向的是通一个 id 内存标识所以拿的都是通一内存的值
print('比较值使用')
print(bu == shi)

print('比较对象的标识使用 is')
"""
[{id:1111,type:int,value:10}]
"""
# 这里的对象是指id 指向的内存地址
print(bu is shi)

print(id(bu))
print(id(shi))

# 在不懂 看这里
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(id(list2))
print(id(list1))
print(list2 == list1)  # == 是比较值 True
print(list2 is list1)  # is 是比较id -----》内存地址的标识 False

print('------------------- is not ------------------------------')
# is not 表示   如果 a id = 1000 ,  b id = 1000    a的id不等于b吗  False
print(bu is not shi)
print(list1 is not list2)  # list1 的id 不等于 list2 的id True
