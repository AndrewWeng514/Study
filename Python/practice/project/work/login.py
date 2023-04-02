# @Time    : 2022/9/16 22:40
# @Author  : Andrew
import time

from project.work.common.common_dr import GetDriver


class Login:
    name = ('xpath', '//input[@placeholder="请输入账号"]')
    password = ('xpath', '//input[@type="password"]')
    click_login = ('id', 'login')

    def __init__(self):
        self.dr = GetDriver().get_driver_chrom()

    def admin_login(self, name="admin", password='11111'):
        self.dr.find_element(*self.name).send_keys(name)
        self.dr.find_element(*self.password).send_keys(password)
        self.dr.find_element(*self.click_login).click()


if __name__ == '__main__':
    restLogin = Login()
    restLogin.admin_login('admin', '11111')

    time.sleep(2)
    restLogin.dr.quit()
