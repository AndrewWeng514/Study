from project.SHClass67.woniusales.test_login import TestLogin

"""
js注入
js = ''
dr.execute_script(js)
"""


class TestQuery:
    def __init__(self):
        self.login = TestLogin()
        self.login.login()

    def test_case_1(self):
        self.login.dr.find_element('link text', '库存查询').click()
        # 移除只读属性，让元素可以输入
        js = "document.getElementById('earlystoretime').removeAttribute('readonly') "
        self.login.dr.execute_script(js)  # 执行js脚本
        self.login.dr.find_element('id', 'earlystoretime').send_keys('2021-01-04')
        # self.login.dr.find_element('xpath','//input[@value="按条件查询库存情况"]').click()
        # 自定义属性，用于后续的元素定位
        js2 = "document.getElementsByClassName('form-control btn-primary')[2].setAttribute('id','query')"
        self.login.dr.execute_script(js2)
        self.login.dr.find_element('id', 'query').click()


if __name__ == '__main__':
    tq = TestQuery()
    tq.test_case_1()
