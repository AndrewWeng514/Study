class DBOperation:
    @staticmethod
    def openDB(host, user, pwd, port, db):
        import pymysql
        dbObj = pymysql.connect(host=host, user=user, password=pwd, port=int(port), db=db, charset='utf8')
        curObj = dbObj.cursor()  # 生成游标对象
        return dbObj, curObj

    @staticmethod
    def readDB(curObj, sql):
        curObj.execute(sql)
        result = curObj.fetchall()  # 提取查询结果的所有记录
        return result

    @staticmethod
    def writeDB(dbObj, curObj, sqlList):  # 进行数据库写操作['delete from score...','delete from student.....']
        try:
            for sql in sqlList:
                curObj.execute(sql)
            dbObj.commit()  # 提交
        except:
            dbObj.rollback()  # 回滚

    @staticmethod
    def close(dbObj, curObj):  # 关闭数据库连接操作
        curObj.close()
        dbObj.close()
