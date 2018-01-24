# -*- coding: utf-8 -*-
# __author__=luhu
import itertools
from numpy.core.defchararray import capitalize, isalpha

var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])
print("已更新字符串 : \n", var1[:6] + 'Runoob!'*2)     # 字符串拼接

# 字符串中的转义字符
#   \(在行尾时)	    续行符
#   \\	            反斜杠符号
#   \'	            单引号
#   \"          	双引号
#   \a	            响铃
#   \b	            退格(Backspace)
#   \e	            转义
#   \000	        空
#   \n	            换行
#   \v	            纵向制表符
#   \t	            横向制表符
#   \r	            回车
#   \f	            换页
#   \oyy	        八进制数，yy代表的字符，例如：\o12代表换行
#   \xyy	        十六进制数，yy代表的字符，例如：\x0a代表换行
#   \other	        其它的字符以普通格式输出

# 字符串运算符
#   +	            字符串连接	a + b 输出结果： HelloPython
#   *	            重复输出字符串	a*2 输出结果：HelloHello
#   []	            通过索引获取字符串中字符	a[1] 输出结果 e
#   [ : ]	        截取字符串中的一部分	a[1:4] 输出结果 ell
#   in	            成员运算符 - 如果字符串中包含给定的字符返回 True	H in a 输出结果 1
#   not in	        成员运算符 - 如果字符串中不包含给定的字符返回 True	M not in a 输出结果 1
#   r/R	            原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	print r'\n' prints \n 和 print R'\n' prints \n
#   % 格式字符串	请看下例。
a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if "H" in a:
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')
print("我叫%s，今年%d岁!" % ('小明', 100))
# 字符串格式化
#   %c	    格式化字符及其ASCII码
#   %s	    格式化字符串
#   %d	    格式化整数
#   %u	    格式化无符号整型
#   %o	    格式化无符号八进制数
#   %x	    格式化无符号十六进制数
#   %X	    格式化无符号十六进制数（大写）
#   %f	    格式化浮点数字，可指定小数点后的精度
#   %e	    用科学计数法格式化浮点数
#   %E	    作用同%e，用科学计数法格式化浮点数
#   %g	    %f和%e的简写
#   %G	    %f 和 %E 的简写
#   %p	    用十六进制数格式化变量的地址

# 格式化操作符辅助指令
#   *	    定义宽度或者小数点精度
#   -	    用做左对齐
#   +	    在正数前面显示加号( + )
#   <sp>	在正数前面显示空格
#   #	    在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
#   0	    显示的数字前面填充'0'而不是默认的空格
#   %	    '%%'输出一个单一的'%'
#   (var)	映射变量(字典参数)
#   m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)

str = "this is string example from runoob....wow!!!"
print("字符串的第一个字母变大写: ", capitalize(str))   # 将字符串的第一个字母变成大写
# 返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充
str = "[www.runoob.com]"
print("str.center(40, '*') : \n", str.center(40, '*'))

'''
    str.count(sub, start= 0,end=len(string))
    sub -- 搜索的子字符串
    start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
    end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
'''
str = "www.runoob.com"
sub = 'o'
print("str.count('o') : ", str.count(sub))
sub = 'run'
print("str.count('run', 0, 10) : ", str.count(sub, 0, 10))

"""
    bytes.decode(encoding="utf-8", errors="strict")
    参数
    encoding -- 要使用的编码，如"UTF-8"。
    errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 
    其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过
     codecs.register_error() 注册的任何值。
"""
str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('gbk', 'strict'))

"""
    endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
    可选参数"start"与"end"为检索字符串的开始与结束位置。
    语法
    str.endswith(suffix[, start[, end]])
    参数
    suffix -- 该参数可以是一个字符串或者是一个元素。
    start -- 字符串中的开始位置。
    end -- 字符中结束位置。
"""
Str = 'Runoob example....wow!!!'
suffix = '!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 20))
suffix = 'run'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 19))

