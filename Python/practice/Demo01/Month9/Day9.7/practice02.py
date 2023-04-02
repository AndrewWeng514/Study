# @Time    : 2022/9/7 10:26
# @Author  : Andrew
# 1. 实现一个计算器，在给定的一个变量data=1000初始值上面进行加减操作；
# 定义3个方法，一个进行加法运算，每次加100，
# 一个进行减法运算，每次减100;
# 一个专门输出变量data的信息，采用多线程的方式来实现
# 加法和减法方法里面利用for循环各循环n次
# import threading
#
#
# class Calculator:
#     def __init__(self):
#         self.data = 1000
#         self.lock = threading.Lock
#     def increase(self, num):
#         for i in range(num):
#             self.lock.acquire()
#             self.data += 100
#             self.lock.release()
#     def subduction(self, num1):
#         for i in range(num1):
#             self.lock.acquire()
#             self.data -= 100
#             self.lock.release()
#     def result(self):
#         print(self.data)
#
#
# if __name__ == '__main__':
#     num3 = Calculator()
#     th1 = threading.Thread(target=num3.increase, args=(10000000,))
#     th2 = threading.Thread(target=num3.subduction, args=(100000,))
#     th1.start()
#     th2.start()
#     th1.join()
#     th2.join()
#     num3.result()


import threading
import time


class computer:
    def __init__(self):
        self.data = 1000
        self.lock = threading.Lock()

    def add(self):
        for i in range(100000):
            self.lock.acquire()
            self.data = self.data + 100
            self.lock.release()

    def sub(self):
        for i in range(100000):
            self.lock.acquire()
            self.data = self.data - 100
            self.lock.release()

    def printData(self):
        print(self.data)


if __name__ == '__main__':
    cObj = computer()
    th1 = threading.Thread(target=cObj.add)
    th2 = threading.Thread(target=cObj.sub)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    cObj.printData()
