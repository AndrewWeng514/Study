# @Time    : 2022/9/16 10:05
# @Author  : Andrew
import time

from selenium import webdriver
from project.Woniusales02.common.common import GetDriver


class Login:
    #   定义网页各元素
    username = ('id', 'username')
    password = ('id', 'password')
    checkCode = ('id', 'verifycode')
    buttonLogin = ('xpath', '//button[contains(text(),"登录")]')

    def __init__(self):
        self.dr = GetDriver().get_driver1_chrome()

    #   定义登录方法
    def login(self, username, password, checkcode):
        self.dr.find_element(*self.username).send_keys(username)
        self.dr.find_element(*self.password).send_keys(password)
        self.dr.find_element(*self.checkCode).send_keys(checkcode)
        self.dr.find_element(*self.buttonLogin).click()


if __name__ == '__main__':
    test = Login()
    test.login('admin', '123456', '0000')
