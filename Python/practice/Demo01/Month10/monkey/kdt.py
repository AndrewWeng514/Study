"""
 @Author: Andrew
 @FileName: kdt.py
 @DateTime: 2022/10/20 11:40
 @Brief:
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Common:
    def __init__(self):
        pass

    def open(self, browser):
        if browser == 'chrome':
            s = Service(executable_path=r"E:\practice\Demo01\UI\chromedriver.exe")
            self.dr = webdriver.Chrome(service=s)
        elif browser == 'firefox':
            s = Service(executable_path=r"E:\practice\Demo01\UI\chromedriver.exe")
            self.dr = webdriver.Firefox(service=s)
        self.dr.maximize_window()

    def visit(self, url):
        self.dr.get(url)

    def input(self, by, what, content):
        self.dr.find_element(by, what).send_keys(content)

    def click(self, by, what):
        self.dr.find_element(by, what).click()

    def do_login(self, username='WNCD000', password="woniu123", checkcode='0000'):
        self.open('chrome')
        self.visit("http://101.34.13.184:8080/WoniuBoss4.0/login/")
        self.input('xpath', '//input[@placeholder="请输入用户名"]', username)
        self.input('name', 'userPass', password)
        self.input('name', 'checkcode', checkcode)
        self.click('xpath', '//button[@onclick="login();"]')
        self.wait(3)
        self.assert_exist('link text', '[注销]')

    def assert_exist(self, by, what):
        try:
            self.dr.find_element(by, what)
            print("登录成功")
        except:
            print("登录失败")

    def wait(self, n):
        time.sleep(int(n))

    def start_test(self):
        with open("login.csv", 'r', encoding="utf-8") as file:
            cases = file.read()
            cases = cases.split('\n')
            # print(cases,type(cases))
        for i in cases:
            # print(i)
            ope = i.split(',')[0]
            # print(ope)
            data = i.split(',')[1:]
            # print(*data)
            if hasattr(self, ope):
                getattr(self, ope)(*data)
            else:
                print(f'{ope}不存在')


if __name__ == '__main__':
    c = Common()
    # c.start_test()
    c.do_login()
    # c.open("chrome")
    # c.visit("http://101.34.13.184:8080/WoniuBoss4.0/login/")
    # c.input('xpath', '//input[@placeholder="请输入用户名"]','WNCD000')
    # c.input('name', 'userPass','woniu123')
    # c.input('name', 'checkcode','0000')
    # c.click('xpath', '//button[@onclick="login();"]')
    # c.wait("4")
    # c.assert_exist('link text', '[注销]')

    time.sleep(2)
    c.dr.quit()
