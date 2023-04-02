# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : halo.py
@desc: 
@Created on: 2022/9/21 18:47
"""
import time

import requests


class HaloInterface:
    def __init__(self):
        self.token = self.login().json()["data"]["access_token"]
        self.h = {"Admin-Authorization": self.token,
                  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
                  }

    def login(self):
        url = "https://demo.halo.run/api/admin/login"
        # h={"Content-Type":"application/json"}
        # d='{"username":"demo","password":"P@ssw0rd123..","authcode":null}' #这是json数据 字符串
        # d={'username': 'demo', 'password': 'P@ssw0rd123..', 'authcode': None} # python数据类型
        d = {
            "authcode": None,
            "password": "P@ssw0rd123..",
            "username": "demo"
        }
        print(type(d))
        res = requests.post(url, json=d)
        # res.cookies
        print(res.text)
        return res

    def releasejournals(self, content):
        url = "https://demo.halo.run/api/admin/journals"
        j = {
            "sourceContent": content
        }
        res = requests.post(url, json=j, headers=self.h)

        return res

    def getjournals(self, ):
        url = "https://demo.halo.run/api/admin/journals?page=0&size=10"
        res = requests.get(url, headers=self.h)
        return res

    def upload(self):
        import requests
        time.sleep(3)
        url = "https://demo.halo.run/api/admin/attachments/upload"

        payload = {}
        files = [
            ('file', (
            'a.xls', open(r'D:\Pycharm\PythonProject\python67\interface\data\a.xls', 'rb'), 'application/vnd.ms-excel'))
        ]

        res = requests.request("POST", url, headers=self.h, data=payload, files=files)

        # print(response.text)

        return res

        #
        # url="https://demo.halo.run/api/admin/attachments/upload"
        # method="POST"
        #
        # f={"file":open(r"D:\Pycharm\PythonProject\python67\interface\data\a.xls","rb")}
        # res = requests.request(method,url,headers=self.h,files=f)
        # return res


if __name__ == '__main__':
    halo = HaloInterface()
    halo.login()

    # def output(res):
    #     # 提取响应对象的头部中的Content-Type  判断是否为html
    #
    #     if 'text/html' in res.headers["Content-Type"]:  # 条件成立 说明是html
    #         with open("a.html", "wb") as f:
    #             f.write(res.content)
    #         print("内容是html格式 保存到 a.html中")
    #     else:
    #         print("查看响应正文", res.text)
    #     print("查看响应头", res.headers)
    #     print("查看响应状态码", res.status_code)
    #     print("查看请求头", res.request.headers)
    #     print("查看请求正文", res.request.body)

    # res = halo.login()
    # res = halo.upload()
    # output(res)
