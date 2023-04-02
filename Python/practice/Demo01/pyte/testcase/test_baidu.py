# @Date   : 2022/9/23 10:11
# @Author : Andrew
# @Name   : test_baidu
import time

import pytest


def setup_module(self):
    print("$$$$$每个模块执行前执行一次")


def teardown_module(self):
    print("$$$$$每个模块执行后执行一次")


class TestBaidu:

    def setup_class(self):
        print("所有用例执行前执行一次")

    def teardown_class(self):
        print("所有用例执行后执行一次")

    def setup(self):
        print("每个用例执行前执行一次")

    def teardown(self):
        print("每个用例执行后执行一次")

    def testlogin(self):
        print("测试登录")
        time.sleep(1)
        assert 1 == 3

    @pytest.mark.login
    def testsell(self):
        print("测试购买")
        time.sleep(1)
        assert 1 == 1
