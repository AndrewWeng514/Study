from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestLogin:

    def __init__(self):
        self.s = Service(executable_path='../ui/chromedriver.exe')
        self.dr = webdriver.Chrome(service=self.s)
        self.dr.maximize_window()

    def login(self):
        """
        封装登录操作
        """
        self.dr.get('http://192.168.18.128:8080/woniusales')
        # 查找用户名输入框元素，然后输入admin
        self.dr.find_element('id', 'username').send_keys('admin')
        # 查找密码输入框元素，然后输入123456
        self.dr.find_element('id', 'password').send_keys('123456')
        # 查找验证码输入框，然后输入0000
        self.dr.find_element('id', 'verifycode').send_keys('0000')
        # 查找登录按钮，然后点击
        self.dr.find_element('class name', 'form-control.btn-primary').click()

    def test_case_1(self):
        pass


if __name__ == '__main__':
    tl = TestLogin()
    tl.login()
