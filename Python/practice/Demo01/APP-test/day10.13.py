"""
 @Author: Andrew
 @FileName: day10.13.py
 @DateTime: 2022/10/13 9:43
"""
import os
import random
import string
import time

import pyautogui


class Monkey:
    def __init__(self):
        os.system("calc.exe")
        time.sleep(3)
        time1 = time.strftime("%Y%m%d")
        self.resultname = f"result{time1}.csv"

    def read_test(self):
        test_list = []
        with open(f'{self.resultname}', 'r', encoding='utf8') as file:
            # test_list = file.read().split("\n")[1:]
            test_list1 = file.read().split('\n\n')
            for i in test_list1:
                i = i.split("\n")[0:-4]
                test_list.append(i)
        return test_list

    def execute_test(self, test_list, reference):

        test_reference = []
        for i in test_list:
            if reference in i:
                test_reference = i
        print(test_reference)
        for i in test_reference[1:]:
            i = i.split(",")
            print(i)
            # print(i, type(i))
            # 使用反射
            args = i[1:]
            print(args)
            if hasattr(self, i[0]):
                getattr(self, i[0])(*args)
            else:
                print("没有该方法")
            # 一般方法 判断类型并执行
            # if i[0] == 's_click':
            #     x = int(i[1])
            #     y = int(i[2])
            #     self.s_click(x, y)
            # elif i[0] == 'd_click':
            #     x = int(i[1])
            #     y = int(i[2])
            #     self.d_click(x, y)
            # elif i[0] == 'r_click':
            #     x = int(i[1])
            #     y = int(i[2])
            #     self.r_click(x, y)
            # elif i[0] == 'input':
            #     self.input(i[1])

    def s_click(self, x, y, content="无"):
        pyautogui.click(int(x), int(y), clicks=1, button='LEFT')
        print("执行s")

    def d_click(self, x, y, content="无"):
        pyautogui.click(int(x), int(y), clicks=2, button='LEFT')
        print("执行d")

    def r_click(self, x, y, content="无"):
        pyautogui.click(int(x), int(y), clicks=1, button='RIGHT')
        print('执行r')

    def input(self, content):
        pyautogui.write(content)
        print('执行input')


if __name__ == '__main__':
    m = Monkey()
    test_list = m.read_test()
    # print(test_list)
    reference = f"--------{input()}-------"
    m.execute_test(test_list, reference)
