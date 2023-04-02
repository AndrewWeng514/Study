import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from project.SHClass67.other.img_match import Img


class ImgTest:
    def __init__(self):
        self.s = Service(executable_path='../ui/chromedriver.exe')
        # 实例化Chrome对象。打开chrome浏览器
        self.dr = webdriver.Chrome(service=self.s)

        # 最大化浏览器
        self.dr.maximize_window()
        self.img = Img()

    def login(self):
        self.dr.get('http://192.168.18.128:8080/woniusales')
        time.sleep(1)
        self.img.input('username.png', 'admin')
        self.dr.find_element('id', 'password').clear()
        self.dr.find_element('id', 'password').send_keys('123456')
        time.sleep(1)
        self.img.input('checkcode.png', '0000')
        time.sleep(1)
        self.img.click('login.png')


if __name__ == '__main__':
    it = ImgTest()
    it.login()
