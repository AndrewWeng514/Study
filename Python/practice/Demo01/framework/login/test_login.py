"""
 @Author: Andrew
 @FileName: test_login.py
 @DateTime: 2022/10/17 14:30
"""
import time
import pyautogui
from Demo01.framework.basic.closer import wrapper
from Demo01.framework.basic.database import Common
from Demo01.framework.basic.xls import read_xls_up
from Demo01.framework.config.config import resultdb
from login_page import LoginPage


class TestLogin:
    def __init__(self):
        self.login = LoginPage()
        self.db_object, self.sheet_object = Common.openDB(*resultdb)
        self.cases = read_xls_up("../testdata/TestCase-up.xls", 'Sheet1')

    # 定义登录成功的测试脚本
    def login_success(self):
        self.login.login_page()
        if self.login.get_element(LoginPage.login_out):
            print('登陆成功,测试成功')
        else:
            print('登录失败')

    # 定义登录失败的测试脚本
    @wrapper(*read_xls_up("../testdata/TestCase-up.xls", 'Sheet1'))
    def login_faile(self, case_id, case_name, username, password, checkcode, id, name, exp):
        self.login.dr.refresh()
        self.login.login_page(username, password, checkcode)
        # "密码不能为空."  "用户名或密码错误."
        # 定位到提示框   断言依据 文字不等于期望值
        time.sleep(1)  # 等待发现元素,过快捕捉不到
        result = self.login.get_element((id, name)).text
        # print(result,exp)
        if result == exp:
            print(f"{case_id},{case_name},测试成功")
            sql = f"INSERT INTO login (test_id,NAME, result, picture, exp, fact )" \
                  f"VALUES('{case_id}','{case_name}','success','无','{exp}','{self.login.get_element((id, name)).text}')"
            # print(sql)
            Common.writeDB(self.db_object, self.sheet_object, sql)

        else:
            picture = f"{case_id}.png"
            # print(picture)
            picture_ad = f"../report/{picture}"
            # 截图保存到指定位置
            pyautogui.screenshot(picture_ad)
            #  写入数据库中
            print(f"{case_id},{case_name},测试失败")
            sql = f"INSERT INTO login (test_id,NAME, result, picture, exp, fact )" \
                  f"VALUES('{case_id}','{case_name}','fail','{picture}','{exp}','{self.login.get_element((id, name)).text}')"
            # print(sql)
            Common.writeDB(self.db_object, self.sheet_object, sql)

    def main(self, filead, sheetname):
        cases = read_xls_up(filead, sheetname)
        for i in cases:
            self.login_faile(*i)


if __name__ == '__main__':
    t = TestLogin()
    t.login_faile()
    # t.main("../testdata/TestCase-up.xls",'Sheet1')
    # t.login_success()
    # t.login_faile("sadsajkdhf","dasdjh","用户名或密码错误.")

    time.sleep(2)
    t.login.dr.quit()
