# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : db.py
@desc: 专门用来操作数据库的文件
@Created on: 2021/12/16 10:40
"""

from pymysql import connect
from pymysql.cursors import DictCursor

from common.settings import DBConfig as db


class DB():  # 内聚性  #事务 四大特性
    def __init__(self, database=db.database, host=db.host, port=db.port, user=db.user, password=db.password,
                 cursortype=db.type, autocommit=db.iscommit):
        self.db = connect(host=host, port=port, user=user, password=password, database=database)
        if cursortype == "dict":
            self.cursor = self.db.cursor(DictCursor)  # 字典游标 查询数据后返回的结果是字典格式
        else:
            self.cursor = self.db.cursor()  # 查询数据后返回的结果是元祖格式
        self.db.autocommit(autocommit)

    def fetchone(self, sql):  # 根据sql 查询  一条结果  如果没有返回None
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):  # 根据sql 查询  所有结果
        self.cursor.execute(sql)
        dbres = self.cursor.fetchall()  # 查询不到 返回的是 ()
        return dbres if dbres else []  # 如果有结果返回结果 没结果 () 变 []

    def writeDB(self, sql):  # 根据sql写入数据(增加数据 修改数据 删除数据) 返回受影响的行数

        res = self.cursor.execute(sql)  # 返回受影响的行数1

        return res

    def begin(self):  # 事务开始
        self.db.autocommit(0)

    def end(self):  # 事务结束
        self.db.commit()  # 提交事务
        self.db.autocommit(True)  # 再次设为自动提交


if __name__ == '__main__':
    db = DB("woniusales")
    sql = f'SELECT goodsserial,goodsname,barcode,unitprice from goods WHERE barcode ="123456" ORDER BY goodsid DESC LIMIT 1'
    dbres = db.fetchall(sql)
    print(dbres)
