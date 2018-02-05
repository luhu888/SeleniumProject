# -*- coding: utf-8 -*-
# __author__=luhu
import unittest

import pymysql


class MySQLTest(unittest.TestCase):
    def setUp(self):
        self.conn = pymysql.connect(host='192.168.1.104',     # 打开数据库连接
                                    user='root',
                                    password='luhu199515lbh',
                                    database='test1',
                                    port=3306)

    def tearDown(self):
        self.conn.close()

    def test_mysql(self):
        sql = 'show tables;'
        cur = self.conn.cursor()
        cur.execute(sql)
        rs = cur.fetchall()
        print('第三张表是：' + str(rs[2]))
        for tables in rs:  # 打印执行结果
            print(tables)
