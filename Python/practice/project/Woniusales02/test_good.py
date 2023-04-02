# @Time    : 2022/9/16 10:52
# @Author  : Andrew
import time

from project.Woniusales01.test_login import TestLogin


class TestGood:

    def __init__(self):
        self.login = TestLogin()

    def test_case_1(self):
        try:
            self.login.test_case_1()
        except:
            pass
        self.login.dr.find_element('link text', '批次管理').click()
        self.login.dr.find_element('id', 'batchname').clear()
        self.login.dr.find_element('id', 'batchname').send_keys('GB202209678')
        self.login.dr.find_element('id', 'batchfile').send_keys(r"C:\Users\Andrew\Desktop\autoTest.xls")
        self.login.dr.find_element('xpath', '//input[@value="确认导入本批次商品信息"]').click()
        print('商品导入成功')


if __name__ == '__main__':
    good = TestGood()
    good.test_case_1()

    time.sleep(1)
    good.login.dr.quit()
