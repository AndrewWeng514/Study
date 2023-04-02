# @Time    : 2022/9/6 11:01
# @Author  : Andrew
from school02.common.common import Common
from school02.config.config import schooldb


class back:
    def __init__(self):
        self.db_object, self.sheet_object = Common.openDB(*schooldb)

    def __del__(self):
        Common.closeDB(self.db_object, self.sheet_object)

    def searchStu(self, name='', sex='', cid='', race=''):
        sql = "select * from student where "
        if name == '':  # 为空  不添加语句
            sql = sql + 'Sname = Sname '  # 方便后方and连接
        else:
            sql = sql + f"Sname = '{name}' "
        if sex == '':
            sql = sql
        else:
            sql = sql + f"and sex = '{sex}' "
        if cid == '':
            sql = sql
        else:
            sql = sql + f"and CID = '{cid}' "
        if race == '':
            sql = sql
        else:
            sql = sql + f"and race = '{race}' "
        print(sql)
        info1 = Common.readDB(self.sheet_object, sql)  # 返回读取信息
        if len(info1) == 0:
            return 0
        else:
            return info1

    def addStu(self, name, birth, firstDay, cid, sex, race='', height=0, hobbies='', remarks=''):
        sql = "insert into student(Sname,birth,firstDay,race,sex,height,CID,hobbies,remarks) values" \
              f"(\'{name}\',\'{birth}\',\'{firstDay}\',\'{race}\',\'{sex}\',\'{height}\',\'{cid}\',\'{hobbies}\',\'{remarks}\')"
        print(sql)
        result = Common.writeDB(self.db_object, self.sheet_object, sql)  # 成功为0,失败-1
        return result

    def updateStu(self, sid, Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks):

        sql = "update student set "
        if Sname == '':
            sql = sql + 'Sname = Sname'
        else:
            sql = sql + f"sname = '{Sname}'"
        if birth == '':
            sql = sql
        else:
            sql = sql + f", birth ='{birth}'"
        if firstDay == '':
            sql = sql
        else:
            sql = sql + f", firstDay ='{firstDay}'"
        if race == '':
            sql = sql
        else:
            sql = sql + f", race ='{race}'"
        if sex == '':
            sql = sql
        else:
            sql = sql + f", sex ='{sex}'"
        if CID == '':
            sql = sql
        else:
            sql = sql + f", cid ={CID}"
        if height == '':
            sql = sql
        else:
            sql = sql + f", height ={height}"
        if hobbies == '':
            sql = sql
        else:
            sql = sql + f", hobbies ='{hobbies}'"
        if remarks == '':
            sql = sql + f" where sid = {sid}"
        else:
            sql = sql + f", remarks = '{remarks}' where sid = {sid}"
        print(sql)
        result = Common.writeDB(self.db_object, self.sheet_object, sql)  # 成功为0,失败-1
        return result

    def delectstu(self, stu_sid):
        sql = "delete from student where " + f"sid = '{stu_sid}'"
        print(sql)
        result3 = Common.writeDB(self.db_object, self.sheet_object, sql)
        return result3
