"""
 @Author: Andrew
 @FileName: get_driver.py
 @DateTime: 2022/10/19 10:30
 @Brief: 实例化浏览器
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from project.WoniuBossAuto.config.get_path import TOOLPATH


class GetDriver:
    dr = None
    brower_ip = TOOLPATH + r"\chromedriver.exe"

    # print(brower_ip)
    def __init__(self):
        pass

    @classmethod
    def get_driver(cls):
        if cls.dr is None:
            s = Service(cls.brower_ip)
            cls.dr = webdriver.Chrome(service=s)
            cls.dr.implicitly_wait(5)

        cls.dr.maximize_window()
        return cls.dr


if __name__ == '__main__':
    d = GetDriver()
    d.get_driver()
