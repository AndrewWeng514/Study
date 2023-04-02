"""
 @Author: Andrew
 @FileName: db.py
 @DateTime: 2022/10/18 10:06
 @Brief:
"""
import pymysql


class DB:
    def __init__(self):
        pass

    def openDB(self):
        self.db = pymysql.Connect(host="localhost",
                                  user="root",
                                  password="123456",
                                  port=3306,
                                  db="woniuboss4.0",
                                  charset="utf8")
        self.cur = self.db.cursor()
        return self.db, self.cur

    def readDB(self):
        pass

    def write(self):
        pass


if __name__ == '__main__':
    d = DB()
    a = d.openDB()
    print(a)
