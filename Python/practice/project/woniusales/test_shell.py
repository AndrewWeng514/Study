# @Time    : 2022/9/14 17:29
# @Author  : Andrew
import time
from selenium.webdriver.support.select import Select
from test_login import TestLogin
from bd import DB


class TestShell:
    def __init__(self):
        self.login = TestLogin()
        self.login.test_case_1()

    def test_case(self):
        # 输入商品条码
        self.login.dr.find_element('id', 'barcode').send_keys("6955203662897")
        #  点击确认
        self.login.dr.find_element('class name', "form-control.btn-primary").click()
        #  查找折扣框
        s1 = self.login.dr.find_element('xpath', '//input[@onblur="changeDiscountRatio(this)"]')
        # 清空折扣框
        s1.clear()
        time.sleep(1)
        # 清空后会出现弹窗,需点击'ok'键
        self.login.dr.find_element('xpath', '//button[@data-bb-handler="ok"]').click()
        time.sleep(1)
        #  输入新的折扣
        s1.send_keys("34")
        #   选取支付方式的下滑框
        s2 = self.login.dr.find_element('xpath', '//select[@id="paymethod"]')
        pay_method = Select(s2)
        #  根据值来选择支付方式
        pay_method.select_by_value('微信')
        #   输入会员账号
        time.sleep(1)
        self.login.dr.find_element('id', "customerphone").send_keys("15983123450")
        #   点击查询会员信息
        time.sleep(1)
        self.login.dr.find_element('xpath', '//button[text()=" 查询会员信息"]').click()
        time.sleep(2)
        self.login.dr.find_element('class name', "form-control.btn-block.btn-primary").click()
        time.sleep(2)
        self.login.dr.switch_to.alert.accept()
        #  输入会员仅有一次确认
        # time.sleep(2)
        # self.login.dr.switch_to.alert.accept()
        time.sleep(1)
        self.login.dr.find_element('xpath', '//a[@href="report"]').click()
        time.sleep(1)
        # s3=self.login.dr.find_element('xpath','/html/body/div[4]/div[3]/table[1]/tbody/tr[1]/td[12]').text
        s3 = self.login.dr.find_element('xpath', '//table[@id="selldetail"]/tbody/tr[1]/td[12]').text
        # / html / body / div[4] / div[3] / table[1] / tbody / tr[1] / td[12]
        print(s3)
        # selldetail > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(12)
        # dr1.find_element(By.CLASS_NAME, "form-control.btn-primary").click()
        a = DB().read_one(sql="SELECT creditsum FROM sellsum ORDER BY createtime DESC LIMIT 1;")
        if a == s3:
            print('收款金额正确')
        else:
            print('收款金额错误')


if __name__ == '__main__':
    ts = TestShell()
    ts.test_case()
