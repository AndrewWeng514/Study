"""
 @Author: Andrew
 @FileName: work.py
 @DateTime: 2022/10/12 18:47
"""
import os
import random
import string
import time
import pyautogui


class MonkeyTest:
    def __init__(self):
        time1 = time.strftime("%Y%m%d")
        resultname = f"result{time1}.csv"
        self.file = open(f'{resultname}', 'a+', encoding='utf8')
        self.count_s = 0
        self.count_d = 0
        self.count_r = 0
        self.count_input = 0

    def random_xy(self):
        x = random.randint(0, 1500)
        y = random.randint(100, 1000)
        return x, y

    def writer_result(self, word):
        self.file.write(word)

    def s_click(self):
        x, y = self.random_xy()
        pyautogui.click(x, y, clicks=1, button='LEFT')
        word = f"s_click,{x},{y},无\n"
        self.writer_result(word)
        self.count_s += 1
        # print(self.count_s)

    def d_click(self):
        x, y = self.random_xy()
        pyautogui.click(x, y, clicks=2, button='LEFT')
        word = f"d_click,{x},{y},无\n"
        self.writer_result(word)
        self.count_d += 1
        # print(self.count_d)

    def r_click(self):
        x, y = self.random_xy()
        pyautogui.click(x, y, clicks=1, button='RIGHT')
        word = f"r_click,{x},{y},无\n"
        self.writer_result(word)
        self.count_r += 1
        # print(self.count_r)

    def input(self):
        content = random.choices(string.digits, k=8)
        content = "".join(content)
        print(content)
        # self.s_click()
        pyautogui.write(content)
        word = f"input,{content}\n"
        self.writer_result(word)
        self.count_input += 1
        # print(self.count_input)

    def monkey_test(self, n):
        time1 = time.strftime("%Y%m%d-%H%M%S")  # 同一天的日志  写到一个文件中
        self.file.write(f"--------{time1}-------\n")
        for i in range(n):
            seed = random.randint(1, 100)

            if seed <= 25:
                self.s_click()
            elif seed <= 50:
                self.d_click()
            elif seed <= 75:
                self.r_click()
            else:
                self.input()
        self.file.write(f"s_click次数为:{self.count_s}\t占比为:{(self.count_s / n):.2%}\n"
                        f"d_click次数为:{self.count_d}\t占比为:{(self.count_d / n):.2%}\n"
                        f"r_click次数为:{self.count_r}\t占比为:{(self.count_r / n):.2%}\n"
                        f"input次数为:{self.count_input}\t占比为:{(self.count_input / n):.2%}\n\n")


if __name__ == '__main__':
    os.system("calc.exe")
    time.sleep(3)
    mt = MonkeyTest()
    mt.monkey_test(12)
