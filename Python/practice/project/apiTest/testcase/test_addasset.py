"""
 @Author: Andrew
 @FileName: test_addasset.py
 @DateTime: 2022/10/19 16:57
 @Brief:测试新增的脚本
"""
import random

from project.apiTest.tools.common import Common
from project.apiTest.action.do_addasset import AddAsset


class TestAddAsset:
    def __init__(self):
        self.asset = AddAsset()

    def get_barcode(self):
        sql = "select bar_code from assets"
        code_result = Common.operate_db("r", sql)
        # print(code_result)
        while True:
            bar_code = random.randint(11111111111, 99999999999)
            if bar_code not in code_result:
                break
        # print(bar_code)
        return bar_code

    @Common.wrapper(*Common.read_excel1("asset.xls", "Sheet1"))
    def test_asset(self, case_id, case_name, url, request, head, data, exp):
        # print(url,type(url),request,type(request),head,type(head),data,type(data),sep="\n")
        #  如果条形码为none 则随机生成一个新的条形码
        if data['ass.bar_code'] is None:
            data['ass.bar_code'] = self.get_barcode()
        # print(data['ass.bar_code'])
        add_result = self.asset.add_asset(url, request, head, data)
        if add_result.text == exp:
            print(f'{case_id},{case_name}测试成功')
        else:
            print(f'{case_id},{case_name}测试失败')


if __name__ == '__main__':
    a = TestAddAsset()
    a.test_asset()
    # a.get_barcode()
