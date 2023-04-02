# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : run.py
@desc: 
@Created on: 2022/9/23 10:38
"""
import os

import pytest

pytest.main([])  # 执行用例

os.system("allure generate ./temp -o ./report --clean")  # 调用终端执行 allure生成报告
