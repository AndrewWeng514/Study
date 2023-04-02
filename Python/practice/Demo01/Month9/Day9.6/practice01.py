# @Time    : 2022/9/6 9:26
# @Author  : Andrew
class father:
    Country = 'China'

    def __init__(self):
        self.Race = '汉'
        print(f'I am {self.Race}')

    def run(self):
        print('I can run fast')

    @classmethod
    def sing(cls):
        print('I can sing')

    @staticmethod
    def dance():
        print('I can dance')


class son(father):
    pass


if __name__ == '__main__':
    sonObj = son()  # 实例化子类对象
    sonObj.run()  # 子类对象调用父类对象方法
    sonObj.sing()  # 子类对象调用父类类方法
    sonObj.dance()  # 子类对象调用父类静态方法
    son.sing()  # 子类通过类名调用父类类方法
    son.dance()  # 子类通过类名调用父类静态方法
    print(sonObj.Country)  # 子类对象调用父类类变量
    print(son.Country)  # 子类通过类名调用父类类变量
    print(sonObj.Race)  # 子类对象调用父类对象变量


# <2>. 多继承
# 一个子类可以从多个父类进行继承
class father:
    def __init__(self, Name):  # 类方法-初始化方法
        self.name = Name  # 实例变量，通过self进行修饰

    def sing(self):  # 类方法
        print("{} can sing".format(self.name))


class mother:
    def __init__(self, Name):  # 类方法-初始化方法
        self.name = Name  # 实例变量，通过self进行修饰

    def dance(self):  # 类方法
        print("{} can dance".format(self.name))


class son(father, mother):
    pass


if __name__ == '__main__':
    sonObj = son('大头儿子')  # 实例化对象，通过变量保存对象
    sonObj.sing()
    sonObj.dance()
