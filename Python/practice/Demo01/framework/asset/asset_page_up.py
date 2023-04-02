"""
 @Author: Andrew
 @FileName: asset_page_up.py
 @DateTime: 2022/10/18 15:38
 @Brief:
"""
import time
from Demo01.framework.config.config import ip
from Demo01.framework.login.login_page import LoginPage
from Demo01.framework.basic.base import Base


class AssetPage(Base):
    button_add = ('xpath', '//button[text()="新增"]')

    button_asset_name = ('xpath', "(//select[@name='ass.assets_name'])[2]")
    button_asset_type = ('xpath', "(//select[@name='ass.assets_type'])[2]")
    button_asset_code = ('xpath', "(//input[@name='ass.bar_code'])[2]")
    button_asset_price = ('xpath', "(//input[@name='ass.price'])[2]")
    button_asset_time = ('xpath', "(//input[@name='ass.purchase_time'])[3]")
    button_asset_today = ('xpath', "(//th[@class='today'])[3]")
    button_asset_purchase_employee = ('xpath', "(//input[@name='purchase_employee'])[3]")
    button_asset_note = ('xpath', "(//input[@name='ass.note'])[3]")
    button_asset_owner = ('xpath', "(//select[@name='ass.assets_owner'])[3]")

    button_asset_save = ('xpath', "(//button[@id='addAssBtn'])[2]")

    def __init__(self):
        super().__init__()
        LoginPage().login_page()

    def add_asset(self, asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
                  asset_owner):
        time.sleep(2)
        self.dr.get(f"http://{ip}:8080/WoniuBoss4.0/assets")
        self.click(self.button_add)
        self.select(self.button_asset_name, asset_name)
        self.select(self.button_asset_type, asset_type)
        self.input(self.button_asset_code, asset_code)
        self.input(self.button_asset_price, asset_price)

        self.click(self.button_asset_time)
        self.click(self.button_asset_today)  # 日历

        self.input(self.button_asset_purchase_employee, asset_purchase_employee)
        self.input(self.button_asset_note, asset_note)
        self.select(self.button_asset_owner, asset_owner)

        self.click(self.button_asset_save)


if __name__ == '__main__':
    a = AssetPage()
    a.add_asset("电脑", "T400", 123213, 123, '张三', "无", "公司")

    time.sleep(5)
    a.dr.quit()
