# -*- coding: utf-8 -*-
# __author__=luhu
# 运算符
print(2**4)    # 开方，2的4次方
print(77 % 5)   # 取余（取模）返回余数
print(43//5)    # 整除取整商

# 比较运算符
print(4 == 5)    # 比较两数是否相等
print(4 != 5)    # 比较两数是否不等
print(4 >= 5)
print(4 <= 5)
print(4 < 5)
print(4 > 5)

# 赋值运算符
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a   # 等效于c=c+a
print("2 - c 的值为：", c)

c *= a    # 等效于 c = c * a
print("3 - c 的值为：", c)

c /= a    # 等效于 c = c / a
print("4 - c 的值为：", c)

c = 2
c %= a    # 等效于 c = c % a
print("5 - c 的值为：", c)

c **= a  # 等效于 c = c ** a
print("6 - c 的值为：", c)

c //= a   # 等效于 c = c // a
print("7 - c 的值为：", c)

# 位运算符
a = 0b00111100  # 60 = 0011 1100
b = 0b00001101  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("1 - c 的值为：", bin(c))

c = a | b  # 61 = 0011 1101
print("2 - c 的值为：", bin(c))

c = a ^ b  # 49 = 0011 0001
print("3 - c 的值为：", bin(c))

c = ~a  # -61 = 1100 0011
print("4 - c 的值为：", bin(c))

c = a << 2  # 240 = 1111 0000
print("5 - c 的值为：", bin(c))

c = a >> 2  # 15 = 0000 1111
print("6 - c 的值为：", bin(c))

# 逻辑运算符
a = 10
b = 20

if a and b:
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

a = 0    # 修改变量 a 的值
if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not a and b:
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

# 成员运算符,Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
a = 10
b = 20
list = [1, 2, 3, 4, 5]
tuple = ('hha', 324, 32)
string = 'technology'
if a in list:
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if b not in list:
    print("2 - 变量 b 不在给定的列表list 中")
else:
    print("2 - 变量 b 在给定的列表list 中")

# 修改变量 a 的值
a = 32
if a in tuple:
    print("3 - 变量 a 在给定的元组tuple 中")
else:
    print("3 - 变量 a 不在给定的元组tuple 中")

a = 'tech'
if a in string:
    print('4 -变量 a 在给定的字符串string 中')
else:
    print('4 -变量 a 不在在给定的字符串string 中')

# 身份运算符，身份运算符用于比较两个对象的存储单元，即比较他们的内存地址，id() 方法获取他们的内存地址
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
a = 20
b = 20

if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if id(a) == id(b):
    print("2 - a 和 b 有相同的标识", id(a))
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")








































