# @Date   : 2022/9/23 16:37
# @Author : Andrew
# @Name   : test_sell
import json
import pytest
from project.Woniusales_Interface.common.db import DB
from project.pytestwoniusales.business.sell import Sell
from project.pytestwoniusales.data.testdata import barcodedata


class TestSell:

    @pytest.mark.parametrize("barcode", barcodedata)
    def test_barcode(self, barcode):
        res = Sell().barcode(barcode)
        # print(res.text, type(res.text))
        res_web = json.loads(res.text)
        # print(res_web,type(res_web))
        if res_web:
            res_web[0].pop("createtime")
            print(res_web, type(res_web))

        sql = f'SELECT goodsserial,goodsname,barcode,unitprice from goods WHERE barcode = {barcode} ORDER BY goodsid DESC limit 1'
        res_sql = DB().fetchall(sql)
        assert res_sql == res_web
