# @Time    : 2022/9/2 17:22
# @Author  : Andrew
import time

import pymysql


def open_DB(host, user, password, port, db):
    db_object = pymysql.Connect(host=host, user=user, password=password, port=port, db=db, charset='utf8')
    sheet_object = db_object.cursor()
    return db_object, sheet_object


db_object, sheet_object = open_DB('localhost', 'root', '514623', 3307, 'practice')


def read_DB(sheet_object, sql):
    sheet_object.execute(sql)
    result = sheet_object.fetchall()
    return result


def write_DB(db_object, sheet_object, sql):
    sheet_object.execute(sql)
    db_object.commit()


def close_DB(db_object, sheet_object):
    db_object.close()
    sheet_object.close()


def getStuSearchInfo():
    while True:
        name, sex, cid, race = input("请输入学生信息(以','隔开):\nname sex cid race").split(',')
        if sex not in ('男', '女'):
            print('输入用户性别非法,请重新输入!')
        else:
            return name, sex, cid, race


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


# info = getStuSearchInfo()
# result,info_stu = searchStu(*info)
#
# print(info_stu,type(info_stu),len(info_stu))
# if len(result) == 0:
#     print('没有该同学')
# else:
#     print(result)
# try:
#     dt = "2020-01-3"
# #转换成时间数组
#     timeArray = time.strptime(dt, "%Y-%m-%d")
#  except:
#     print('请输入正确的时间格式')
# else:
#     print('这是一个正确的时间')
# 转换成时间戳
# timestamp = time.mktime(timeArray)
# print(timeArray,"\n",timestamp)
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


def addStu(name, birth, firstDay, race, sex, height, cid, hobbies, remarks):
    if height == '':
        height = 0
    sql = "insert into student(Sname,birth,firstDay,race,sex,height,CID,hobbies,remarks) values" \
          f"(\'{name}\',\'{birth}\',\'{firstDay}\',\'{race}\',\'{sex}\',\'{height}\',\'{cid}\',\'{hobbies}\',\'{remarks}\')"
    write_DB(db_object, sheet_object, sql)
    result = searchStu(name, sex, cid, race)
    return result


'''
def getStuUpdataInfo():
    while True:
        name = input('请输入学生姓名:')
        result, stu_info = searchStu(name, sex='', cid='', race='')
        # print(stu_info,type(stu_info))
        if result == -1:
            print('没有该同学,请重新输入')
        elif result == 0:
            stu_info1= []
            stu_info1.extend(stu_info[0])
            while True:
                print(stu_info1)
                choice2 = input('请选择需要修改的学生信息:\n'
                                '1.[name] 2.[birth] 3.[firstDay] 4.[race] 5.[sex] 6.[height] 7.[CID] 8.[hobbies] 9.[remarks]:\n')
                if choice2 == '1':
                    word = input('请输入修改的内容:')
                    if word == '':
                        print('学生姓名不能为空,请重新输入!')
                    else:
                         name= word

                elif choice2 == '2':
                    word = input('请输入修改的生日日期:')
                    if word == '':
                        print('学生生日不能为空,请重新输入!')
                    else:
                        try:
                            timeArray = time.strptime(word, "%Y-%m-%d")
                        except:
                            print('请输入正确的出生日期')
                        else:
                            birth = word
                elif choice2 == '3':
                    word = input('请输入修改的内容:')
                    if word == '':
                        print('入学时间不能为空,请重新输入!')
                    else:
                        try:
                            timeArray = time.strptime(word, "%Y-%m-%d")
                        except:
                            print('请输入正确的入学时间')
                        else:
                            firstDay = word
                elif choice2 == '4':
                    word = input('请输入修改的内容:')
                    stu_info1[4] = word
                elif choice2 == '5':
                    word = input('请输入修改的内容:')
                    if word == '':
                        print('学生性别不能为空,请重新输入!')
                    elif word not in ('男', '女'):
                        print('输入用户性别非法,请重新输入!')
                    else:
                        stu_info1[5] = word
                elif choice2 == '6':
                    word = float(input('请输入修改的内容:'))
                    stu_info1[6] = int(word)
                elif choice2 == '7':
                    word = int(input('请输入修改的内容:'))
                    if word == '':
                        print('班级编号不能为空,请重新输入!')
                    elif int(word) not in (31, 33, 35, 37, 38, 39, 41):
                        print('请输入正确的班级')
                    else:
                        stu_info1[7] = int(word)
                elif choice2 == '8':
                    word = input('请输入修改的内容:')
                    stu_info1[8] = word
                elif choice2 == '9':
                    word = input('请输入修改的内容:')
                    stu_info1[9] = word
                elif choice2=='q':
                    break
                # sid = stu_info1[0]
                # name= stu_info1[1]
                # birth= stu_info1[2]
                # firstDay= stu_info1[3]
                # race= stu_info1[4]
                # sex= stu_info1[5]
                # height= stu_info1[6]
                # cid= stu_info1[7]
                # hobbies= stu_info1[8]
                # remarks= stu_info1[9]
                return sid,name, birth, firstDay, race, sex, height, cid, hobbies, remarks
'''


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
            return name, Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks


def updateStu(sql):
    write_DB(db_object, sheet_object, sql)


#   张三,2010-12-03,2010-01-02,,男,,31,,
# while True:
#     info = getStuAddInfo()
#     sql = addStu(*info)
#     print(sql)
sql = getStuUpdataInfo()
print(sql)

updateStu(sql)
# print(result)
