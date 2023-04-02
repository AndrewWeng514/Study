# @Date   : 2022/9/21 19:14
# @Author : Andrew
# @Name   : halo
import json

import requests


# 后台地址：https://demo.halo.run/admin
# 用户名：demo
# 密码：P@ssw0rd123..

class Halointerface():

    def __init__(self):
        self.loginer = self.login()

    def login(self, username="demo", password="P@ssw0rd123.."):
        url = "https://demo.halo.run/api/admin/login"
        h = {"Content-Type": "application/json"}
        #  将正文中的null  改成None

        # d1 ={
        #         "authcode": None,
        #         "password": f"{password}",
        #         "username": f"{username}"
        #     }
        # res = requests.post(url, json=d1)
        # print(d1,type(d1))

        # data利用data传输
        d2 = f'{"authcode":null,"password":f"{password}","username":f"{username}"}'
        d2 = json.dumps(d2)
        # print(d2,type(d2))        #
        res = requests.post(url, data=d2, headers=h)
        print(res.text)
        return res

    def test_login(self, username, password, ex):
        res = self.login(username, password).json()
        if res["message"] == ex:
            print(f"测试成功 期望结果{ex} 实际结果{res['message']}")
        else:
            print(f"测试失败 期望结果{ex} 实际结果{res['message']}")

    def journal(self, words):
        res = json.loads(self.loginer.text)
        self.access_token = res["data"]["access_token"]
        url = "https://demo.halo.run/api/admin/journals"
        h = {"Admin-Authorization": f"{self.access_token}", "Content-Type": "application/json"}
        d = {
            "sourceContent": f"{words}"
        }
        b = json.dumps(d)
        res = requests.post(url, data=b, cookies=self.loginer.cookies, headers=h)
        print(res.text)


if __name__ == '__main__':
    a = Halointerface()
    #  用户名或者密码不正确
    #   ok
    res = a.login()
    # print(res.json())
    # res = a.test_login("demo","P@ssw0rd12","OK")
    # res = a.journal("asdasfasfsa")
