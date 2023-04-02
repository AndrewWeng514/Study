# @Time    : 2022/9/14 19:46
# @Author  : Andrew
import pymysql


class DB:
    def __init__(self):
        self.db_obj = pymysql.connect(user='root', password='123456', host='192.168.4.32', port=3306, db='woniusale',
                                      charset='utf8')
        self.cur_obj = self.db_obj.cursor()

    def read_one(self, sql):
        self.cur_obj.execute(sql)
        return self.cur_obj.fetchone()

    def read_all(self, sql):
        self.cur_obj.execute(sql)
        return self.cur_obj.fetchall()


if __name__ == '__main__':
    db = DB()
    sql = "SELECT creditsum FROM sellsum ORDER BY createtime DESC LIMIT 1;"
    a = db.read_one(sql)
