"""
 @Author: Andrew
 @FileName: test_login.py
 @DateTime: 2022/10/19 11:12
 @Brief: 测试登录的脚本
"""
import time

from project.WoniuBossAuto.common.closer import wrapper
from project.WoniuBossAuto.common.database import Common
from project.WoniuBossAuto.common.excel import read_xls_up
from project.WoniuBossAuto.common.screenshot import screenshot
from project.WoniuBossAuto.config.config import resultdb
from project.WoniuBossAuto.page.login import LoginPage


class TestLogin:
    # 登录测试数据的文件名和表名
    # dataname_success =("TestCase-up",'Sheet1')
    dataname_fail = ("TestCase-up", 'Sheet1')

    def __init__(self):
        self.login = LoginPage()
        self.db_object, self.sheet_object = Common.openDB(*resultdb)
        self.tablename = "login" + time.strftime('%Y%m%d%H%M%S')
        sql = f"CREATE TABLE `{self.tablename}`  " \
              "(  `id` int(11) NOT NULL AUTO_INCREMENT," \
              "`test_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL," \
              "`name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL," \
              "`result` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL," \
              "`picture` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL," \
              "`exp` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL," \
              "`fact` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL," \
              "PRIMARY KEY (`id`) USING BTREE) " \
              "ENGINE = MyISAM AUTO_INCREMENT = 0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"
        sql2 = 'SET FOREIGN_KEY_CHECKS = 1;'
        self.sheet_object.execute(sql)
        self.sheet_object.execute(sql2)

    # 定义登录成功的测试脚本
    # @wrapper(*read_xls_up(*dataname_success))
    def login_success(self):
        self.login.login_page()
        if self.login.get_element(LoginPage.login_out):
            print('登陆成功,测试成功')
        else:
            print('登录失败')

    # 定义登录失败的测试脚本
    @wrapper(*read_xls_up(*dataname_fail))
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
            sql = f"INSERT INTO {self.tablename} (test_id,NAME, result, picture, exp, fact )" \
                  f"VALUES('{case_id}','{case_name}','success','无','{exp}','{self.login.get_element((id, name)).text}')"
            # print(sql)
            Common.writeDB(self.db_object, self.sheet_object, sql)

        else:
            screenshot(case_id)
            #  写入数据库中
            print(f"{case_id},{case_name},测试失败")
            sql = f"INSERT INTO {self.tablename} (test_id,NAME, result, picture, exp, fact )" \
                  f"VALUES('{case_id}','{case_name}','fail','{case_id}.png','{exp}','{self.login.get_element((id, name)).text}')"
            # print(sql)
            Common.writeDB(self.db_object, self.sheet_object, sql)


if __name__ == '__main__':
    t = TestLogin()
    # t.login_success()
    t.login_faile()
    # t.main("../testdata/TestCase-up.xls",'Sheet1')
    # t.login_success()
    # t.login_faile("sadsajkdhf","dasdjh","用户名或密码错误.")

    time.sleep(2)
    t.login.dr.quit()
