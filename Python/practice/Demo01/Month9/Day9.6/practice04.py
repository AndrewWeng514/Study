# @Time    : 2022/9/6 16:41
# @Author  : Andrew
# 1. 定义三个类：人，学生，教授，说明如下：
# 第一个类【人】：2个对象属性，name和Age
# 设置方法myInfo()，打印两个对象属性的值，打印格式："我是xxx，我是xxx岁"
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myInfo(self):
        print(f"我是{self.name},我有{self.age}岁.")


# 第二个类【学生】：
# 继承【人】的name和Age。
# 设置对象属性：成绩（score）
# 设置方法myInfo() 打印格式"我是学生，我的成绩xx分。"
class Student(People):
    def __init__(self, name, age, score):
        super(Student, self).__init__(name, age)
        self.score = score

    def myInfo(self):
        print(f"我是学生,我有{self.score}分")


# 第三个类【教授】：
# 继承【人】的name和Age。
# 设置对象属性：学科（subject）
# 设置方法myInfo() 打印格式"我是教授，我的学科是xx。"
class Professor(People):
    def __init__(self, name, age, subject):
        super(Professor, self).__init__(name, age)
        self.subject = subject

    def myInfo(self):
        print(f"我是教授,我的学科是{self.subject}")


# 三个类分别进行实例化操作,要求显示
# 【人】我是Lee,我是24岁。
# 【学生】我是Zed，我是23岁，我是学生，我的成绩89分。
# 【教授】我是Annie，我是59岁，我是教授，我的学科是生物。


if __name__ == '__main__':
    peo = People('Lee', 24, )
    peo.myInfo()
    stu = Student('Zed', 23, 89)
    super(Student, stu).myInfo()
    stu.myInfo()
    pro = Professor('Annie', 59, '生物')
    super(Professor, pro).myInfo()
    pro.myInfo()
