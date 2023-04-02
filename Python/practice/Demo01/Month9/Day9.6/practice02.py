# @Time    : 2022/9/6 10:10
# @Author  : Andrew
import threading

from unicodedata import name

# 格式：thObj.setDamon(True)
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
        for i in range(2):
            print(f'I am singing {songName} at {ctime()}')
            sleep(1)

    def dance(self, danceName):
        for i in range(2):
            print(f'I am dancing {danceName} at {ctime()}')
            sleep(1)


if __name__ == '__main__':
    ac = actor()
    ac.begin('丽丽')
    threadList = []
    t1 = threading.Thread(target=ac.sing, args=('傻傻的爱傻傻等待',))
    t2 = threading.Thread(target=ac.dance, args=('恰恰舞',))
    threadList.append(t1)
    threadList.append(t2)
    for th in threadList:
        th.Daemon = False  # 设置每个子线程为守护线程，王死则将死，陪葬
        th.start()
    ac.end('丽丽')
