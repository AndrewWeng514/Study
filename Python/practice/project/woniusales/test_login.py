# @Time    : 2022/9/14 20:14
# @Author  : Andrew
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import Service
from selenium.webdriver.support.select import Select


class TestLogin:
    def __init__(self):
        self.s = Service(executable_path='../../Demo01/UI/geckodriver.exe')
        self.dr = webdriver.Firefox(service=self.s)
        self.dr.maximize_window()
        self.dr.get("http://192.168.4.32:8080/woniusales")

    def test_case_1(self):
        self.dr.find_element("id", 'username').send_keys('admin')
        self.dr.find_element("id", 'password').send_keys('123456')
        self.dr.find_element("id", 'verifycode').send_keys('0000')
        self.dr.find_element("class name", 'form-control.btn-primary').click()


if __name__ == '__main__':
    login = TestLogin()
    login.test_case_1()
