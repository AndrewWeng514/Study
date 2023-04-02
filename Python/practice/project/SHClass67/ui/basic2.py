"""
解决警告问题
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s = Service(executable_path='geckodriver.exe')

dr = webdriver.Firefox(service=s)

dr.maximize_window()

dr.get('http://192.168.18.128:8080/woniusales')

dr.find_element('id', 'username').send_keys('admin')
# 查找密码输入框元素，然后输入123456
dr.find_element('id', 'password').send_keys('123456')
# 查找验证码输入框，然后输入0000
dr.find_element('id', 'verifycode').send_keys('0000')
# 查找登录按钮，然后点击
dr.find_element('class name', 'form-control.btn-primary').click()
