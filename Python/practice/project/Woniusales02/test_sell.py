# @Time    : 2022/9/16 10:36
# @Author  : Andrew
import time

from project.Woniusales02.page.login import TestLogin
from project.Woniusales02.common.db import DB
from selenium.webdriver.support.select import Select


class TestShell:
    def __init__(self):
        self.login = TestLogin()

    def test_case(self):
        self.login.dr.implicitly_wait(2)
        try:
            self.login.test_case_1()
        except:
            pass
        # 输入商品条码
        self.login.dr.find_element('id', 'barcode').send_keys("6955203662897")
        #  点击确认
        self.login.dr.find_element('class name', "form-control.btn-primary").click()
        #  查找折扣框
        s1 = self.login.dr.find_element('xpath', '//input[@onblur="changeDiscountRatio(this)"]')
        # 清空折扣框
        # s1.clear()
        # # 清空后会出现弹窗,需点击'ok'键
        # self.login.dr.find_element('xpath', '//button[@data-bb-handler="ok"]').click()
        # #  输入新的折扣
        # s1.send_keys("34")
        #   选取支付方式的下滑框
        s2 = self.login.dr.find_element('xpath', '//select[@id="paymethod"]')
        pay_method = Select(s2)
        #  根据值来选择支付方式
        pay_method.select_by_value('微信')
        #   输入会员账号
        self.login.dr.find_element('id', "customerphone").send_keys("15983123450")
        #   点击查询会员信息
        self.login.dr.find_element('xpath', '//button[text()=" 查询会员信息"]').click()
        self.login.dr.find_element('class name', "form-control.btn-block.btn-primary").click()
        self.login.dr.switch_to.alert.accept()
        #  输入会员仅有一次确认
        time.sleep(2)
        # self.login.dr.switch_to.alert.accept()
        self.login.dr.find_element('xpath', '//a[@href="report"]').click()
        s3 = self.login.dr.find_element('xpath', '//table[@id="selldetail"]/tbody/tr[1]/td[12]').text
        a = DB().read_one(sql="SELECT creditsum FROM sellsum ORDER BY createtime DESC LIMIT 1;")
        if a == s3:
            print('收款金额正确')
        else:
            print('收款金额错误')


if __name__ == '__main__':
    sell = TestShell()
    sell.test_case()
