# 开发者: wang
# 开发时间：2021/11/27 0027 14:42
name = '张三'
age = 20

# print('我叫' + name + '今年' + age)  # 不转类型 报错 can only concatenate str (not "int") to str
print('我叫' + name + '今年' + str(age))  # 如果不转类型这里就会报错 str 类型的 不能 与 int 类型 的值 合并

print('-----------------------str()将其他类型转成str类型-------------------------------')

a = 10
b = 1.1
c = False
d = 19.3
e = 'hello'

print(str(a), str(b), str(c))  # 转成str
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))  # 说明转换是对的

print('-----------------------int()将其他类型转成int类型-------------------------------')

print(int(d))  # 当浮点型 转换成int 类型时 只会截取 前面的整数部分 打印 19
# print(int(e))  # 这里 会报错 文字不能转换 为 int 类型 str 必须为整数 只要是非整数就会报错
print(int(c))  # 布尔类型 转换 成 int 之前就说过了 False = 0 True = 1 所以 在转int的 时候 False 就打印为0

print('-----------------------float()将其他类型转成float类型-------------------------------')

print(float(a))  # 整数转浮点型 加小数点 10.0
print(float(b))  # 这里 浮点型转 浮点型肯定是一样的
print(float(c))  # 这里和int一样True 代表 1 False 代表 0 所以 当转成浮点型的时候 只是在后面 加了小数点 所以 True = 1.0 False = 0.0
# print(float(e))  # 这里肯定是会报错的 文字是不可能转正浮点型的


# codinng:utf-8 中文编码声明


"""
我是多行注释
"""