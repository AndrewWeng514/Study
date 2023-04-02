# @Time    : 2022/9/2 9:22
# @Author  : Andrew
import time
import datetime

import pymysql


###   学生信息的增删改查

#  数据库的读写操作
def open_DB(host, user, password, port, db):
    db_object = pymysql.Connect(host=host, user=user, password=password, port=port, db=db, charset='utf8')
    sheet_object = db_object.cursor()
    return db_object, sheet_object


def read_DB(sheet_object, sql):
    sheet_object.execute(sql)
    result = sheet_object.fetchall()
    return result


def write_DB(db_object, sheet_object, sql):
    try:
        sheet_object.execute(sql)
        db_object.commit()
    except:
        db_object.rollback()


def close_DB(db_object, sheet_object):
    db_object.close()
    sheet_object.close()


#  前段交互操作 函数

#   得到需要搜索的学生信息
def getStuSearchInfo():
    while True:
        name, sex, cid, race = input("请输入学生信息(以','隔开):\nname sex cid race\n").split(',')
        if sex not in ('男', '女'):
            print('输入用户性别非法,请重新输入!')
        else:
            return name, sex, cid, race


#    得到需要添加的学生的信息
def getStuAddInfo():
    while True:
        Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks = input("请输入学生信息(以','隔开)\n"
                                                                                 "Sname,birth,firstDay,race,sex,height,CID,hobbies,remarks:\n").split(
            ',')
        if Sname == '':
            print('学生姓名不能为空,请重新输入!')
        elif birth == '':
            print('学生生日不能为空,请重新输入!')
            try:
                timeArray = time.strptime(birth, "%Y-%m-%d")
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
        elif CID == '':
            print('班级编号不能为空,请重新输入!')
        elif int(CID) not in (31, 33, 35, 37, 38, 39, 41):
            print('请输入正确的班级')
        else:
            return Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks


#   得到需要修改的学生信息
def getStuUpdataInfo():
    while True:
        name = input('请输入学生姓名:')
        result, stu_info = searchStu(name, sex='', cid='', race='')
        # print(stu_info,type(stu_info))
        if result == 0:
            sid = stu_info[0][0]
            # stu_info1.extend(stu_info[0])
            Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks = input("请输入学生信息(以','隔开)\n"
                                                                                     "Sname,birth,firstDay,race,sex,height,CID,hobbies,remarks:\n").split(
                ',')
            if Sname == '':
                print('学生姓名不能为空,请重新输入!')
            elif birth == '':
                print('学生生日不能为空,请重新输入!')
                try:
                    timeArray = time.strptime(birth, "%Y-%m-%d")
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
            elif CID == '':
                print('班级编号不能为空,请重新输入!')
            elif int(CID) not in (31, 33, 35, 37, 38, 39, 41):
                print('请输入正确的班级')
            else:
                if height == '':
                    height = 0
            return name, Sname, birth, firstDay, sex, CID, race, height, hobbies, remarks


def stuDelectInfo():
    while True:
        stu_name = input('请输入需要删除的学生姓名:')
        result1, stu_info2 = searchStu(stu_name, sex='', cid='', race='')
        if result1 == -1:
            print('没有该同学')
        else:
            # print(stu_info2)
            # choice3 = input('请输入需要删除的学生学号:')
            result3 = delectstu(stu_name)
            if result3 == -1:
                print('删除失败')
            else:
                print('删除成功')

# 后端操作
#   查询学生信息并返回result结果 0.-1
def searchStu(name, sex, cid, race):
    sql = "select * from student where "
    if name == '':
        sql = sql + 'Sname = Sname '
    else:
        sql = sql + f'Sname = \'{name}\' '
    if sex == '':
        sql = sql + 'and sex = sex '
    else:
        sql = sql + f'and sex = \'{sex}\' '
    if cid == '':
        sql = sql + 'and CID = CID '
    else:
        sql = sql + f'and CID = \'{cid}\' '
    if race == '':
        sql = sql + 'and race = race '
    else:
        sql = sql + f'and race = \'{race}\' '
    info1 = read_DB(sheet_object, sql)
    if len(info1) == 0:
        result = -1
    else:
        result = 0
    return result, info1


#   添加学生的信息到数据库
def addStu(name, birth, firstDay, race, sex, height, cid, hobbies, remarks):
    if height == '':
        height = 0
    sql = "insert into student(Sname,birth,firstDay,race,sex,height,CID,hobbies,remarks) values" \
          f"(\'{name}\',\'{birth}\',\'{firstDay}\',\'{race}\',\'{sex}\',\'{height}\',\'{cid}\',\'{hobbies}\',\'{remarks}\')"
    write_DB(db_object, sheet_object, sql)
    result = searchStu(name, sex, cid, race)
    return result


def updateStu(name, Sname, birth, firstDay, sex, CID, race, height, hobbies, remarks):
    sql = "update student set "
    if Sname == '':
        sql = sql + "sname = sname"
    else:
        sql = sql + f"sname = '{Sname}'"
    if birth == '':
        sql = sql + ", birth = birth"
    else:
        sql = sql + f", birth ='{birth}'"
    if firstDay == '':
        sql = sql + ", firstDay = firstDay"
    else:
        sql = sql + f", firstDay ='{firstDay}'"
    if sex == '':
        sql = sql + ", sex = sex"
    else:
        sql = sql + f", sex ='{sex}'"
    if CID == '':
        sql = sql + ", cid = cid"
    else:
        sql = sql + f", cid ={CID}"
    if race == '':
        sql = sql + ", race = race"
    else:
        sql = sql + f", race ='{race}'"
    if height == '':
        sql = sql + ", height = height"
    else:
        sql = sql + f", height ={height}"
    if hobbies == '':
        sql = sql + ", hobbies = hobbies "
    else:
        sql = sql + f", hobbies ='{hobbies}'"
    if remarks == '':
        sql = sql + f", remarks = remarks where Sname = '{name}'"
    else:
        sql = sql + f", remarks = {remarks} where Sname = '{name}'"
    write_DB(db_object, sheet_object, sql)
    result, stu_info = searchStu(Sname, sex, CID, race)
    return result


def delectstu(num):
    sql = "delete from student where " + f"Sname = '{num}'"
    print(sql)
    result3 = write_DB(db_object, sheet_object, sql)
    return result3


db_object, sheet_object = open_DB('localhost', 'root', '514623', 3307, 'practice')
# choice = input('1.add\n2.search\n3.updata\n4.delete\n请输入您的选择:')
while True:
    choice = input('1.add\n2.search\n3.updata\n4.delete\n请输入您的选择:')
    ## 增加学生信息
    if choice == '1':
        add_stu_info = getStuAddInfo()
        result = addStu(*add_stu_info)
        if result == -1:
            print('添加失败!')
        else:
            print('新增成功!')
    #  查询功能
    elif choice == '2':
        search_info = getStuSearchInfo()
        result, stu_info = searchStu(*search_info)
        if result == -1:
            print('没有该同学')
        else:
            print(stu_info)

    elif choice == '3':
        name, Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks = getStuUpdataInfo()
        result1, check_info = updateStu(name, Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks)
        if result1 == -1:
            print('修改失败!')
        else:
            print('修改成功!')
    elif choice == '4':
        stuDelectInfo()
    elif choice == 'q':
        break
    else:
        print('请输入正确的选项!')
close_DB(db_object, sheet_object)
# '1.[name] 2.[birth] 3.[firstDay] 4.[race] 5.[sex] 6.[height] 7.[CID] 8 [hobbies] 9[remarks]
