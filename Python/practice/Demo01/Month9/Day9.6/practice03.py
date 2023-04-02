# @Time    : 2022/9/6 15:03
# @Author  : Andrew

# 定义一个teacher父类，咨询师consultant子类，授课老师technical子类，就业老师job_teacher子类，三个子类继承自父类
# 父类中的属性：ID，Name，FirstDay,Sex,Birth,Level
# 父类中的方法：showJobDesc() 显示应该遵守的规定
class teacher:
    def __init__(self, ID, Name, FirstDay, Sex, Birth, Level):
        self.id = ID
        self.name = Name
        self.fristday = FirstDay
        self.sex = Sex
        self.birth = Birth
        self.level = Level
        print(
            f"欢迎{self.name}老师入职, 工号:{self.id}, 入职日期:{self.fristday}，性别:{self.sex}, 生日:{self.birth}, 级别:{self.level}")

    # @classmethod
    def showJobDesc(self):
        print("【遵守公司的考勤制度】\n【遵守公司的财务制度】\n【遵守公司的人事制度】")


class consultant(teacher):
    def rule(self):
        print("请遵守如下相关规定：")
        self.showJobDesc()
        print("咨询老师需要遵守【招生制度】")


class technical(teacher):
    def rule(self):
        print("请遵守如下相关规定：")
        self.showJobDesc()
        print('授课老师需要遵守【招生制度】')


class job_teacher(teacher):
    def rule(self):
        print("请遵守如下相关规定：")
        self.showJobDesc()
        print('就业老师需要遵守【招生制度】')


# 1. 所有员工需要遵守如下规定：
# 	【遵守公司的考勤制度】
# 	【遵守公司的财务制度】
# 	【遵守公司的人事制度】
# 2. 咨询老师需要遵守【招生制度】
#     授课老师需要遵守【上课制度】
#     就业老师需要遵守【就业制度】
#     采用父类和子类设计欢迎新老师入职的打印信息，如：
#     "欢迎XXX老师入职, 工号:XXX, 入职日期:XXX，性别:XXX, 生日:XXX, 级别:XXX"
#     "请遵守如下相关规定：XXXXX"
#
#     注：
#     1. 父类teacher需要有__init__(self,ID,Name,FirstDay,Sex,Birth,Level)初始化方法
#     子类不需要有__init__初始化方法


if __name__ == '__main__':
    tea1 = consultant(12, '王五', '1992-2-2', '男', '2001-2-3', '特级教师')
    tea1.rule()


class Teacher:
    commonRules = ['【遵守公司的考勤制度】', '【遵守公司的财务制度】', '【遵守公司的人事制度】']

    def __init__(self, ID, Name, FirstDay, Sex, Birth, Level):
        self.ID = ID
        self.Name = Name
        self.FirstDay = FirstDay
        self.Sex = Sex
        self.Birth = Birth
        self.Level = Level

    def Welcome(self):
        print(
            f"欢迎{self.Name}老师入职, 工号:{self.ID}, 入职日期:{self.FirstDay}，性别:{self.Sex}, 生日:{self.Birth}, 级别:{self.Level}")

    def printRules(self, rules):
        for rule in rules:
            print(rule)


class Consultant(Teacher):
    commonRules = ['【遵守公司的招生制度】']


if __name__ == '__main__':
    CObj = Consultant(1001, 'Kate', '2020-01-1', 'Female', '1990-01-01', 'M')
    CObj.Welcome()
    rules = []
    rules = Teacher.commonRules + Consultant.commonRules

    CObj.printRules(rules)
