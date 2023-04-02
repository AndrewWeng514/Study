# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : woniusales.py
@desc: woniusale项目中的接口业务
@Created on: 2022/9/20 17:21
"""
import json
import time

import requests


class WoniuSalesInterface:
    IP = "http://localhost:8080"

    def __init__(self):
        self.loginres = self.login("admin", "123456", "0000")

    #  登录功能的实现
    def login(self, username, password, verifycode):
        """
        woniusales登陆接口
        :param username: 用户名参数
        :param password: 密码参数
        :param verifycode: 验证码参数
        :return: 接口的响应对象
        """
        d = {"username": username, "password": password, "verifycode": verifycode}
        # res =requests.post(f"{self.IP}/WoniuSales-20180508-V1.4-bin/user/login", data=d)
        res = requests.post(f"{self.IP}/WoniuSales-20180508-V1.4-bin/user/login", data=d)
        return res

    def querybarcode(self, barcode):
        url = f"{self.IP}/WoniuSales-20180508-V1.4-bin/sell/barcode"
        data = {"barcode": barcode}

        res = requests.post(url, data=data, cookies=self.loginres.cookies)
        return res

    def addvip(self, phone, name="未知", sex="男", date=time.strftime("%Y-%m-%d"), kids="0", cloth="0"):
        """
        新增会员信息接口
        :param phone: 手机号信息 必填参数
        :param name: 会员名称
        :param sex: 会员性别
        :param date:
        :param kids:
        :param cloth:
        :return: 接口的响应对象
        """
        url = f"{self.IP}/WoniuSales-20180508-V1.4-bin/customer/add"
        data = {
            "customername": name,
            "customerphone": phone,
            "childsex": sex,
            "childdate": date,
            "creditkids": kids,
            "creditcloth": cloth
        }

        res = requests.post(url, cookies=self.loginres.cookies, data=data)
        return res

    def upload(self, batchname, filepath):
        url = f"{self.IP}/WoniuSales-20180508-V1.4-bin/goods/upload"  #
        d = {"batchname": batchname}
        f = {"batchfile": open(filepath, "rb")}
        res = requests.post(url, data=d, files=f, cookies=self.loginres.cookies)
        return res

    def deletebatch(self, batchname):
        url = f"{self.IP}/WoniuSales-20180508-V1.4-bin/goods/deletebatch"
        data = {"batchname": batchname}
        res = requests.post(url, data=data, cookies=self.loginres.cookies)
        return res


if __name__ == '__main__':
    def output(res):
        # 提取响应对象的头部中的Content-Type  判断是否为html
        if 'text/html' in res.headers["Content-Type"]:  # 条件成立 说明是html
            with open("a.html", "wb") as f:
                f.write(res.content)
            print("内容是html格式 保存到 a.html中")
        else:
            print("查看响应正文", res.text)
        print("查看响应头", res.headers)
        print("查看响应状态码", res.status_code)
        print("查看请求头", res.request.headers)
        # print("查看请求正文", res.request.body)


    wn = WoniuSalesInterface()
    # res = wn.login("admin","123456","00")
    # res = wn.querybarcode("123456")
    # res = wn.addvip("12345612")
    res = wn.upload("GB20220921", r"D:\Pycharm\PythonProject\python67\interface\data\a.xls")
    # res = wn.deletebatch("GB20220921")
    # print(res.text)
    output(res)
