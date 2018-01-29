# -*- coding: utf-8 -*-
# __author__=luhu
"""
    读和写文件
    open() 将会返回一个 file 对象，基本语法格式如下:
    open(filename, mode)
    filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
    mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
    这个参数是非强制的，默认文件访问模式为只读(r)。
    模式	描述
    r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb	    以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
    r+	    打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+	    以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
    w	    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb	    以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    w+	    打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb+	    以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+	    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
    模式	    r	r+	w	w+	a	a+
    读	        +	+		+		+
    写		        +	+	+	+	+
    创建			    +	+	+	+
    覆盖			    +	+
    指针在开始	+	+	+	+
    指针在结尾					+	+
"""
import pickle


def my_write_file():
    f = open("tmp/foo.txt", "w", encoding='utf-8')    # 打开文件，指定解码格式
    content = u'Python 是一个非常好的语言。\n是的，的确非常好!!\n'
    num = f.write(content)
    print(num)    # 返回写入的字符数。
    # 关闭打开的文件
    f.close()


def my_write_file2():      # 如果要写入一些不是字符串的东西, 那么将需要先进行转换
    f = open("tmp/foo1.txt", "w", encoding='utf-8')
    value = ("www.baidu.com", 14)
    s = str(value)
    f.write(s)
    print(f.tell())    # f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
    f.close()


def my_readlines():     # f.readlines() 将返回该文件中包含的所有行。如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
    f = open("tmp/foo1.txt", "r", encoding='utf-8')
    str = f.readlines()
    print(str)
    f.close()
# 在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
# 当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。


def my_readline():     # 迭代一个文件对象然后读取每行
    f = open("tmp/foo.txt", "r", encoding='utf-8')
    for line in f:
        print(line, end='')
    f.close()


"""
    如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
    from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
    seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    seek(x,1) ： 表示从当前位置往后移动x个字符
    seek(-x,2)：表示从文件的结尾往前移动x个字符
    from_what 值为默认为0，即文件开头
"""


def my_seek():
    f = open('tmp/foo.txt', 'rb+')
    f.write(b'0123456789abcdef')
    f.seek(5)  # 移动到文件的第六个字节
    print(f.read(1))
    f.seek(-3, 2)  # 移动到文件的倒数第三字节
    print(f.read(1))
    f.close()


"""
    python的pickle模块实现了基本的数据序列和反序列化。
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
    基本接口：
    pickle.dump(obj, file, [,protocol])
    有了 pickle 这个对象, 就能对 file 以读取的形式打开:
    x = pickle.load(file)
"""
# pickle模块主要函数的应用举例


def my_pickle():
    dataList = [[1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    dataDic = {0: [1, 2, 3, 4],
               1: ('a', 'b'),
               2: {'c': 'yes', 'd': 'no'}}

    # 使用dump()将数据序列化到文件中, 使用pickle模块将数据对象保存到文件
    fw = open('tmp/data.txt', 'wb')
    # Pickle the list using the highest protocol available.
    pickle.dump(dataList, fw, -1)
    # Pickle dictionary using protocol 0.
    pickle.dump(dataDic, fw)
    fw.close()

    # 使用load()将数据从文件中序列化读出
    fr = open('tmp/data.txt', 'rb')
    data1 = pickle.load(fr)
    print(data1)
    data2 = pickle.load(fr)
    print(data2)
    fr.close()

    # 使用dumps()和loads()举例
    p = pickle.dumps(dataList)
    print(pickle.loads(p))
    p = pickle.dumps(dataDic)
    print(pickle.loads(p))






if __name__ == '__main__':
    # my_write_file()
    # my_readlines()
    # my_readline()
    # my_seek()
    my_pickle()










