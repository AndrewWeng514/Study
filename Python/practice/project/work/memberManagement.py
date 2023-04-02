# @Time    : 2022/9/16 23:16
# @Author  : Andrew
import time

from project.work.common.common_dr import GetDriver
from project.work.login import Login
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains


class Member:
    mem_button = ('xpath', '//span[text()="会员管理"]')
    mem_list_button = ('xpath', '//span[text()="会员列表"]')
    mem_list_add_button = ('xpath', '//span[text()="添加新会员"]')
    mem_list_infos = ('xpath', '//input[@class="el-input__inner"]')
    men_list_lever = ('class name', 'el-select-dropdown__item')
    men_list_verifys = ('xpath', '//button[@class="el-button el-button--primary"]')

    def __init__(self):
        # 实例化浏览器
        self.login = Login().admin_login()
        self.dr = GetDriver().get_driver_chrom()
        self.dr.find_element(*self.mem_button).click()
        self.action = ActionChains(self.dr)
        self.dr.find_element(*self.mem_list_button).click()

    def add_men(self, name, birth, phonenum, level):
        try:
            self.login.admin_login()
        except:
            pass

        self.dr.find_element(*self.mem_list_add_button).click()

        self.dr.find_elements(*self.mem_list_infos)[2].clear()  # 姓名
        self.dr.find_elements(*self.mem_list_infos)[2].send_keys(name)  # 姓名

        self.dr.find_elements(*self.mem_list_infos)[3].clear()  # 生日
        self.dr.find_elements(*self.mem_list_infos)[3].send_keys(birth)  # 生日
        pyautogui.click(1367, 340)

        self.dr.find_elements(*self.mem_list_infos)[4].clear()  # 联系电话
        self.dr.find_elements(*self.mem_list_infos)[4].send_keys(phonenum)  # 联系电话

        #  会员方式
        time.sleep(2)
        ele = self.dr.find_elements(*self.mem_list_infos)[5]
        self.action.click(ele)
        self.action.perform()
        if level == '周卡':
            self.dr.find_elements(*self.men_list_lever)[4].click()
        elif level == '月卡':
            self.dr.find_elements(*self.men_list_lever)[5].click()
        else:
            self.dr.find_elements(*self.men_list_lever)[6].click()
        # 会员方式

        # 点击确认后会直接成功
        time.sleep(1)
        ele2 = self.dr.find_elements(*self.men_list_verifys)[0]
        self.action.click(ele2)
        self.action.perform()


##  class="el-button el-button--primary"[1]


if __name__ == '__main__':
    mem = Member()
    mem.add_men('张三3', '2020-01-12', 13127534, '周卡')

    time.sleep(5)
    mem.dr.quit()
