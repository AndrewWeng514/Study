"""
 @Author: Andrew
 @FileName: run.py
 @DateTime: 2022/10/19 14:23
 @Brief:
"""
import time

from project.WoniuBossAuto.page.login import LoginPage
from project.WoniuBossAuto.testcase.test_login import TestLogin
from project.WoniuBossAuto.common.report import Reporter

if __name__ == '__main__':
    # print(ROOT_PATH)
    LoginPage().login_page()
    # tl = TestLogin()
    # tl.login_success()
    # time.sleep(9)
