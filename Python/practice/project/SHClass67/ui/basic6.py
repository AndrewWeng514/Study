"""
下拉框的操作
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.select import Select


# 实例化chromedriver服务
from selenium.webdriver.support.select import Select

s = Service(executable_path='chromedriver.exe')
# 实例化Chrome对象。打开chrome浏览器
dr = webdriver.Chrome(service=s)

# 最大化浏览器
dr.maximize_window()
# 访问网址
dr.get('http://192.168.18.128:8080/woniusales')
# 查找用户名输入框元素，然后输入admin
dr.find_element('id', 'username').send_keys('admin')
# 查找密码输入框元素，然后输入123456
dr.find_element('id', 'password').send_keys('123456')
# 查找验证码输入框，然后输入0000
dr.find_element('id', 'verifycode').send_keys('0000')
# 查找登录按钮，然后点击
dr.find_element('class name', 'form-control.btn-primary').click()

ele = dr.find_element('id', 'paymethod')  # 定位下拉框
skfs = Select(ele)  # 实例化Select类，参数是一个web元素
# skfs.select_by_value('刷卡') # 通过option标签的value属性的值来选择
# skfs.select_by_visible_text('微信') # 通过option标签对应的文本值来选择
skfs.select_by_index(4)  # 通过option标签的索引来选择，索引值从0开始
