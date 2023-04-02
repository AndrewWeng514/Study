"""
 @Author: Andrew
 @FileName: test_login.py
 @DateTime: 2022/10/19 15:35
 @Brief:登录接口的测试脚本
"""
from project.apiTest.action.do_login import Login


class TestLogin:

    def __init__(self):
        pass

    def test_login(self, username, password, checkcode, exp):
        result = Login().do_login(username, password, checkcode)
        if result.text == exp:
            print('测试成功')
        else:
            print('测试失败')


if __name__ == '__main__':
    t = TestLogin()
    t.test_login("WNCD000", 'woniu123', '0000', 'success')
    t.test_login("WNCD000", 'woniu12', '0000', 'error')
    t.test_login("WNCD000", 'woniu12', '000', 'success')
