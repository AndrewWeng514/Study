import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui

# 实例化chromedriver服务
s = Service(executable_path='../ui/chromedriver.exe')
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
dr.find_element('id', 'submit').click()
time.sleep(2)
# dr.save_screenshot('./webdrivertest.png')
pyautogui.screenshot('./pyautotest.png')
