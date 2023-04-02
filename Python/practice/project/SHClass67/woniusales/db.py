import pymysql


class Db:
    def __init__(self):
        self.conn = pymysql.connect(user='root', password='123456', host='192.168.18.128', db='woniusales')
        self.cur = self.conn.cursor()

    def query_one(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def query_all(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()


if __name__ == '__main__':
    db = Db()
    sql = 'SELECT discountprice from sell ORDER BY sellid desc LIMIT 1;'
    print(db.query_one(sql)[0])
