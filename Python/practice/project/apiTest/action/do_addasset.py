"""
 @Author: Andrew
 @FileName: do_addasset.py
 @DateTime: 2022/10/19 15:46
 @Brief:新增资产的接口
"""
from project.apiTest.action.do_login import Login
from project.apiTest.tools.common import Common


class AddAsset:
    def __init__(self):
        Login().do_login()
        self.sess = Common.get_session()

    def add_asset1(self):
        url = 'http://101.34.13.184:8080/WoniuBoss4.0/assets/addAss'
        data = {
            "ass.assets_name": "01",
            "ass.assets_type": "01",
            "ass.bar_code": "23123221231",
            "ass.price": "250",
            "purchase_employee": "李四",
            "ass.purchase_employee_id": "4",
            "ass.purchase_time": "2022-10-01",
            "ass.note": "API",
            "ass.assets_owner": "01"
        }
        head = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        add_asset = self.sess.post(url=url, data=data, headers=head)
        print(add_asset.text)

    def add_asset(self, url, request, head, data):
        # print(url,type(url),request,type(request),head,type(head),data,type(data),sep="\n")
        # url = url
        # data = data
        # head = head
        add_asset = None
        if request == "post":
            add_asset = self.sess.post(url=url, data=data, headers=head)
            # print(add_asset.text)
        elif request == "get":
            add_asset = self.sess.get(url=url, params=data)
        elif request == "put":
            add_asset = self.sess.put(url, data)
        elif request == "delete":
            add_asset = self.sess.delete(url=url, params=data)
        return add_asset

    # 带有文件上传
    def add_asset2(self, url, request, head, data, file):
        # print(url,type(url),request,type(request),head,type(head),data,type(data),sep="\n")
        # url = url
        # data = data
        # head = head
        add_asset = None
        if request == "post":
            if file == "":
                add_asset = self.sess.post(url=url, data=data, headers=head)
            else:
                add_asset = self.sess.post(url=url, data=data, headers=head, files=file)

            # print(add_asset.text)
        elif request == "get":
            add_asset = self.sess.get(url=url, params=data)
        elif request == "put":
            add_asset = self.sess.put(url, data)
        elif request == "delete":
            add_asset = self.sess.delete(url=url, params=data)
        return add_asset


if __name__ == '__main__':
    a = AddAsset()
