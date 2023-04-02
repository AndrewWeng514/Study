"""
 @Author: Andrew
 @FileName: do_login.py
 @DateTime: 2022/10/19 15:24
 @Brief:登录接口的操作
"""
from project.apiTest.tools.common import Common


class Login:
    def __init__(self):
        self.sess = Common.get_session()

    def do_login(self, username='WNCD000', password='woniu123', checkcode='0000'):
        url = "http://101.34.13.184:8080/WoniuBoss4.0/login/userLogin"
        data = {'userName': username, 'userPass': password, 'checkcode': checkcode, 'remember': 'Y'}
        head = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        login = self.sess.post(url=url, data=data, headers=head)
        # print(login.text)
        return login


if __name__ == '__main__':
    l = Login()
    l.do_login()
