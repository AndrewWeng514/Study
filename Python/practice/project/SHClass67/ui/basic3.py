"""
八大定位方法
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

# 实例化chromedriver服务
s = Service(executable_path='chromedriver.exe')
# 实例化Chrome对象。打开chrome浏览器
dr = webdriver.Chrome(service=s)

# 最大化浏览器
dr.maximize_window()
# 访问网址
dr.get('http://192.168.18.128:8080/woniusales')
# 查找用户名输入框元素，然后输入admin
# dr.find_element('id','username').send_keys('admin')
# 通过By类的ID属性类定位
# dr.find_element(By.ID,"username").send_keys('admin')
# 通过xpath来定位
# dr.find_element(By.XPATH,'//input[@id="username"]').send_keys('admin')
# dr.find_element('xpath','//input[contains(@id,"name")]').send_keys('admin')
# dr.find_element(By.CSS_SELECTOR,'#username').send_keys('admin')
# dr.find_element(By.CSS_SELECTOR,'input#username').send_keys('admin')
time.sleep(3)
dr.find_element(By.CSS_SELECTOR, 'form.form-inline>div:nth-child(2)>input').send_keys('admin')
# 查找密码输入框元素，然后输入123456
# dr.find_element('id','password').send_keys('123456')
# dr.find_element(By.NAME,"pwd").send_keys('123456')
# dr.find_element('name','pwd').send_keys('123456')
# dr.find_element('xpath','//input[@name="pwd"]').send_keys('123456')
# dr.find_element(By.CSS_SELECTOR,'.form-control').send_keys('123456')
dr.find_elements(By.CSS_SELECTOR, '.form-control')[1].send_keys('123456')
# 查找验证码输入框，然后输入0000
dr.find_element('id', 'verifycode').send_keys('0000')
# dr.find_elements(By.TAG_NAME,'input')[2].send_keys('0000')
# dr.find_elements('tag name','input')[2].send_keys('0000')

# 查找登录按钮，然后点击
# dr.find_element('class name','form-control.btn-primary').click()
# dr.find_element('xpath','//button[text()="登录"]').click()
# dr.find_element('xpath','//button[contains(text(),"登录")]').click()
dr.find_element('xpath', '''//*[@onclick="doLogin('null')"]''').click()
# 等待5秒
time.sleep(5)
# 使用link text方式来定位
# dr.find_element(By.LINK_TEXT,"注销").click()
# dr.find_element('link text',"注销").click()


# 使用partial link text来定位。
# dr.find_element(By.PARTIAL_LINK_TEXT,"admin").click()
dr.find_element('partial link text', "管理员").click()
"""


"""
