# @Time    : 2022/9/3 20:14
# @Author  : Andrew
import time

import pymysql

from school.backSevice.business import delectstu


def open_DB(host, user, password, port, db):
    db_object = pymysql.Connect(host=host, user=user, password=password, port=port, db=db, charset='utf8')
    sheet_object = db_object.cursor()
    return db_object, sheet_object


def read_DB(sheet_object, sql):
    sheet_object.execute(sql)
    result = sheet_object.fetchall()
    return result  # 返回  查询的结果


def write_DB(db_object, sheet_object, sql):
    try:
        sheet_object.execute(sql)
        db_object.commit()
        return 0  # 执行成功  返回0
    except:
        db_object.rollback()
        return -1  # 执行失败   返回-1


def close_DB(db_object, sheet_object):
    db_object.close()
    sheet_object.close()


def getStuSearchInfo():
    while True:
        name, sex, cid, race = input("请输入学生信息(以','隔开):\nname sex cid race\n").split(',')
        #       田七,男,,
        if sex not in ('男', '女', ''):  # 判定性别合法 ''查询所有
            print('输入用户性别非法,请重新输入!')
        else:
            result = searchStu(name, sex, cid, race)  # 读取成功返回0 或 学生信息
            if result == 0:
                print('没有该学生')
            else:
                print(result)  # 默认元组  会有,连接
                break


def searchStu(name='', sex='', cid='', race=''):
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
    info1 = read_DB(sheet_object, sql)  # 返回读取信息
    if len(info1) == 0:
        return 0
    else:
        return info1


def getStuAddInfo():
    while True:  # 得到学生的信息
        #   张三,2010-12-03,2010-01-02,,男,,31,,
        Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks = input("请输入学生信息(以','隔开)\n"
                                                                                 "Sname,birth,firstDay,race,sex,height,CID,hobbies,remarks:\n").split(
            ',')
        if Sname == '':
            print('学生姓名不能为空,请重新输入!')
        elif birth == '':
            print('学生生日不能为空,请重新输入!')
            try:
                timeArray = time.strptime(birth, "%Y-%m-%d")  # 判定是否是日期类型
            except:
                print('请输入正确的出生日期')
        elif firstDay == '':
            print('入学时间不能为空,请重新输入!')
            try:
                timeArray = time.strptime(firstDay, "%Y-%m-%d")
            except:
                print('请输入正确的入学时间')
        elif sex == '':
            print('学生性别不能为空,请重新输入!')
        elif sex not in ('男', '女'):
            print('输入用户性别非法,请重新输入!')
        elif height == '':
            height = 0
        elif CID == '':
            print('班级编号不能为空,请重新输入!')
        elif int(CID) not in (31, 33, 35, 37, 38, 39, 41):
            print('请输入正确的班级')
        result = addStu(Sname, birth, firstDay, CID, sex, race, height, hobbies, remarks)
        if result == 0:
            print('添加成功')
        else:
            print('添加失败')
        break


def addStu(name, birth, firstDay, cid, sex, race='', height=0, hobbies='', remarks=''):
    sql = "insert into student(Sname,birth,firstDay,race,sex,height,CID,hobbies,remarks) values" \
          f"(\'{name}\',\'{birth}\',\'{firstDay}\',\'{race}\',\'{sex}\',\'{height}\',\'{cid}\',\'{hobbies}\',\'{remarks}\')"
    print(sql)
    result = write_DB(db_object, sheet_object, sql)  # 成功为0,失败-1
    return result


def getStuUpdataInfo():
    while True:
        name = input('请输入学生姓名:')
        if name == '':
            print("姓名不能为空!")
        else:
            result = searchStu(name)
            if result == -1:
                print('学生不存在,请重新输入')
            else:
                print(result)
                sid = input('请输入需要修改的学生学号:')
                #   张三2,2010-12-03,2010-01-02,,女,,41,,
                Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks \
                    = input(
                    "请输入学生信息(以','隔开)\n""Sname,birth,firstDay,race,sex,height,CID,hobbies,remarks:\n").split(
                    ',')
                if Sname == '':  # 判断
                    print('学生姓名不能为空,请重新输入!')
                elif birth == '':
                    print('学生生日不能为空,请重新输入!')
                    try:
                        timeArray = time.strptime(birth, "%Y-%m-%d")  # 判定是否是日期类型
                    except:
                        print('请输入正确的出生日期')
                elif firstDay == '':
                    print('入学时间不能为空,请重新输入!')
                    try:
                        timeArray = time.strptime(firstDay, "%Y-%m-%d")
                    except:
                        print('请输入正确的入学时间')
                elif sex == '':
                    print('学生性别不能为空,请重新输入!')
                elif sex not in ('男', '女'):
                    print('输入用户性别非法,请重新输入!')
                elif height == '':
                    height = 0
                elif CID == '':
                    print('班级编号不能为空,请重新输入!')
                elif int(CID) not in (31, 33, 35, 37, 38, 39, 41):
                    print('请输入正确的班级')
                result = updateStu(sid, Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks)
                if result == 0:
                    print('修改成功')
                else:
                    print('修改失败')
                break


def updateStu(sid, Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks):
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
        sql = sql + f", remarks = '{remarks}' where sid = '{sid}"
    print(sql)
    result = write_DB(db_object, sheet_object, sql)  # 成功为0,失败-1
    return result


def getStuDelectInfo():
    while True:
        stu_name = input('请输入需要删除的学生姓名:')
        stu_info = searchStu(stu_name)
        if stu_info == 0:
            print('没有该同学')
        else:
            print(stu_info)
            choice3 = input('请输入需要删除的学生学号:')
            result3 = delectstu(choice3)
            if result3 == -1:
                print('删除失败')
            else:
                print('删除成功')
            break


c

db_object, sheet_object = open_DB('localhost', 'root', '514623', 3307, 'practice')
while True:
    choice = input('1.add\n2.search\n3.updata\n4.delete\n请输入您的选择:')
    if choice == '1':  ## 增加学生信息
        getStuAddInfo()
    elif choice == '2':  # 查询功能
        getStuSearchInfo()
    elif choice == '3':  # 修改学生信息
        getStuUpdataInfo()
    elif choice == '4':  # 删除学生信息
        getStuDelectInfo()
    elif choice == 'q':
        break
    else:
        print('请输入正确的选项!')
