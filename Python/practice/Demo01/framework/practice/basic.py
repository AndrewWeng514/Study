"""
 @Author: Andrew
 @FileName: base.py
 @DateTime: 2022/10/17 9:22
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 实例化新的浏览器,
s = Service(executable_path="../../UI/chromedriver.exe")
dr = webdriver.Chrome(service=s)
dr.maximize_window()
dr.get('http://192.168.4.89:8080/WoniuBoss4.0/login')

# 登录
# dr.find_element('name','userName').send_keys("WNCD000")
dr.find_element('xpath', '//input[@placeholder="请输入用户名"]').send_keys('WNCD000')

dr.find_element('name', 'userPass').send_keys("woniu123")
dr.find_element('name', 'checkcode').send_keys("0000")
dr.find_element('xpath', '//button[@onclick="login();"]').click()

if dr.find_element('link text', '[注销]'):
    print('登陆成功')
else:
    print('登录失败')

time.sleep(3)
dr.quit()