"""
    expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
    语法
    str.expandtabs(tabsize=8)
    参数
    tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数。
    返回值
    该方法返回字符串中的 tab 符号('\t')转为空格后生成的新字符串。
"""
str = "this is\tstring example....wow!!!"
print("原始字符串: " + str)
print("替换 \\t 符号: " +str.expandtabs())
print("使用16个空格替换 \\t 符号: " +str.expandtabs(16))

"""
    描述
    find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
    则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。
    如果不包含索引值，返回-1。
    语法
    str.find(str, beg=0, end=len(string))
    参数
    str -- 指定检索的字符串
    beg -- 开始索引，默认为0。
    end -- 结束索引，默认为字符串的长度。
    返回值
    如果包含子字符串返回开始的索引值，否则返回-1。
"""
str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.find(str2))
print(str1.find(str2, 5))
print(str1.find(str2, 10))

"""
    index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
    则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
    语法
    str.index(str, beg=0, end=len(string))
    参数
    str -- 指定检索的字符串
    beg -- 开始索引，默认为0。
    end -- 结束索引，默认为字符串的长度。
    返回值
    如果包含子字符串返回开始的索引值，否则抛出异常。
"""
str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.index(str2))
print(str1.index(str2, 5))
# print(str1.index(str2, 10))

"""
    isalnum() 方法检测字符串是否由字母和数字组成。
    语法
    str.isalnum()
    参数
    无。
    返回值
    如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
"""
str = "runoob2016"  # 字符串没有空格
print(str.isalnum())
str = "www.runoob.com"
print(str.isalnum())

"""
    isalpha() 方法检测字符串是否只由字母组成。
    语法
    str.isalpha()
    参数
    无。
    返回值
    如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
"""
str = "runoob"
print(isalpha(str))
str = "Runoob example....wow!!!"
print(str.isalpha())

"""
    isdigit() 方法检测字符串是否只由数字组成。
    语法
    str.isdigit()
    参数
    无。
    返回值
    如果字符串只包含数字则返回 True 否则返回 False。
"""
str = "123456"
print(str.isdigit())
str = "Runoob example....wow!!!"
print(str.isdigit())

"""
    islower() 方法检测字符串是否由小写字母组成。
    str.islower()
    参数
    无。
    返回值
    如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
"""
str = "RUNOOB example....wow!!!"
print(str.islower())

str = "runoob example....wow!!!"
print(str.islower())

"""
    isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
    注：定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可，具体可以查看本章节例子。
    语法
    str.isnumeric()
    参数
    无。
    返回值
    如果字符串中只包含数字字符，则返回 True，否则返回 False
"""
str = "runoob2016"
print(str.isnumeric())
str = "23443434"
print(str.isnumeric())
"""
    str.isdecimal () 与str.isdigit()的区别
    str.isdecimal() 函数只对十进制数返回 True，同时函数 str.isdigit() 对其他 unicode 支持的字符返回 True。
"""
line = '-' * 37
print(line)
print("|    №   | isdigit | isdecimal | chr")
print(line)
for number in itertools.chain(range(1000), range(4969, 4978), range(8304, 11000)):
    char = chr(number)
    if char.isdigit() or char.isdecimal():
        print('| {0:>6} | {1:^7} | {2:^9} | {3:3} '.format(
            number,
            '+' if char.isdigit() else '-',
            '+' if char.isdecimal() else '-',
            char
        )
    )

"""
    isspace() 方法检测字符串是否只由空白字符组成。
    语法  
    str.isspace()
    参数
    无。
    返回值
    如果字符串中只包含空格，则返回 True，否则返回 False.
"""
str = "       "
print(str.isspace())

str = "Runoob example....wow!!!"
print(str.isspace())

"""
    istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
    语法
    str.istitle()
    参数
    无。
    返回值
    如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
"""
str = "This Is String Example...Wow!!!"
print(str.istitle())
str = "This is string example....wow!!!"
print(str.istitle())

"""
    isupper() 方法检测字符串中所有的字母是否都为大写。
    语法
    str.isupper()
    参数
    无。
    返回值
    如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
"""
str = "THIS IS STRING EXAMPLE....WOW!!!"
print(str.isupper())
str = "THIS is string example....wow!!!"
print(str.isupper())

