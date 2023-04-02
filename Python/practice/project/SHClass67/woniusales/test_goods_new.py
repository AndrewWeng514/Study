"""
文件上传处理方法
"""
import time

from project.SHClass67.woniusales.test_login_new import TestLogin
from selenium.webdriver.common.action_chains import ActionChains

"""
pip install uiautomation
"""
import uiautomation


class TestGoods:
    def __init__(self):
        # self.dr = GetDriver.get_driver()
        self.login = TestLogin()

    def test_case_1(self):
        """
        第一种方法：
        直接定位文件上传输入框，然后调用send_keys方法
        """
        try:
            self.login.login()
        except:
            pass
        self.login.dr.find_element('link text', '批次管理').click()
        self.login.dr.find_element('id', 'batchname').send_keys('GB20220916')
        self.login.dr.find_element('id', 'batchfile').send_keys(r'C:\Users\Administrator\Desktop\autoTest.xls')
        self.login.dr.find_element('xpath', '//input[@value="确认导入本批次商品信息"]').click()
        print('case1测试完成')

    def test_case_2(self):
        """
        第二种方法：
        纯粹的模拟手工操作的执行步骤
        uiautomation库：封装了对windows对象的操作方法
        ControlType决定使用哪个类来定位控件。
        因为input框不一定能够点击，所以使用键盘和鼠标的操作来实现单击
        """
        try:
            self.login.login()
        except:
            pass
        self.login.dr.find_element('link text', '批次管理').click()
        self.login.dr.find_element('id', 'batchname').send_keys('GB20220917')
        time.sleep(3)
        # 实例化键鼠操作。参数：浏览器对象
        action = ActionChains(self.login.dr)
        # 识别我们要点击的元素
        time.sleep(2)
        ele = self.login.dr.find_element('id', 'batchfile')
        # 通过action对象的点击方法来对元素单击
        action.click(ele)
        action.perform()  # perform()方法的作用：执行action中所有的动作
        # self.login.dr.find_element('id','batchfile').click()
        # 定位文件名输入框，并且输入文件名
        time.sleep(1)
        uiautomation.EditControl(ClassName="Edit").SendKeys(r'C:\Users\Administrator\Desktop\autoTest.xls')
        # 定位“打开”按钮，并且点击
        time.sleep(1)
        uiautomation.ButtonControl(Name="打开(O)").Click()
        self.login.dr.find_element('xpath', '//input[@value="确认导入本批次商品信息"]').click()
        print('case2执行完成')


if __name__ == '__main__':
    tg = TestGoods()

    tg.test_case_2()
    tg.test_case_1()
