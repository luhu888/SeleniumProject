# -*- coding: utf-8 -*-
# __author__=luhu
# 数据类型，数字函数
from math import ceil, exp, fabs, floor, log

import math
from random import choice, randrange, random, shuffle, uniform, randint, sample

a = 12
b = 23.123
c = -45
d = 100
e = (1, 2, 4, 5, 45, 46, 40)
f = [20, 16, 10, 5]
g = 'abcdefghijklmnopq'
print(float(a))     # 不支持复数转换为整数或浮点数

h = 8+5j
print("h的实部是：", h.real, "h的虚部是：", h.imag)

print(complex(a))    # 将a转换为一个复数，实数部分为a，虚数部分为0
print(complex(a, b))    # 将a，b转换到一个复数，实数部分为a，虚数部分为b
print('c的绝对值为：', abs(c))
print('b的上入整数为：', ceil(b))   # 如math.ceil(4.1) 返回 5
print('返回e的x次幂', exp(13))
print('c的绝对值为：', fabs(c))    # 与abs()的区别:fabs() 函数只对浮点型跟整型数值有效; abs() 还可以运用在复数中abs() 是内置函数。 fabs() 函数在 math 模块中定义
print('b的下舍整数为：', floor(b))  # 如math.floor(4.9)返回 4
print('e的自然对数', log(math.e))
print('d的以10为基数的对数', log(d, 10))
print('d的以10为基数的对数', math.log10(d))    # 效果同上
print("max(80, 100, 1000) : ", max(80, 100, 1000))   # 返回最大值
print("max(a, b, c) : ", max(a, int(b), c))
print("min(a, b, c) : ", min(a, int(b), c))
print(math.modf(b))      # 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
print(pow(12, 3))   # 12的3次方

print(round(3.123545, 4))      # 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。国家标准也已经规定使用 "4舍6入5看齐,奇进偶不进" 取代"四舍五入".

print(math.sqrt(45))                 # 返回数字x的平方根
print(choice(e))    # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
print(randrange(2, 1000, 2))    # randrange ([start,] stop [,step])从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
print(random())   # 随机生成下一个实数，它在[0,1)范围内。

shuffle(f)    # 将列表随机排序后打印
print(f)

print(uniform(2, 99))     # 随机生成下一个实数，它在[x,y]范围内。
print(randint(4, 77))  # 随机生一个整数int类型，可以指定这个整数的范围)

list = sample(g, 4)    # 可以从指定的序列中，随机的截取指定长度的片断，不修改原序列。
strs = ''.join(list)
print(strs)

print()
print()
print()
print()




































































