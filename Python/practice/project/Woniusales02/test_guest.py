# @Time    : 2022/9/15 18:52
# @Author  : Andrew
import random
import time
from project.Woniusales02.page.login import TestLogin
from project.Woniusales02.common.db import DB
from selenium.webdriver.support.select import Select


class TestGuest:
    def __init__(self):
        self.login = TestLogin()

    def test_case_1(self, phonenum):
        self.login.dr.implicitly_wait(2)
        try:
            self.login.test_case_1()
        except:
            pass
        self.login.dr.find_element('link text', '会员管理').click()
        self.login.dr.find_element('id', 'customerphone').send_keys(phonenum)
        self.login.dr.find_element('xpath', '//button[@onclick="addCustomer()"]').click()
        try:
            self.login.dr.find_element('xpath', '//button[@data-bb-handler="ok"]')
        except:
            sql = f'SELECT * from customer where customerphone = {phonenum}'
            num = DB().read_one(sql)
            if len(num) == 0:
                print('会员已存在')
            else:
                print('会员录入成功')
        else:
            print('会员已存在')

    def test_case_2(self, phonenum):
        self.login.dr.implicitly_wait(2)
        self.login.dr.find_element('id', 'customerphone').send_keys(phonenum)
        self.login.dr.find_element('xpath', '//button[@onclick="addCustomer()"]').click()
        try:
            self.login.dr.find_element('xpath', '//button[@data-bb-handler="ok"]')
        except:
            print('会员录入成功')
        else:
            print('会员已存在')

    def guest_number(self):
        num = random.randint(11111111111, 99999999999)
        return num

    def guest_info(self, phonenum, name, sex, date, kidscore, clothscore):
        self.login.dr.implicitly_wait(2)
        try:
            self.login.test_case_1()
        except:
            pass
        self.login.dr.find_element('link text', '会员管理').click()
        self.login.dr.find_element('id', 'customerphone').send_keys(phonenum)

        self.login.dr.find_element('id', 'customername').clear()
        self.login.dr.find_element('id', 'customername').send_keys(name)

        self.sex_method = Select(self.login.dr.find_element('id', 'childsex'))
        self.sex_method.select_by_value(sex)

        js = "document.getElementById('childdate').removeAttribute('readonly')"
        self.login.dr.execute_script(js)
        self.login.dr.find_element('id', 'childdate').clear()
        self.login.dr.find_element('id', 'childdate').send_keys(date)
        time.sleep(2)
        self.login.dr.find_element('id', 'creditkids').send_keys(kidscore)

        self.login.dr.find_element('id', 'creditcloth').send_keys(clothscore)

        self.login.dr.find_element('xpath', '//button[@onclick="addCustomer()"]').click()
        try:
            self.login.dr.find_element('xpath', '//button[@data-bb-handler="ok"]')
        except:
            print('会员录入成功')
        else:
            print('会员已存在')


if __name__ == '__main__':
    guest = TestGuest()
    # guest.test_case_1(12341)
    guest.guest_info(122332, '王五', '男', '2020-1-3', 12, 43)

    time.sleep(3)
    guest.login.dr.quit()
