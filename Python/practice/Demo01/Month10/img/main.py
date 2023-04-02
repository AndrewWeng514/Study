"""
 @Author: Andrew
 @FileName: main.py
 @DateTime: 2022/10/20 15:11
 @Brief:利用图片来进行自动化

"""
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Img:
    def __init__(self):
        s = Service(executable_path=r'E:\practice\Demo01\UI\chromedriver.exe')
        self.dr = webdriver.Chrome(service=s)
        self.dr.maximize_window()

    def cllik(self):
        pass

    def get_coord(self, picname):
        picad = './picture/' + picname
        x, y = pyautogui.locateCenterOnScreen(picad)
        print(x, y)

    def login(self):
        self.dr.get('http://101.34.13.184:8080/WoniuBoss4.0/login/')
        self.get_coord('password.png')


if __name__ == '__main__':
    t = Img()
    t.login()

    time.sleep(4)
    t.dr.quit()
