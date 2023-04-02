# @Time    : 2022/9/5 15:59
# @Author  : Andrew

class People:
    skin = 'Yellow'  # 类变量： 定义在类体内，但是在方法之外的变量
    name = 'Kate'

    @classmethod  # 类方法： 被@classmethod修饰，第一个形参是cls参数,cls代表当前类本身
    def run(cls):
        print(f'{cls.name} can run!')  # 在一个类方法中修改的类变量可以作用于其他的类方法中

    @staticmethod  # 类静态方法： @staticmethod修改，没有特殊的参数，简单看做之前的函数
    def walk(name):
        print(f'{name} can walk')

    def __init__(self):  # 初始化方法，对对象进行初始化，自动调用执行的方法,创建一个对象的时候会自动执行
        print('This is init method')
        self.height = 185  # 对象变量 通过self表示的变量
        self.nation = 'China'

    def sing(self):  # 对象方法：  没有特定的修饰，但有一个特殊的参数self，self代表对象自身
        print('I like singing')
        print('my height is :', self.height)
        print('my nation is :', self.nation)
        print(self.skin)

    def dance(self):
        print('I like dancing')
        print('my height is :', self.height)
        print('my nation is :', self.nation)


print(People.skin)  # 类名.类变量  直接访问类变量的值
People.run()  # 类名.类方法  通过类名可以直接访问类方法
People.walk('Mike')  # 类名.静态方法  通过类名可以直接访问类静态方法
# People.sing()            # 类名.对象方法  通过类名不可以直接访问对象方法
People.sing(People())  # 类名()   ---创建一个对象
# People.dance(People())

a = People()


def __init__(a):  # 初始化方法，对对象进行初始化，自动调用执行的方法,创建一个对象的时候会自动执行
    print('This is init method')
    a.height = 185  # 对象变量 通过self表示的变量
    a.nation = 'China'
