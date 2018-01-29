# -*- coding: utf-8 -*-
# __author__=luhu
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数


def fibonacci_series():
    a, b = 0, 1
    while b < 50:
        print(b, end=',')
        a, b = b, a+b
# 第一行包含了一个复合赋值：变量 a 和 b 同时得到新值 0 和 1。最后一行再次使用了
# 同样的方法，可以看到，右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是
# 从左往右的,关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符


if __name__ == '__main__':
    fibonacci_series()















