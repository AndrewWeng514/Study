"""
时间等待：
1、time.sleep(3) # 强制等待
2、dr.implicitly_wait(10) # 隐式等待。全局的等待方法。等待页面加载完成，最多等待10秒。
3、wait = WebDriverWait(dr,10,0.5)  # 显式等待。针对单个元素

ele = wait.until(lambda x: x.find_element('id', "username1")) # until方法中使用匿名函数

ele = wait.until(ec.presence_of_element_located(['id','username'])) # until方法中调用expected_conditions中的方法

"""
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

s = Service(executable_path='geckodriver.exe')

dr = webdriver.Firefox(service=s)

dr.maximize_window()
# dr.implicitly_wait(10)

wait = WebDriverWait(dr, 10, 0.5)

dr.get('http://192.168.18.128:8080/woniusales')
print('---------------1')
# dr.find_element('id','username').send_keys('admin')
# ele = wait.until(lambda x: x.find_element('id', "username1")) # until方法中使用匿名函数
# ele = wait.until(ec.presence_of_element_located(('id','username1')))
ele = wait.until(ec.presence_of_element_located(['id', 'username']))
ele.send_keys('admin')

# 查找密码输入框元素，然后输入123456
print('----------------2')
dr.find_element('id', 'password1').send_keys('123456')
# 查找验证码输入框，然后输入0000
print('----------------3')
dr.find_element('id', 'verifycode').send_keys('0000')
# 查找登录按钮，然后点击
print('----------------4')
dr.find_element('class name', 'form-control.btn-primary').click()
