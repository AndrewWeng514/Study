# @Time    : 2022/9/7 9:40
# @Author  : Andrew
from time import ctime, sleep
import threading
# class actor:
#     def __init__(self):
#         pass
#
#     def begin(self,name):
#         print(f'{name}开始表演...')
#
#     def end(self,name):
#         print(f'{name}表演结束...')
#
#     def sing(self,songName):
#         for i in range(5):
#             print(f'I am singing {songName} at {ctime()}')
#             sleep(1)
#
#     def dance(self,danceName):
#         for i in range(5):
#             print(f'I am dancing {danceName} at {ctime()}')
#             sleep(1)
#
# if __name__ == '__main__':
#     ac=actor()
#     ac.begin('丽丽')
#     th1=threading.Thread(target=ac.sing,args=('傻傻的爱傻傻等待',))   #创建子线程   工人
#     th2=threading.Thread(target=ac.dance,args=('恰恰舞',))
#     th1.start()     #启动子线程开始运行    工人开始干活
#     th2.start()
#     th1.join()     #join是阻塞的作用，主要是对主线程进行阻塞，需要针对子线程调用该方法，让主线程等待该子线程运行结束
#     th2.join()
#     ac.end('丽丽')


from time import ctime, sleep
import threading


class actor:
    def __init__(self):
        pass

    def begin(self, name):
        print(f'{name}开始表演...')

    def end(self, name):
        print(f'{name}表演结束...')

    def sing(self, songName):
        for i in range(5):
            print(f'I am singing {songName} at {ctime()}')
            sleep(1)

    def dance(self, danceName):
        for i in range(5):
            print(f'I am dancing {danceName} at {ctime()}')
            sleep(1)


if __name__ == '__main__':
    ac = actor()
    ac.begin('丽丽')
    th1 = threading.Thread(target=ac.sing, args=('傻傻的爱傻傻等待',))  # 创建子线程   工人
    th2 = threading.Thread(target=ac.dance, args=('恰恰舞',))
    th1.Daemon = True  # 守护方法
    th2.Daemon = True
    th1.start()  # 启动子线程开始运行    工人开始干活
    th2.start()
    ac.end('丽丽')
