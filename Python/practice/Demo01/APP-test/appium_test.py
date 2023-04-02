"""
 @Author: Andrew
 @FileName: appium_test.py
 @DateTime: 2022/10/13 14:57
"""
import appium
from appium import webdriver


class Appium:
    def __init__(self):
        addr = 'http://127.0.0.1:4723/wd/hub'
        cpas = {"platformName": "Android",
                "platformVersion": "7.1.2",
                "deviceName": "Appium",
                "unicodeKeyboard": True,
                "appPackage": "com.wondertek.paper",
                "appActivity": "cn.thepaper.paper.ui.splash.welcome.LaunchActivity",
                "udid": "127.0.0.1:62001",
                "noReset": False
                }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cpas)

    def test(self):
        self.dr.implicitly_wait(15)
        self.dr.find_element("id", 'com.wondertek.paper:id/know').click()

        self.dr.find_element("xpath",
                             '//android.widget.LinearLayout[@resource-id="com.wondertek.paper:id/bottomBar"]/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.TextView').click()

        self.dr.find_element('id', 'com.wondertek.paper:id/one_key_confirm').click()

        self.dr.find_element('id', 'com.wondertek.paper:id/input_phone').send_keys("13127534369")
        self.dr.find_element('id', 'com.wondertek.paper:id/input_verification_code').send_keys("4369")

        # self.dr.find_element('id','	com.wondertek.paper:id/checkbox_agreement').click()
        self.dr.find_element('id', 'com.wondertek.paper:id/confirm').click()

        if self.dr.find_element('id', 'com.wondertek.paper:id/ok').text == '阅读并同意':
            print('测试成功')
        else:
            print('测试失败')


if __name__ == '__main__':
    a = Appium()
    a.test()
