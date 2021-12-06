# 开发者: wang
# 开发时间：2021/12/1 0001 17:47
# 测试对象的布尔值
print('------------------以下对象的布尔值为False---------------------')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合
# g = [1]
# g.append(12)
# print(g)
print('-------------------其他对象的布尔值为True-----------------------')
print(bool(15))
print(bool(True))
print(bool('helloword'))