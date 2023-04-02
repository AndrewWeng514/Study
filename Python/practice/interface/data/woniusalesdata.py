# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : woniusalesdata.py
@desc: 
@Created on: 2022/9/23 16:53
"""
import time

logindata = [
    ("admin", "123456", "0000", "login-pass"),
    ("admin", "123456", "0000", "login-pass"),
    ("admin", "12345", "0000", "login-fail"),
    ("admin", "12345", "00", "vcode-erro")
]
barcodedata = [
    "123456",
    "2154984132548"
]
from faker import Faker

f = Faker("zh_cn")
addvipdata = [
    ("18682558655", "未知", "男", time.strftime("%Y-%m-%d"), "0", "0", "already-added"),
    (
    f.phone_number(), f.name(), f.random.choice(["男", "女"]), str(f.date_between(start_date='-10y', end_date='today')),
    "0", "0", "add-successful"),

]

uploadanddeletedat = [
    ("GB20220928", r"D:\Pycharm\PythonProject\python67\interface\data\a.xls")
]
uploadfaildata = [
    ("GB20220931", r"F:\VideoRecording\网易云音乐测试用例.xls", "format-error"),
    ("GB20220920", r"D:\Pycharm\PythonProject\python67\interface\data\a.xls", "already-imported")
]
