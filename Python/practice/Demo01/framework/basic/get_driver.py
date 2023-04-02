"""
 @Author: Andrew
 @FileName: get_driver.py
 @DateTime: 2022/10/17 11:05
 使用类方法的形式 定义实例化浏览器
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class GetDriver:
    dr = None

    def __init__(self):
        pass

    @classmethod
    def get_driver(cls):
        if cls.dr is None:
            s = Service('../../UI/chromedriver.exe')
            cls.dr = webdriver.Chrome(service=s)
            cls.dr.implicitly_wait(5)

        cls.dr.maximize_window()
        return cls.dr
