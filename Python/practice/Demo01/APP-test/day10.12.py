"""
 @Author: Andrew
 @FileName: day10.12.py
 @DateTime: 2022/10/12 16:25
"""
import threading

"""
导入os包

"""

import os


class Monkey():
    def __init__(self):
        self.cpu_list = []

    def start_monkey(self):
        cmd = "adb shell monkey -p com.wondertek.paper -v -v -v 3000 > monkey.log"
        th = threading.Thread(target=self.performance_monkey, args=())
        th.daemon = True
        th.start()
        os.system(cmd)

    def performance_monkey(self):
        cmd = "adb shell dumpsys cpuinfo | findstr com.wondertek.paper"
        while True:
            result_cpu = os.popen(cmd).read()
            self.cpu_list.append(result_cpu.strip().split(" ")[0])
            print(result_cpu.strip().split(" ")[0])


if __name__ == '__main__':
    m = Monkey()
    m.start_monkey()
    # m.performance_monkey()
