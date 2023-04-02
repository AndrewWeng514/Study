from project.SHClass67.woniusales.test_login import TestLogin

"""
1、导入pymysql
2、创建链接
3、创建游标
4、基于游标来执行sql操作
"""


class TestSell:
    def __init__(self):
        self.login = TestLogin()
        self.login.login()

    def test_case_1(self):
        self.login.dr.find_element('id', 'barcode').send_keys('6955203636348')
        self.login.dr.find_element('xpath', '//button[@onclick="queryByBarCode()"]').click()
        self.login.dr.find_element('id', 'customerphone').send_keys('18682558655')
        #
        self.login.dr.find_element('xpath', '//button[@onclick="customerQueryByPhone()"]').click()
        price = self.login.dr.find_element('id', 'finaltotalprice').text
        self.login.dr.find_element('id', 'submit').click()
        if price in self.login.dr.switch_to.alert.text:
            print("价格计算正确")
        else:
            print("价格计算错误")
        self.login.dr.switch_to.alert.accept()
        # 继续加断言


if __name__ == '__main__':
    ts = TestSell()
    ts.test_case_1()
