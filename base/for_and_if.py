# coding=utf-8
# author:luhu

result = 88
if result >= 90:    # 分支和循环，分支就用if，循环就用for
    print '优秀'
elif 80 <= result < 90:
    print '良好'
elif 60 <= result < 80:
    print '一般'
elif result < 60:
    print '不及格'
strings = 'hello python'

for i in strings:
    print i

for i in range(1, 10, 2):    # range(start，end，scan)表示一连串数，start表示起始数，end表示结束位置，scan表示步长
    print i