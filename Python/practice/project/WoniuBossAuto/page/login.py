"""
 @Author: Andrew
 @FileName: login.py
 @DateTime: 2022/10/19 11:02
 @Brief:登录界面
"""
import time

from project.WoniuBossAuto.common.base import Base
from project.WoniuBossAuto.config.config import ip


class LoginPage(Base):
    # 单例
    username = ('xpath', '//input[@placeholder="请输入用户名"]')
    password = ('name', 'userPass')
    checkcode = ('name', 'checkcode')
    button_login = ('xpath', '//button[@onclick="login();"]')
    login_out = ('link text', '[注销]')

    def __init__(self):
        super().__init__()  # 继承父类中init方法

    def login_page(self, username='WNCD000', password='woniu123', checkcode='0000'):
        self.dr.maximize_window()
        self.dr.get(f'http://{ip}:8080/WoniuBoss4.0/login')
        self.input(self.username, username)
        self.input(self.password, password)
        self.input(self.checkcode, checkcode)
        self.click(self.button_login)
        # self.dr.find_element(*self.username).send_keys(username)
        # self.dr.find_element(*self.password).send_keys(password)
        # self.dr.find_element(*self.checkcode).send_keys(checkcode)
        # self.dr.find_element(*self.button_login).click()


if __name__ == '__main__':
    l = LoginPage()
    l.login_page()

    time.sleep(7)
    l.dr.quit()
