# @Time    : 2022/9/15 20:29
# @Author  : Andrew
import time

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import Service


class Work:
    def __init__(self):
        s = Service(executable_path='geckodriver.exe')
        self.dr = webdriver.Firefox(service=s)
        self.dr.maximize_window()
        self.dr.get('http://106.12.175.75:8080/')
        self.dr.find_element('id', 'loginName').send_keys('jsh')
        self.dr.find_element('id', 'password').send_keys('123456')
        self.dr.find_element('id', 'btnSubmit').click()

    def test_case_1(self):
        time.sleep(1)
        self.dr.find_element('xpath', '//a[@title="采购管理"]').click()
        time.sleep(1)
        self.dr.find_element('xpath', '//a[@title="采购订单"]').click()
        self.dr.find_element('id', 'tabpanel-e71300507a').click()

        self.dr.switch_to.frame("tabpanel-e71300507a-frame")
        self.dr.find_element('id', 'addDepotHead').click()
        self.dr.execute_script()


if __name__ == '__main__':
    work = Work()
    work.test_case_1()

    time.sleep(2)
    work.dr.quit()
