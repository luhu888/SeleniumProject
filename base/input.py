# coding=utf-8
# author:luhu
from pip._vendor.distlib.compat import raw_input

content = input('Enter any content: ')   # input方法很矫情，要求输入的数据类型一定要正确，字符串输入必须加引号，否则会报错
print('Your input is %r' % content)
content2 = raw_input('Enter any content2: ')  # 这时可以使用raw_input方法输入任何类型都可以
print('Your input is %r' % content2)
