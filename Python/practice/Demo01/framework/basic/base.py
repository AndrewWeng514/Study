"""
 @Author: Andrew
 @FileName: base.py
 @DateTime: 2022/10/17 14:16
 浏览器的一些常用操作
"""
from selenium.webdriver.support.wait import WebDriverWait
from Demo01.framework.basic.get_driver import GetDriver
from selenium.webdriver.support import expected_conditions as ec  # 异常处理
from selenium.webdriver.support.select import Select


class Base:
    def __init__(self):
        self.dr = GetDriver.get_driver()

    def input(self, location, content):
        # self.dr.find_element(*location).send_keys(content)
        try:
            self.get_element(location).send_keys(content)
        except:
            print(f"input{location},未找到")

    def inputs(self, location, i, content):
        # self.dr.find_element(*location).send_keys(content)
        try:
            self.get_elements(location)[i].send_keys(content)
        except:
            print(f"input{location},未找到")

    def click(self, location):
        # self.dr.find_element(*location).click()
        try:

            self.get_element(location).click()
        except:
            print(f'click{location},未找到')

    def clicks(self, location, i):
        # self.dr.find_element(*location).click()
        try:
            self.get_elements(location)[i].click()
        except:
            print(f'click{location},未找到')

    def selects(self, location, i, content):
        try:
            Select(self.get_elements(location)[i]).select_by_visible_text(content)
        except:
            print(f'元素{location}未找到')

    def select(self, location, content):
        try:
            Select(self.get_element(location)).select_by_visible_text(content)
        except:
            print(f'元素{location}未找到')

    def get_element(self, location):
        try:
            ele = WebDriverWait(self.dr, 10, 0.5).until(ec.presence_of_element_located(location))
            return ele
        except:
            print(f'元素{location}没有定位到')

    def get_elements(self, location):
        try:
            ele = WebDriverWait(self.dr, 10, 0.5).until(ec.presence_of_all_elements_located(location))
            return ele
        except:
            print(f'元素{location}没有定位到')

    # def input(self, location, content):
    #     self.dr.find_element(*location).send_keys(content)