"""
    join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。    
    语法
    str.join(sequence)
    参数
    sequence -- 要连接的元素序列。
    返回值
    返回通过指定字符连接序列中元素后生成的新字符串。
"""
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b")     # 字符串序列
print(s1.join(seq))
print(s2.join(seq))

"""
    len() 方法返回对象（字符、列表、元组等）长度或项目个数。
    语法
    len( s )
    参数
    s -- 对象。
    返回值
    返回对象长度。
"""
str = "runoob"
print(len(str))             # 字符串长度
lst = [1, 2, 3, 4, 5]
print(len(lst))               # 列表元素个数

"""
    ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
    语法
    str.ljust(width[, fillchar])
    参数
    width -- 指定字符串长度。
    fillchar -- 填充字符，默认为空格。
    返回值
    返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
"""
str = "Runoob example....wow!!!"
print(str.ljust(50, '*'))

"""
    lower() 方法转换字符串中所有大写字符为小写。
    
    语法
    str.lower()
    参数
    无。
    返回值
    返回将字符串中所有大写字符转换为小写后生成的字符串。
 """
str = "Runoob EXAMPLE....WOW!!!"
print(str.lower())

"""
    lstrip() 方法用于截掉字符串左边的空格或指定字符。
    语法
    str.lstrip([chars])
    参数
    chars --指定截取的字符。
    返回值
    返回截掉字符串左边的空格或指定字符后生成的新字符串。
"""
str = "     this is string example....wow!!!     "
print(str.lstrip())
str = "88888888this is string example....wow!!!8888888"
print(str.lstrip('8'))

"""
    maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，
    第二个参数也是字符串表示转换的目标。两个字符串的长度必须相同，为一一对应的关系。
    注：Python3.4已经没有string.maketrans()了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()
    语法
    str.maketrans(intab, outtab)
    参数
    intab -- 字符串中要替代的字符组成的字符串。
    outtab -- 相应的映射字符的字符串。
    返回值
    返回字符串转换后生成的新字符串。
"""
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print(str.translate(trantab))

"""
    max() 方法返回字符串中最大的字母。
    语法
    max(str)
    参数
    str -- 字符串。
    返回值
    返回字符串中最大的字母。
"""
str = "runoob"
print("最大字符: " + max(str))

"""
    min() 方法返回字符串中最小的字母。
    语法   
    min(str)
    参数
    str -- 字符串。
    返回值
    返回字符串中最小的字母。
"""
str = "runoob"
print("最小字符: " + min(str))

