"""
 @Author: Andrew
 @FileName: asset_page.py
 @DateTime: 2022/10/17 18:34
 @Brief:进入采购登记界面
"""
import time

from Demo01.framework.config.config import ip
from Demo01.framework.login.login_page import LoginPage
from Demo01.framework.basic.base import Base


class AssetPage(Base):
    button_add = ('xpath', '//button[text()="新增"]')

    button_asset_name = ('xpath', "(//select[@name='ass.assets_name'])")
    button_asset_type = ('xpath', "(//select[@name='ass.assets_type'])")
    button_asset_code = ('xpath', "(//input[@name='ass.bar_code'])")
    button_asset_price = ('xpath', "(//input[@name='ass.price'])")
    button_asset_time = ('xpath', "(//input[@name='ass.purchase_time'])")
    button_asset_today = ('xpath', "(//th[@class='today'])")
    button_asset_purchase_employee = ('xpath', "(//input[@name='purchase_employee'])")
    button_asset_note = ('xpath', "(//input[@name='ass.note'])")
    button_asset_owner = ('xpath', "(//select[@name='ass.assets_owner'])")

    button_asset_save = ('xpath', "(//button[@id='addAssBtn'])")

    def __init__(self):
        super().__init__()
        LoginPage().login_page()

    def add_asset(self, asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
                  asset_owner):
        time.sleep(2)
        self.dr.get(f"http://{ip}:8080/WoniuBoss4.0/assets")
        self.click(self.button_add)

        self.select(('xpath', "(//select[@name='ass.assets_name'])[2]"), asset_name)
        # self.selects(self.button_asset_name,1,asset_name)
        self.selects(self.button_asset_type, 1, asset_type)
        self.inputs(self.button_asset_code, 1, asset_code)
        self.inputs(self.button_asset_price, 1, asset_price)

        self.clicks(self.button_asset_time, 2)
        self.clicks(self.button_asset_today, 2)  # 日历

        self.inputs(self.button_asset_purchase_employee, 2, asset_purchase_employee)
        self.inputs(self.button_asset_note, 2, asset_note)
        self.selects(self.button_asset_owner, 2, asset_owner)

        self.clicks(self.button_asset_save, 1)
        # ele = self.dr.find_elements('xpath',"(//select[@name='ass.assets_name'])")
        # sk = Select(ele)
        # sk.select_by_visible_text(asset_name)


if __name__ == '__main__':
    a = AssetPage()
    a.add_asset("电脑", "T400", 123213, 123, '张三', "无", "公司")

    time.sleep(5)
    a.dr.quit()
