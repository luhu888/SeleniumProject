# -*- coding: utf-8 -*-
# __author__=luhu
"""
    close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
    当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。
    语法
    fileObject.close();
    参数
    无
    返回值
    该方法没有返回值。
"""


def my_close():
    fo = open("tmp/foo.txt", "wb")
    print("文件相对路径名为: ", fo.name)
    # 关闭文件
    fo.close()


"""
    flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
    一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
    语法
    fileObject.flush();
    参数
    无
    返回值
    该方法没有返回值。
"""


def my_flush():
    fo = open("tmp/foo.txt", "wb")
    print("文件相对路径名为: ", fo.name)
    fo.flush()      # 刷新缓存区
    fo.close()      # 关闭文件


"""
    fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作。 
    语法    
    fileObject.fileno(); 
    参数
    无    
    返回值
    返回文件描述符。
"""


def my_fileno():
    fo = open("tmp/foo.txt", "wb")
    print("文件相对路径名为: ", fo.name)
    fid = fo.fileno()
    print("文件描述符为: ", fid)
    fo.close()  # 关闭文件


"""
    isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。    
    语法
    fileObject.isatty(); 
    参数
    无  
    返回值
    如果连接到一个终端设备返回 True，否则返回 False。
"""


def my_isatty():
    fo = open("tmp/foo.txt", "wb")
    print("文件相对路径名为: ", fo.name)
    ret = fo.isatty()
    print("返回值：", ret)
    fo.close()


"""
    Python 3 中的 File 对象不支持 next() 方法。 Python 3 的内置函数 next() 通过迭代器调用 __next__() 方法返回下一项。 在循环中，next()方法
    会在每次循环中调用，该方法返回文件的下一行，如果到达结尾(EOF),则触发 StopIteration
    语法
    next(iterator[,default])
    参数
    无
    返回值
    返回文件下一行。
"""


def my_next():
    fo = open("tmp/runoob.txt", "r", encoding='utf-8')
    print("文件名为: ", fo.name)
    for index in range(5):
        line = next(fo)
        print("第 %d 行 - %s" % (index, line))
    fo.close()


"""
    read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有
    语法
    fileObject.read(); 
    参数
    size -- 从文件中读取的字节数。
    返回值
    返回从字符串中读取的字节。
"""


def my_read():
    fo = open("tmp/runoob.txt", "r+", encoding='utf-8')
    print("文件名为: ", fo.name)
    line = fo.read(10)
    print("读取的字符串: %s" % line)
    fo.close()


"""
    readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
    语法
    fileObject.readline(); 
    参数
    size -- 从文件中读取的字节数。
    返回值
    返回从字符串中读取的字节。
"""


def my_readline():
    fo = open("tmp/runoob.txt", "r+", encoding='utf-8')
    print("文件名为: ", fo.name)
    line = fo.readline()
    print("读取第一行 %s" % line)
    line = fo.readline(5)
    print("读取的字符串为: %s" % line)
    fo.close()


"""
    readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。 如果碰
    到结束符 EOF 则返回空字符串。
    如果碰到结束符 EOF 则返回空字符串。
    语法
    fileObject.readlines( );
    参数
    无。
    返回值
    返回列表，包含所有的行。
"""


def my_readlines():
    fo = open("tmp/runoob.txt", "r", encoding='utf-8')
    print("文件名为: ", fo.name)
    for line in fo.readlines():  # 依次读取每行
        line = line.strip()      # 去掉每行头尾空白
        print("读取的数据为: %s" % line)

    fo.close()


"""
    seek() 方法用于移动文件读取指针到指定位置。
    语法
    fileObject.seek(offset[, whence])
    参数
    offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始
    算起，2代表从文件末尾算起。    
    返回值
    该函数没有返回值。
"""


def my_seek():
    fo = open("tmp/foo1.txt", "r+", encoding='utf-8')
    print("文件名为: ", fo.name)
    line = fo.readline()
    print("读取的数据为: %s" % line)
    # 重新设置文件读取指针到开头
    fo.seek(0, 2)
    line = fo.readline()
    print("读取的数据为: %s" % line)
    # 关闭文件
    fo.close()


"""
    tell() 方法返回文件的当前位置，即文件指针当前位置。    
    语法
    fileObject.tell(offset[, whence])
    参数
    无
    返回值
    返回文件的当前位置。
"""


def my_tell():
    fo = open("tmp/foo1.txt", "r+", encoding='utf-8')
    print("文件名为: ", fo.name)
    line = fo.readline()
    print("读取的数据为: %s" % line)
    # 获取当前文件位置
    pos = fo.tell()
    print("当前位置: %d" % pos)


"""
    truncate() 方法用于从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有
    字符被删除，其中 Widnows 系统下的换行代表2个字符大小。 
    语法
    fileObject.truncate( [ size ])
    参数
    size -- 可选，如果存在则文件截断为 size 字节。
    返回值
    该方法没有返回值。
"""


def my_truncate():
    fo = open("tmp/foo1.txt", "r+", encoding='utf-8')
    print("文件名: ", fo.name)
    fo.truncate(10)
    line = fo.read()
    print("读取数据: %s" % line)
    # 关闭文件
    fo.close()


"""
    write() 方法用于向文件中写入指定字符串。
    在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
    语法
    fileObject.write( [ str ])
    参数
    str -- 要写入文件的字符串。
    返回值
    该方法没有返回值。
"""


def my_write():
    fo = open("tmp/runoob.txt", "r+")
    print("文件名: ", fo.name)
    str = "6:www.runoob.com\n"
    # 在文件末尾写入一行
    fo.seek(0, 2)
    line = fo.write(str)
    # 读取文件所有内容
    fo.seek(0, 0)
    for index in range(6):
        line = next(fo)
        print("文件行号 %d - %s" % (index, line))
    # 关闭文件
    fo.close()


"""
    writelines() 方法用于向文件中写入一序列的字符串。
    这一序列字符串可以是由迭代对象产生的，如一个字符串列表。   
    换行需要制定换行符 \n。  
    语法 
    fileObject.writelines( [ str ])
    参数
    str -- 要写入文件的字符串序列。  
    返回值
    该方法没有返回值。
"""


def my_writelines():
    fo = open("tmp/test.txt", "w", encoding='utf-8')
    print("文件名为: ", fo.name)
    seq = ["菜鸟教程 1\n", "菜鸟教程 2"]
    fo.writelines(seq)
    fo.close()


def getfile_fix(filename):      # 获取文件后缀
    name = filename[filename.rfind('.') + 1:]
    print(name)


if __name__ == '__main__':
    # my_close()
    # my_fileno()
    # my_isatty()
    # my_next()
    # my_read()
    # my_readline()
    # my_readlines()
    # my_seek()
    # my_tell()
    # my_truncate()
    # my_write()
    my_writelines()
    getfile_fix('runoob.txt')

















































