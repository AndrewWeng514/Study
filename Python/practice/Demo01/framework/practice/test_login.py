"""
 @Author: Andrew
 @FileName: test_login.py
 @DateTime: 2022/10/17 11:03
"""
from Demo01.framework.basic.get_driver import GetDriver


class TestLogin:
    def __init__(self):
        self.dr = GetDriver().get_driver()

    def login_test(self):
        self.dr.maximize_window()
        self.dr.get('http://192.168.4.89:8080/WoniuBoss4.0/login')

        self.dr.find_element('xpath', '//input[@placeholder="请输入用户名"]').send_keys('WNCD000')
        self.dr.find_element('name', 'userPass').send_keys("woniu123")
        self.dr.find_element('name', 'checkcode').send_keys("0000")
        self.dr.find_element('xpath', '//button[@onclick="login();"]').click()

        if self.dr.find_element('link text', '[注销]'):
            print('登陆成功')
        else:
            print('登录失败')
