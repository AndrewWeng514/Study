from project.SHClass67.pom.page_login import PageLogin
import time


class TestLogin:
    def __init__(self):
        self.login = PageLogin()

    def test_case(self, caseid, username, password, checkcode, exp):
        self.login.login(username, password, checkcode)
        try:
            self.login.dr.find_element('xpath', f'//div[text()="{exp}"]')
            print(f"{caseid}:测试通过")
            self.login.dr.refresh()
        except:
            print(f"{caseid}:测试失败")
            filename = caseid + time.strftime('%Y%m%d%H%M%S') + '.png'
            time.sleep(1)
            self.login.dr.save_screenshot(f'./img/{filename}')
            self.login.dr.refresh()


if __name__ == '__main__':
    tl = TestLogin()
    tl.test_case('login-1', 'admin1', '123456', '0000', '用户名错误')
    tl.test_case('login-2', 'admin', '1234567', '0000', '密码错误')
    tl.test_case('login-3', 'admin', '123456', '00001', '验证码错误')
