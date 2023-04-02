# @Time    : 2022/9/6 11:01
# @Author  : Andrew
import pymysql


class Common:
    @staticmethod
    def openDB(host, user, password, port, db):
        import pymysql
        db_object = pymysql.Connect(host=host, user=user, password=password, port=port, db=db, charset='utf8')
        sheet_object = db_object.cursor()
        return db_object, sheet_object

    @staticmethod
    def readDB(sheet_object, sql):
        sheet_object.execute(sql)
        result = sheet_object.fetchall()
        return result  # 返回  查询的结果

    @staticmethod
    def writeDB(db_object, sheet_object, sql):
        try:
            sheet_object.execute(sql)
            db_object.commit()
            return 0  # 执行成功  返回0
        except:
            db_object.rollback()
            return -1  # 执行失败   返回-1

    @staticmethod
    def closeDB(db_object, sheet_object):
        db_object.close()
        sheet_object.close()