"""
    replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
    语法
    str.replace(old, new[, max])
    参数
    old -- 将被替换的子字符串。
    new -- 新字符串，用于替换old子字符串。
    max -- 可选字符串, 替换不超过 max 次
    返回值
    返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
"""
str = "www.w3cschool.cc"
print("菜鸟教程旧地址：", str)
print("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
str = "this is string example....wow!!!"
print(str.replace("is", "was", 1))
print(str.replace("is", "was", 3))

"""
    rfind() 类似于 find()函数，不过是从右边开始查找,返回字符串最后一次出现的位置，如果没有匹配项则返回-1。 
    语法
    str.rfind(str, beg=0 end=len(string))
    参数
    str -- 查找的字符串
    beg -- 开始查找的位置，默认为0
    end -- 结束查找位置，默认为字符串的长度。
    返回值
    返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
"""
str1 = "this is really a string example....wow!!!"
str2 = "is"
print(str1.rfind(str2))
print(str1.rfind(str2, 0, 10))
print(str1.rfind(str2, 10, 0))
print(str1.find(str2))
print(str1.find(str2, 0, 10))
print(str1.find(str2, 10, 0))

"""
    rindex() 类似于 index()，不过是从右边开始,返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，
    你可以指定可选参数[beg:end]设置查找的区间。
    语法
    str.rindex(str, beg=0 end=len(string))
    参数
    str -- 查找的字符串
    beg -- 开始查找的位置，默认为0
    end -- 结束查找位置，默认为字符串的长度。
    返回值
    返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常。
"""
str1 = "this is really a string example....wow!!!"
str2 = "is"
print(str1.rindex(str2))
# print(str1.rindex(str2, 10))

"""
    rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
    语法
    str.rjust(width[, fillchar])
    参数
    width -- 指定填充指定字符后中字符串的总长度.
    fillchar -- 填充的字符，默认为空格。
    返回值
    返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
"""
str = "this is string example....wow!!!"
print(str.rjust(50, '*'))

"""
    rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
    语法
    str.rstrip([chars])
    参数
    chars -- 指定删除的字符（默认为空格）
    返回值
    返回删除 string 字符串末尾的指定字符后生成的新字符串。
"""
str = "     this is string example....wow!!!     "
print(str.rstrip())
str = "*****this is string example....wow!!!*****"
print(str.rstrip('*'))

"""
    split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
    语法
    str.split(str="", num=string.count(str)).
    参数
    str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    num -- 分割次数。
    返回值
    返回分割后的字符串列表。
"""
str = "this is string example....wow!!!"
print(str.split())
print(str.split('i', 4))
print(str.split('w'))

"""
    splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
    语法
    str.splitlines([keepends])
    参数
    keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。
    返回值
    返回一个包含各行作为元素的列表。
"""
str = 'ab c\n\nde fg\rkl\r\n'
print(str.splitlines())
print(str.splitlines(True))

"""
    startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
    如果参数 beg 和 end 指定值，则在指定范围内检查。
    语法
    str.startswith(str, beg=0,end=len(string));
    参数
    str -- 检测的字符串。
    strbeg -- 可选参数用于设置字符串检测的起始位置。
    strend -- 可选参数用于设置字符串检测的结束位置。
    返回值
    如果检测到字符串则返回True，否则返回False。
"""
str = "this is string example....wow!!!"
print(str.startswith('this'))
print(str.startswith('string', 8))
print(str.startswith('this', 2, 4))

"""
    strip() 方法用于移除字符串头尾指定的字符（默认为空格）,相当于在字符串上执行 lstrip()和 rstrip()
    语法
    str.strip([chars]);
    参数
    chars -- 移除字符串头尾指定的字符。
    返回值
    返回移除字符串头尾指定的字符生成的新字符串。
"""
str = "*****this is string example....wow!!!*****"
print(str.strip('*'))

"""
    swapcase() 方法用于对字符串的大小写字母进行转换。
    语法
    str.swapcase();
    参数
    无
    返回值
    返回大小写字母转换后生成的新字符串。
"""
str = "this is string example....wow!!!"
print(str.swapcase())
str = "This Is String Example....WOW!!!"
print(str.swapcase())

"""
    title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
    语法
    str.title();
    参数
    无。
    返回值
    返回"标题化"的字符串,就是说所有单词都是以大写开始。
"""
str = "this is string example from runoob....wow!!!"
print(str.title())

"""
    translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。  
    语法
    str.translate(table[, deletechars]); 
    bytes.translate(table[, delete])    
    bytearray.translate(table[, delete]) 
    参数
    table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
    deletechars -- 字符串中要过滤的字符列表。
    返回值
    返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，剩下的字符要按照table中给出的映射来进行映射 。
"""
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表
str = "this is string example....wow!!!"
print(str.translate(trantab))

"""
    upper() 方法将字符串中的小写字母转为大写字母。
    语法
    str.upper()
    参数
    NA。
    返回值
    返回小写字母转为大写字母的字符串。
"""
str = "this is string example from runoob....wow!!!"
print("str.upper() : ", str.upper())

"""
    zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
    语法
    str.zfill(width)
    参数
    width -- 指定字符串的长度。原字符串右对齐，前面填充0。
    返回值
    返回指定长度的字符串。
"""
str = "this is string example from runoob....wow!!!"
print("str.zfill : ", str.zfill(40))
print("str.zfill : ", str.zfill(50))

"""
    isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
    注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
    语法
    str.isdecimal()
    参数
    无
    返回值
    如果字符串是否只包含十进制字符返回True，否则返回False。
"""
str = "runoob2016"
print(str.isdecimal())
str = "23443434"
print(str.isdecimal())



































