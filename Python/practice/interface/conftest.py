# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : conftest.py
@desc: 
@Created on: 2022/9/23 15:09
"""
import pytest


@pytest.fixture()
def myfixture():
    print("执行前要做的操作")  # 用例执行前要做的事 写在yield之前
    yield
    print("执行后要做的操作")  # 用例执行后要做的事 写在yield之后

# @pytest.fixture(scope="session")
# def start():
#     print("整个会话开始前作用")  # 用例执行前要做的事 写在yield之前
#     yield
#     print("整个会话结束后作用")  # 用例执行后要做的事 写在yield之后

# @pytest.fixture(scope="module")
# def startmodule():
#     print("整个模块开始前作用")  # 用例执行前要做的事 写在yield之前
#     yield
#     print("整个模块结束后作用")  # 用例执行后要做的事 写在yield之后
