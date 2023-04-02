# @Time    : 2022/9/7 15:21
# @Author  : Andrew
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
