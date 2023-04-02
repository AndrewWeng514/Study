# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : aaatestwoniusales.py
@desc: 
@Created on: 2022/9/20 18:53
"""
import json
import time

import pytest

from interface.business.woniusales import WoniuSalesInterface
from interface.common.db import DB
from interface.data.woniusalesdata import *


class TestWoniuSales:

    def setup_class(self):
        self.wn = WoniuSalesInterface()
        self.db = DB("woniusales")

    @pytest.mark.parametrize("username,password,verifycode,expect", logindata)
    def test_login(self, username, password, verifycode, expect):
        res = self.wn.login(username, password, verifycode)
        assert res.text == expect

    @pytest.mark.parametrize("barcode", barcodedata)
    def test_querybarcode(self, barcode):
        res = self.wn.querybarcode(barcode)

        resobj = json.loads(res.text)  # 将json格式的响应正文变成python1数据类型  方便我们进行校验

        # 格式处理
        if resobj:  # 条件成立说明有数据
            del resobj[0]["createtime"]  # 删除数据中的"createtime"

        sql = f'SELECT goodsserial,goodsname,barcode,unitprice from goods WHERE barcode ="{barcode}" ORDER BY goodsid DESC LIMIT 1'
        dbres = self.db.fetchall(sql)
        assert resobj == dbres

    @pytest.mark.parametrize("phone,name,sex,date,kids,cloth,expect", addvipdata)
    def test_addvip(self, phone, name, sex, date, kids, cloth, expect):
        res = self.wn.addvip(phone, name, sex, date, kids, cloth)  # 调用新增会员接口 得到接口的响应对象
        assert res.text == expect

        # 结合数据库校验
        # 已经存在
        if expect == "already-added":
            sql = f"SELECT * from customer WHERE customerphone='{phone}' "
        # 新增成功
        else:
            sql = f'SELECT * from customer WHERE customerphone="{phone}" and customername="{name}" and ' \
                  f'childsex="{sex}" and childdate="{date}" and creditkids="{kids}" and creditcloth="{cloth}"'

        res = self.db.fetchone(sql)
        assert res  # 期望是能查到结果 如果为None就有问题

    @pytest.mark.parametrize("batchname,batchfile", uploadanddeletedat)
    def testuploadanddelete(self, batchname, batchfile):
        res = self.wn.upload(batchname, batchfile)  #
        # json.loads(res.text)
        if "json" in res.headers["Content-Type"]:
            resobj = res.json()  # 得到json响应对象的python类型数据
        else:
            resobj = res.text
        # 结合数据库校验是否正确
        # 去数据库查询该批次数据 得到结果和 响应结果校验
        sql = f'SELECT * from goods WHERE batchname="{batchname}" order by goodsid '
        dbres = self.db.fetchall(sql)  # 查看到新增成功的结果

        # 将数据库结果进行格式化 保证两个数据格式一致
        for data in dbres:  # 循环遍历数据库查询的每个结果 得到的是一个字典
            data['createtime'] = str(data['createtime'])
        pytest.assume(dbres == resobj)  # 断言出错 不影响后面的执行

        res = self.wn.deletebatch(batchname)  # 调用删除
        # 数据校验 看是否删除成功
        dbres = self.db.fetchall(sql)  # 查看 结果 理论1上应当为空
        pytest.assume(res.text == "delete-successful" and dbres == [])  # 断言出错 不影响后面的执行

    @pytest.mark.parametrize("batchname,batchfile,expect", uploadfaildata)
    def testuploadfail(self, batchname, batchfile, expect):
        res = self.wn.upload(batchname, batchfile)  #
        # json.loads(res.text)
        # resobj = res.json()  # 得到json响应对象的python类型数据
        assert res.text == expect


if __name__ == '__main__':
    pass
    pytest.main()
    # tw = TestWoniuSales()
    # tw.test_login("admin","123456","0000","login-pass")
    # # tw.test_login("admin","123456","0000","login-pass") #
    # # tw.test_login("admin","12345","0000","login-fail") #
    # tw.test_login("admin","12345","00","vcode-erro") #
    # # tw.test_querybarcode("123456") #
    # # tw.test_querybarcode("1248148415656488") #
    # # tw.test_addvip("18682558655",expect="already-added")
    # from  faker import  Faker
    # f = Faker("zh_cn")
    # # tw.test_addvip(f.phone_number(),f.name(),f.random.choice(["男","女"]),str(f.date_between(start_date='-10y',end_date='today')),expect="add-successful")
    # # tw.testuploadanddelete("GB20220928",r"D:\Pycharm\PythonProject\python67\interface\data\a.xls")
    # tw.testuploadfail("GB20220931",r"F:\VideoRecording\网易云音乐测试用例.xls","format-error")
    # tw.testuploadfail("GB20220920",r"D:\Pycharm\PythonProject\python67\interface\data\a.xls","already-imported")
    # # 在死循环 生成随机数
    # 校验随机数
    # 有 重新生成
    # 没有 退出循环 直接使用
