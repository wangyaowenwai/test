# 开发者: wang
# 开发时间：2021/12/2 0002 15:09
performance = int(input('请输入你的成绩'))
if 100 >= performance >= 90:
    print('优秀')
elif 89 >= performance >= 70:
    print('良好')
elif 69 >= performance >= 60:
    print('及格')
else:
    print('不及格')