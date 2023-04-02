"""
 @Author: Andrew
 @FileName: test_assets_up.py
 @DateTime: 2022/10/18 15:46
 @Brief:
"""
import random
import time

from Demo01.framework.basic.closer import wrapper
from Demo01.framework.basic.xls import read_xls_up
from Demo01.framework.config.config import bossdb
from asset_page import AssetPage
from Demo01.framework.basic.database import Common

from selenium.webdriver.common.by import By


class TestAssets:
    # 实例化数据库,打开新增界面
    def __init__(self):
        self.test = AssetPage()
        self.db_object, self.sheet_object = Common.openDB(*bossdb)

    # 随机生成一个与数据库不同的条形码
    def get_barcode(self):
        sql = "select bar_code from assets"
        code_result = Common.readDB(self.sheet_object, sql)
        while True:
            bar_code = random.randint(11111111111, 99999999999)
            if bar_code not in code_result:
                break
        # print(bar_code)
        return bar_code

    # 新增成功的测试脚本
    # asset_name 全部,电脑 投影仪 打印机 其它 asset_type,asset_code,asset_price,asset_purchase_employee,asset_note, asset_owner
    def test_asset_success(self, asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
                           asset_owner):
        self.test.add_asset(asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
                            asset_owner)
        sql = f"select * from assets where bar_code = {asset_code}"
        result = Common.readDB(self.sheet_object, sql)
        if result:
            print("测试成功")
        else:
            print('测试失败')

    # 新增失败的测试脚本
    @wrapper(*read_xls_up("../testdata/assets-test-case.xls", 'Sheet1'))
    def test_asset_fail(self, case_id, case_name, asset_name, asset_type, asset_code, asset_price,
                        asset_purchase_employee, asset_note, asset_owner, by, values, exp):
        self.test.add_asset(asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
                            asset_owner)
        print((by, values))
        print(self.test.dr.find_element(By.CLASS_NAME, 'bootbox-body').text)
        time.sleep(1)
        if self.test.dr.find_element(By.CLASS_NAME, 'bootbox-body').text == exp:
            print(f"{case_id},{case_name},测试成功")
        else:

            print(f"{case_id},{case_name},测试失败")

    def main_fail(self, filead, sheetname):
        cases = read_xls_up(filead, sheetname)
        print(cases)
        for i in cases:
            print(*i)
            self.test_asset_fail(*i)


if __name__ == '__main__':
    t = TestAssets()
    # t.get_barcode()
    t.test_asset_fail()
    # t.main_fail("../testdata/assets-test-case.xls",'Sheet1')
    # t.test_asset_success("电脑","T430",15241362142,125,"张三",'无','公司')

    time.sleep(2)
    t.test.dr.quit()
