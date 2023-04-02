import random

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from project.SHClass67.woniusales.test_login import TestLogin
from project.SHClass67.woniusales.db import Db


class TestVip:
    def __init__(self):
        self.login = TestLogin()
        self.db = Db()

    def add_cus(self, phone):
        try:
            self.login.login()
        except:
            pass
        self.login.dr.implicitly_wait(5)
        self.login.dr.find_element('link text', '会员管理').click()
        self.login.dr.find_element('id', 'customerphone').send_keys(phone)
        self.login.dr.find_element('id', 'customername').clear()  # 昵称
        self.login.dr.find_element('id', 'customername').send_keys('zhangsan')
        sex = self.login.dr.find_element('id', 'childsex')
        cho = Select(sex)
        cho.select_by_index(1)
        js = "document.getElementById('childdate').removeAttribute('readonly') "
        self.login.dr.execute_script(js)
        self.login.dr.find_element('id', 'childdate').clear()
        self.login.dr.find_element('id', 'childdate').send_keys('2022-02-02')  # 日期
        self.login.dr.find_element('id', 'creditkids').clear()
        integral = self.login.dr.find_element('id', 'creditkids')
        action = ActionChains(self.login.dr)
        action.move_to_element(integral).double_click()
        action.send_keys('20')
        action.perform()
        self.login.dr.find_element('id', 'creditcloth').clear()
        self.login.dr.find_element('id', 'creditcloth').send_keys('30')  # 童装
        self.login.dr.find_element('xpath', '//button[text() = " 新增"]').click()

    def generate_phone(self):
        phone = random.randint(11111111111, 9999999999)
        return phone

    def test_add_suss(self):
        phone = self.generate_phone()
        self.add_cus(phone)
        sql = 'SELECT customerphone from customer;'
        try:
            self.login.dr.find_element('xpath', '//h4[text()="错误提示"]')
            print("测试失败")
        except:
            result = self.db.query_all(sql)
            result_list = []
            for i in result:
                result_list.append(i[0])
            if phone in result_list:
                print("新增成功，测试通过")
            else:
                print("新增失败，测试失败")

    def test_add_rep(self):
        phone = 1234
        self.add_cus(phone)
        if self.login.dr.find_element('xpath', '//div[text()="该客户信息已经存在，请勿重复添加."]'):
            print("测试通过")
        else:
            print("测试失败")

    def test_case1(self):
        """
        断言：
        1、使用phone的查询，sql语句加上where条件。判断sql语句执行的结果有没有
        2、把数据库所有的手机号查出来，判断phone在不在查询结果中
        """
        try:
            self.login.login()
        except:
            pass
        self.login.dr.implicitly_wait(5)
        self.login.dr.find_element('link text', '会员管理').click()
        phone = '4568'
        self.login.dr.find_element('id', 'customerphone').send_keys(phone)
        self.login.dr.find_element('id', 'customername').clear()  # 昵称
        self.login.dr.find_element('id', 'customername').send_keys('zhangsan')
        sex = self.login.dr.find_element('id', 'childsex')
        cho = Select(sex)
        cho.select_by_index(1)
        js = "document.getElementById('childdate').removeAttribute('readonly') "
        self.login.dr.execute_script(js)
        self.login.dr.find_element('id', 'childdate').clear()
        self.login.dr.find_element('id', 'childdate').send_keys('2022-02-02')  # 日期
        self.login.dr.find_element('id', 'creditkids').clear()
        integral = self.login.dr.find_element('id', 'creditkids')
        action = ActionChains(self.login.dr)
        action.move_to_element(integral).double_click()
        action.send_keys('20')
        action.perform()
        self.login.dr.find_element('id', 'creditcloth').clear()
        self.login.dr.find_element('id', 'creditcloth').send_keys('30')  # 童装
        self.login.dr.find_element('xpath', '//button[text() = " 新增"]').click()
        sql = 'SELECT customerphone from customer;'
        try:
            self.login.dr.find_element('xpath', '//h4[text()="错误提示"]')
            print("测试失败")
        except:
            result = self.db.query_all(sql)
            result_list = []
            for i in result:
                result_list.append(i[0])
            if phone in result_list:
                print("新增成功，测试通过")
            else:
                print("新增失败，测试失败")


if __name__ == '__main__':
    tv = TestVip()
    tv.test_case1()
