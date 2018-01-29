# -*- coding: utf-8 -*-
# __author__=luhu
"""
os.access() 方法使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。
语法
os.access(path, mode);
参数
path -- 要用来检测是否有访问权限的路径。
mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
os.F_OK: 作为access()的mode参数，测试path是否存在。
os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
返回值
如果允许访问返回 True , 否则返回False。
"""
import os


def my_access():
    ret = os.access("tmp/foo.txt", os.F_OK)
    print("F_OK - 返回值 %s" % ret)
    ret = os.access("tmp/foo.txt", os.R_OK)
    print("R_OK - 返回值 %s" % ret)
    ret = os.access("tmp/foo.txt", os.W_OK)
    print("W_OK - 返回值 %s" % ret)
    ret = os.access("tmp/foo.txt", os.X_OK)
    print("X_OK - 返回值 %s" % ret)


"""
    os.chdir() 方法用于改变当前工作目录到指定的路径。
    语法：
    os.chdir(path)
    参数
    path -- 要切换到的新路径。
    返回值
    如果允许访问返回 True , 否则返回False。
"""


def my_chdir():
    path = "tmp"
    # 查看当前工作目录
    retval = os.getcwd()
    print("当前工作目录为 %s" % retval)
    # 修改当前工作目录
    os.chdir(path)
    # 查看修改后的工作目录
    retval = os.getcwd()
    print("目录修改成功 %s" % retval)


"""
    os.chflags() 方法用于设置路径的标记为数字标记。多个标记可以使用 OR 来组合起来。
    只支持在 Unix 下使用。  
    语法   
    os.chflags(path, flags)
    参数
    path -- 文件名路径或目录路径。
    flags -- 可以是以下值：
    stat.UF_NODUMP: 非转储文件
    stat.UF_IMMUTABLE: 文件是只读的
    stat.UF_APPEND: 文件只能追加内容
    stat.UF_NOUNLINK: 文件不可删除
    stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
    stat.SF_ARCHIVED: 可存档文件(超级用户可设)
    stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
    stat.SF_APPEND: 文件只能追加内容(超级用户可设)
    stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
    stat.SF_SNAPSHOT: 快照文件(超级用户可设)
    返回值
    该方法没有返回值。
"""


def my_chflags():
    path = "tmp/foo.txt"
    # 为文件设置标记，使得它不能被重命名和删除
    flags = os.stat.SF_NOUNLINK
    retval = os.chflags(path, flags)
    print("返回值: %s" % retval)


"""
    os.chmod() 方法用于更改文件或目录的权限。
    Unix 系统可用。 
    语法
    os.chmod(path, mode)
    参数
    path -- 文件名路径或目录路径。
    flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执
    行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。
    stat.S_IXOTH: 其他用户有执行权0o001
    stat.S_IWOTH: 其他用户有写权限0o002
    stat.S_IROTH: 其他用户有读权限0o004
    stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
    stat.S_IXGRP: 组用户有执行权限0o010
    stat.S_IWGRP: 组用户有写权限0o020
    stat.S_IRGRP: 组用户有读权限0o040
    stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
    stat.S_IXUSR: 拥有者具有执行权限0o100
    stat.S_IWUSR: 拥有者具有写权限0o200
    stat.S_IRUSR: 拥有者具有读权限0o400
    stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
    stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
    stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
    stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
    stat.S_IREAD: windows下设为只读
    stat.S_IWRITE: windows下取消只读
    返回值
    该方法没有返回值。
"""


def my_chmod():
    # 假定 /tmp/foo.txt 文件存在，设置文件可以通过用户组执行
    os.chmod("/tmp/foo.txt", os.stat.S_IXGRP)
    # 设置文件可以被其他用户写入
    os.chmod("/tmp/foo.txt", os.stat.S_IWOTH)
    print("修改成功!!")


"""
os.close() 方法用于关闭指定的文件描述符 fd。
语法
os.close(fd);
参数
fd -- 文件描述符。
返回值
该方法没有返回值。
"""


def my_close():
    fd = os.open("tmp/foo.txt", os.O_RDWR | os.O_CREAT)
    #  写入字符串
    os.write(fd, b"This is test")
    # 关闭文件
    os.close(fd)
    print("关闭文件成功!!")


"""
    os.closerange() 方法用于关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略。  
    语法   
    os.closerange(fd_low, fd_high);
    参数
    fd_low -- 最小文件描述符  
    fd_high -- 最大文件描述符   
    该方法类似于：   
    for fd in xrange(fd_low, fd_high):
        try:
            os.close(fd)
        except OSError:
            pass
    返回值
    该方法没有返回值。
"""


def my_closerange():
    fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)
    # 写入字符串
    os.write(fd, b"This is test")
    # 关闭文件
    os.closerange(fd, fd)
    print("关闭文件成功!!")


"""
    os.popen() 方法用于从一个命令打开一个管道。
    在Unix，Windows中有效
    语法 
    os.popen(command[, mode[, bufsize]])
    参数
    command -- 使用的命令。
    mode -- 模式权限可以是 'r'(默认) 或 'w'。
    bufsize -- 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。
    负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，
    它是全缓冲。如果没有改参数，使用系统的默认值。
    返回值
    返回一个文件描述符号为fd的打开的文件对象
"""


def my_popen():
    # 使用 mkdir 命令
    a = 'mkdir nwdir'
    b = os.popen(a, 'r', 1)
    print(b)


"""
    os.removedirs() 方法用于递归删除目录。像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个
    error(它基本上被忽略,因为它一般意味着你文件夹不为空)。
    语法
    os.removedirs(path)
    参数
    path -- 要移除的目录路径
    返回值
    该方法没有返回值
"""


def my_removedirs():
    # 列出目录
    print("目录为: %s" % os.listdir(os.getcwd()))
    # 移除
    # os.removedirs("nwdir")
    # 列出移除后的目录
    print("移除后目录为: %s" % os.listdir(os.getcwd()))


"""
    os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。
    语法
    os.rename(src, dst)
    参数
    src -- 要修改的目录名
    dst -- 修改后的目录名
    返回值
    该方法没有返回值
"""


def my_rename():
    # 列出目录
    print("目录为: %s" % os.listdir(os.getcwd()))
    # 重命名
    try:
        os.rename("uiwx.py", "uiwx2.py")
        print("重命名成功。")
    except FileNotFoundError:
        print("重命名的文件不存在！！！！")
    # 列出重命名后的目录
    print("目录为: %s" % os.listdir(os.getcwd()))


"""
    os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
    语法
    os.rmdir(path)
    参数
    path -- 要删除的目录路径
    返回值
    该方法没有返回值
"""


def my_rmdir():
    # 列出目录
    print("目录为: %s" % os.listdir(os.getcwd()))
    # 删除路径
    os.rmdir("mydir")
    # 列出重命名后的目录
    print("目录为: %s" % os.listdir(os.getcwd()))


if __name__ == '__main__':
    # my_access()
    # my_chdir()
    # my_close()
    # my_closerange()
    # my_popen()
    # my_removedirs()
    # my_rename()
    my_rmdir()



























































