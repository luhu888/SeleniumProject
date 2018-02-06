# -*- coding: utf-8 -*-
# __author__=luhu

import pymysql
from pymysql import ProgrammingError


class MySQLConnect(object):
    @staticmethod
    def test_mysql_init(my_host='192.168.1.104', my_user='root',
                        my_password='luhu199515lbh', my_database='test1',
                        my_port=3306, my_command=''):
        database = pymysql.connect(host=my_host,  # 打开数据库连接
                                   user=my_user,
                                   password=my_password,
                                   database=my_database,
                                   port=my_port,
                                   charset='utf8')  # charset设置很重要，不然会乱码
        cursor = database.cursor()  # 使用cursor()方法获取操作游标
        cursor.execute(my_command)   # 使用execute方法执行SQL语句
        data = cursor.fetchone()    # 使用fetchone()方法获取一条数据
        print('数据库的版本号为：%s' % data)

        database.close()      # 关闭数据库

    @staticmethod
    def test_mysql_exe(my_host='192.168.1.104', my_user='root',
                       my_password='luhu199515lbh', my_database='test1',
                       my_port=3306, my_command=''):
        database = pymysql.connect(host=my_host,  # 打开数据库连接
                                   user=my_user,
                                   password=my_password,
                                   database=my_database,
                                   port=my_port,
                                   charset='utf8')  # charset设置很重要，不然会乱码
        cursor = database.cursor()  # 使用cursor()方法获取操作游标
        # 如果数据表已经存在使用 execute() 方法删除表。
        try:
            cursor.execute(my_command)
            database.commit()
            print(cursor.rowcount)  # 这是一个只读属性，并返回执行execute()方法后影响的行数。
        except:
            database.rollback()  # 回滚，撤销提交数据库操作
        data = cursor.fetchall()  # 使用fetchall()方法获取所有数据
        # print data
        # print type(data)  # data是一个tuple元组
        for key in data:  # 嵌套循环遍历元组中的元组的值
            print('first_name=' + key[0])
            print('last_name=' + key[1])
            print('age=' + str(key[2]))
            print('sex=' + key[3])
            print('tel=' + str(key[4]))
        print('===========')
        # 关闭数据库连接
        database.close()


command = 'SELECT VERSION()'
command2 = "DROP TABLE IF EXISTS EMPLOYEE"
sql = """CREATE TABLE EMPLOYEE (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,  
                 SEX CHAR(1),
                 INCOME FLOAT )"""
sql1 = "INSERT INTO EMPLOYEE VALUES ('卢','虎',21,'m',8000)"
sql2 = "SELECT * FROM EMPLOYEE"
if __name__ == '__main__':
    my_sql = MySQLConnect()
    my_sql.test_mysql_init(my_command=command)
    # my_sql.test_mysql_exe(my_command=command2)
    try:
        # my_sql.test_mysql_exe(my_command=sql)
        my_sql.test_mysql_exe(my_command=sql1)
        my_sql.test_mysql_exe(my_command=sql2)
    except pymysql.err.ProgrammingError:
        print('程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误'
              ' 参数数量错误等等。必须是DatabaseError的子类。')
