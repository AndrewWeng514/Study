"""
find_element()和find_elements()方法讲解
"""
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 实例化chromedriver服务
s = Service(executable_path='chromedriver.exe')
# 实例化Chrome对象。打开chrome浏览器
dr = webdriver.Chrome(service=s)
# 最大化浏览器
dr.maximize_window()
# 访问网址
dr.get('http://192.168.18.128:8080/woniusales')
# 查找用户名输入框元素，然后输入admin
# ele = dr.find_element('xpath','//label[@for="username"]')
# ele = dr.find_element('id','username')
# print(ele.is_enabled())
# ele.click()
# print(ele.is_selected())
# ele.send_keys('12345')
# print(ele.text) # 获取元素的文本信息
# time.sleep(3)
# ele.clear() # 清空输入框中的内容
# print(ele.get_attribute('class')) # 获取元素某个属性的值
# print(ele.get_property('name')) # 获取元素某个属性的值
# print(ele.is_enabled())
# print(ele.is_selected())
eles = dr.find_elements('tag name', 'input')
# print(eles)
s = 'abcdefghigklm123456'
content = random.choices(s, k=8)
content = ''.join(content)
for ele in eles:
    ele.send_keys(content)
dr.find_element('xpath', '''//*[@onclick="doLogin('null')"]''').click()
