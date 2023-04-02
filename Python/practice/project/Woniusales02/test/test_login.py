# @Time    : 2022/9/16 15:04
# @Author  : Andrew
import time

from project.Woniusales02.page.login import Login


class TestLogin:
    def __init__(self):
        self.test_login = Login()

    def test_case_1(self, docname, username, password, checkcode, exp):
        self.test_login.login(username, password, checkcode)
        docuadd = fr"C:\Users\Andrew\Desktop\{docname}.png"
        try:
            self.test_login.dr.find_element(f'xpath', f'//div[text()={exp}]')
            print('测试成功')
            time.sleep(1)
            self.test_login.dr.save_screenshot(docuadd)
            self.test_login.dr.refresh()
        except:
            print('测试失败')
            time.sleep(1)
            self.test_login.dr.save_screenshot(docuadd)
            self.test_login.dr.refresh()


if __name__ == '__main__':
    test = TestLogin()
    test.test_case_1(1, 'admin1', '123456', '0000', '用户名错误')
    test.test_case_1(2, 'admin', '1234567', '0000', '密码错误')
    test.test_case_1(3, 'admin', '123456', '00001', '验证错误')

    time.sleep(2)
    test.test_login.dr.quit()
