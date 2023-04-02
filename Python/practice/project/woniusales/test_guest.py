# @Time    : 2022/9/15 18:52
# @Author  : Andrew
import time

from test_login import TestLogin
from bd import DB


class TestGuest:
    def __init__(self):
        self.login = TestLogin()
        self.login.test_case_1()
        self.login.dr.find_element('link text', '会员管理').click()

    def test_case_1(self, phonenum):
        self.login.dr.implicitly_wait(2)
        self.login.dr.find_element('id', 'customerphone').send_keys(phonenum)
        self.login.dr.find_element('xpath', '//button[@onclick="addCustomer()"]').click()
        sql = f'SELECT * from customer where customerphone = {phonenum}'
        num = DB().read_one(sql)
        if len(num) == 0:
            print('会员已存在')
        else:
            print('会员录入成功')

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


if __name__ == '__main__':
    guest = TestGuest()
    # guest.test_case_1(12341)
    guest.test_case_2(123453)

    time.sleep(3)
    guest.login.dr.quit()
