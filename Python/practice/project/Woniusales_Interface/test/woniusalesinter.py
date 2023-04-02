# @Date   : 2022/9/20 19:34
# @Author : Andrew
# @Name   : woniusalesinter
import json
import random
import time

import requests

# cookies
from project.Woniusales_Interface.common.db import DB
from faker import Faker

"""
url = "http://192.168.6.4:8080/woniusales/user/login"
info ={
    "username": "admin",
    "password": "123456",
    "verifycode": "0000"
}
reslogin = requests.post(url,data=info)
urlsell = "http://192.168.6.4:8080/woniusales/"
ressell = requests.get(urlsell,cookies = reslogin.cookies)
print(ressell.content)
print(ressell.request.headers)
with open("a.html","wb") as file:
    file.write(ressell.content)

"""

#   session
"""
s = requests.session()
url = "http://192.168.6.4:8080/woniusales/user/login"
info ={
    "username": "admin",
    "password": "123456",
    "verifycode": "0000"
}
reslogin = s.post(url,data=info)
urlsell = "http://192.168.6.4:8080/woniusales/"
res = s.get(urlsell)
with open("b.html","wb") as f:
    f.write(res.content)
print(res.request.headers)
"""


class Wonniusales:
    url_login = "http://localhost:8080/woniusales/user/login"
    url_barcode = 'http://localhost:8080/woniusales/sell/barcode'
    url_add_guest = 'http://localhost:8080/woniusales/customer/add'

    def __init__(self):
        self.loginer = self.login()

    #  cookies  登录
    def login(self, username='admin', password="123456", verifycode='0000'):
        # url = "http://localhost:8080/woniusales/user/login"
        info = {
            "username": f"{username}",
            "password": f"{password}",
            "verifycode": f"{verifycode}"
        }
        res = requests.post(self.url_login, data=info)
        return res

    #  session 登录
    def login2(self, username='admin', password="123456", verifycode='0000'):
        sess = requests.session()
        info = {
            "username": f"{username}",
            "password": f"{password}",
            "verifycode": f"{verifycode}"
        }
        res = sess.post(self.url_login, data=info)
        return sess

    def barcode(self, barcode):
        res = self.login("admin", "123456", "0000")
        code = {
            "barcode": f"{barcode}"
        }
        res_barcode = requests.post(self.url_barcode, cookies=res.cookies, data=code)
        return res_barcode

    def test_barcode(self, barcode):
        res = self.barcode(barcode)
        # print(res.text, type(res.text))
        res_web = json.loads(res.text)
        # print(res_web,type(res_web))
        if res_web:
            res_web[0].pop("createtime")
            print(res_web, type(res_web))

        sql = f'SELECT goodsserial,goodsname,barcode,unitprice from goods WHERE barcode = {barcode} ORDER BY goodsid DESC limit 1'
        res_sql = DB().fetchall(sql)
        if res_sql == res_web:
            print(f"测试成功 实际结果{res_web},预期结果{res_sql}")
        else:
            print(f"测试不成功 实际结果{res_web},预期结果{res_sql}")
            # res_barcode = res.text[0]["createtime"]
        #

    def add_guest(self, sess, customerphone, customername='未知', childsex="男", childdate=time.strftime("%Y-%m-%d"),
                  creditkids='0', creditcloth='0'):
        info = {
            "customername": f"{customername}",
            "customerphone": f"{customerphone}",
            "childsex": f"{childsex}",
            "childdate": f"{childdate}",
            "creditkids": f"{creditkids}",
            "creditcloth": f"{creditcloth}"
        }
        res_guest = sess.post(self.url_add_guest, data=info)
        return res_guest

    def test_add_guest(self, sess, customerphone, customername='未知', childsex="男",
                       childdate=time.strftime("%Y-%m-%d"), creditkids='0', creditcloth='0', expect=''):
        res = self.add_guest(sess, customerphone, customername, childsex, childdate, creditkids, creditcloth)
        if res.text == expect:
            print(f'新增成功 期望结果{expect} 实际结果{res.text}')
        else:
            print(f'新增失败 期望结果{expect} 实际结果{res.text}')

    #  上传批次文件
    def upload(self, batchname, fileaddress):
        url = "http://localhost:8080/woniusales/goods/upload"
        d = {"batchname": batchname}
        f = {"batchfile": open(fileaddress, 'rb')}
        res = requests.post(url, data=d, files=f, cookies=self.loginer.cookies)
        return res

    def test_upload(self, batchname, fileaddress):
        res = self.upload(batchname, fileaddress)
        res_web = res.json()

        print(res_web, type(res_web))

        sql = f"SELECT * from goods WHERE batchname = '{batchname}'ORDER BY goodsid"
        res_sql = DB().fetchall(sql)
        for data in res_sql:
            data['createtime'] = str(data['createtime'])  # 将time转化为标准格式

        print(res_sql, type(res_sql))
        if res_web == res_sql:
            print(f"测试成功 显示导入数据{res_web}")
            print(f"测试成功 数据库中数据{res_sql}")
        else:
            print(f"测试失败 显示导入数据{res_web}")
            print(f"测试失败 数据库中数据{res_sql}")

    #  删除上传信息
    def deleted(self, batchname):
        url = "http://localhost:8080/woniusales/goods/deletebatch"
        d = {"batchname": batchname}
        res = requests.post(url, cookies=self.loginer.cookies, data=d)
        # print(res.text)
        return res

    def test_deleted(self, batchname, expect):
        res = self.deleted(batchname)
        if res.text == expect:
            sql = f"SELECT * from goods WHERE batchname = '{batchname}'"
            res_sql = DB().fetchall(sql)
            # print(res_sql,type(res_sql))
            if not res_sql:  # 如果sql查询为空
                print(f"测试成功 期望结果{expect} 实际结果{res.text}")
            else:
                print(f"测试失败  数据库中存在{batchname}信息")
        else:
            print(f"测试失败 期望结果{expect} 实际结果{res.text}")


if __name__ == '__main__':
    test = Wonniusales()
    f = Faker("zh_cn")
    sess = test.login2()
    # res=test.add_guest(sess,"123241")
    # print(res.text)
    # res = test.add_guest(sess,f.phone_number(),f.name(),f.random.choice(["男","女"]),str(f.date_between(start_date="-30d",end_date = "today")))
    # print(res.text)
    res = test.test_upload('GB2022092125', r"C:\Users\Andrew\Desktop\autoTest.xls", )

    res1 = test.test_deleted('GB2022092125', 'delete-successful')
