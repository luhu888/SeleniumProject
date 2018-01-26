# -*- coding: utf-8 -*-
# __author__=luhu
from collections import deque


def queue_list():        # append添加在列表尾部，popleft取出最左边的值
    queue = deque(["Eric", "John", "Michael"])       # 双向队列
    new_queue = queue.copy()    # 浅拷贝
    queue.append("Terry")     # 往右边添加一个元素
    queue.appendleft("Graham")  # 往左边添加一个元素
    queue.popleft()      # 获取最左边一个元素，并在队列中删除
    queue.pop()          # 获取最右边一个元素，并在队列中删除
    # queue.clear()      # 清空队列
    queue.extend([4, ])    # 从队列右边扩展一个列表的元素
    print(type(queue))
    print(queue.count('Michael'))        # 返回指定元素的出现次数
    print("new_queue:", new_queue, "queue:", queue)
    try:
        print('Michael的索引位置为：', queue.index("Michael", 3, 5))        # 查找某个元素的索引位置
    except ValueError:
        print("Michael不在索引区间内")
    queue.insert(-5, '哈哈')   # 索引位置超出范围时，默认放在最后，或开始（看正序插，还是倒序插）
    print('插入后的queue为：', queue)
    try:
        queue.remove('head')
        print(queue)
    except ValueError:
        print("要删除的元素不存在")
    queue.reverse()    # 队列反转
    print("队列反转后为：", queue)
    queue.rotate(3)      # 把右边元素放到左边,指定次数，默认1次
    print("右边元素放到左边3次后：", queue)


if __name__ == '__main__':
    queue_list()
