# @Time    : 2022/9/13 17:15
# @Author  : Andrew
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# class By:
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
s = Service(executable_path='geckodriver.exe')
dr1 = webdriver.Firefox(service=s)
dr1.maximize_window()
dr1.get("http://192.168.4.32:8080/woniusales/")  # 打开蜗牛进销存

# dr1.find_element(By.ID,"username").send_keys("admin")#寻找用户名框并输入
# dr1.find_element("id","username").send_keys("admin")
dr1.find_element(By.CSS_SELECTOR, "#username").send_keys('admin')

# dr1.find_element(By.NAME,"pwd").send_keys("123456")#寻找密码框并输入
dr1.find_element(By.CSS_SELECTOR, "input#password").send_keys("123456")

dr1.find_elements(By.TAG_NAME, "input")[2].send_keys("0000")  # 寻找验证码框并输入
time.sleep(4)
# 7、xpath。通过xpath来定位。
# dr.find_element('xpath','//input[@name="pwd"]')
# dr.find_element(By.XPATH,'//input[@id="username"]')
# /：根节点
# //:当前节点
# @:选取属性
# *：通配符，匹配所有标签
# //标签名[@属性="属性值"]
# //标签名[text()="文本值"]
# //标签名[contains(@属性,"属性值中的一部分")]
# dr1.find_element("xpath",'//button[@class="form-control btn-primary"]').click()
# dr1.find_element("xpath",'''//button[@onclick="doLogin('null')"]''').click()
# dr1.find_element("xpath",'//button[text()=" 登录"]').click()
dr1.find_element("xpath", '//button[contains(text(),"登录")]').click()
# dr1.find_element('class name',"form-control.btn-primary").click()#寻找登录按钮并点击
# dr1.find_element(By.CLASS_NAME,"form-control.btn-primary").click()
# dr1.refresh()
# time.sleep(2)
# dr1.back()
# dr1.forward()
# dr1.minimize_window()
# dr1.quit()
try:

    dr1.find_element(By.LINK_TEXT, "注销")
except:
    print("登录失败!")

else:
    print("登录成功!")
    dr1.find_element(By.ID, "barcode").send_keys("6955203636348")
    dr1.find_element(By.CLASS_NAME, "form-control.btn-primary").click()
    # dr1.find_element(By.CLASS_NAME,"form-control.btn-block.btn-primary").click()
    # print(dr1.switch_to.alert.text)
    # dr1.switch_to.alert.accept()
    # time.sleep(2)
    # print(dr1.switch_to.alert.text)
    # dr1.switch_to.alert.accept()
    # time.sleep(1)
    # dr1.find_element('xpath','//button[@onclick="queryByBarCode()"]').click()
    # time.sleep(1)
    # dr1.find_element('xpath','//button[@data-bb-handler="ok"]').click()
    ele = dr1.find_element('xpath', '//select[@id="paymethod"]')
    pay_method = Select(ele)
    pay_method.select_by_index(3)
    time.sleep(1)
    pay_method.select_by_value('刷卡')
    time.sleep(1)
    pay_method.select_by_visible_text('支付宝')
