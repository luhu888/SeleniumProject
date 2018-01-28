# coding=utf-8
# author:luhu


def sequence_enumerate():       # 在sequence(序列)中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
    list = ['tic', 'tac', 'toe']
    tuple = ('luhu', 234, 'erfda')
    for j, w in enumerate(tuple):
        print(j, w)
        print(type(tuple))
    for i, v in enumerate(list):
        print(i, v)


def sequence_zip():      # 同时遍历两个或更多的序列，可以使用 zip() 组合
    list = ['tic', 'tac', 'toe']
    tuple = ('luhu', 234, 'hello')
    for l, t in zip(list, tuple):
        print('{}, {}'.format(l, t))
        print('%s  %s' % (l, t))      # 格式化，效果与format一致


if __name__ == '__main__':
    # sequence_enumerate()
    sequence_zip()

















