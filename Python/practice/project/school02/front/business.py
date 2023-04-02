# @Time    : 2022/9/6 11:00
# @Author  : Andrew
from school02.back.business import back


class front:

    def __init__(self):
        self.fr = back()

    def getStuSearchInfo(self):
        while True:
            name, sex, cid, race = input("请输入学生信息(以','隔开):\nname sex cid race\n").split(',')
            #       田七,男,,
            if sex not in ('男', '女', ''):  # 判定性别合法 ''查询所有
                print('输入用户性别非法,请重新输入!')
            else:
                result = self.fr.searchStu(name, sex, cid, race)  # 读取成功返回0 或 学生信息
                if result == 0:
                    print('没有该学生')
                else:
                    print(result)  # 默认元组  会有,连接

                    break

    def getStuAddInfo(self):
        import time
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
            result = self.fr.addStu(Sname, birth, firstDay, CID, sex, race, height, hobbies, remarks)
            if result == 0:
                print('添加成功')
            else:
                print('添加失败')

            break

    def getStuUpdataInfo(self):
        import time
        while True:
            name = input('请输入学生姓名:')
            if name == '':
                print("姓名不能为空!")
            else:
                result = back().searchStu(name)
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
                    result = self.fr.updateStu(sid, Sname, birth, firstDay, race, sex, height, CID, hobbies, remarks)
                    if result == 0:
                        print('修改成功')
                    else:
                        print('修改失败')
                    break

    def getStuDelectInfo(self):
        while True:
            stu_name = input('请输入需要删除的学生姓名:')
            stu_info = self.fr.searchStu(stu_name)
            if stu_info == 0:
                print('没有该同学')
            else:
                print(stu_info)
                choice3 = input('请输入需要删除的学生学号:')
                result3 = self.fr.delectstu(choice3)
                if result3 == -1:
                    print('删除失败')
                else:
                    print('删除成功')
                break
