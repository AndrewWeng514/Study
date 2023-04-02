# @Time    : 2022/9/15 10:02
# @Author  : Andrew
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import uiautomation
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service(executable_path='../../Demo01/UI/geckodriver.exe')
dr = webdriver.Firefox(service=s)
dr.maximize_window()
dr.get("http://192.168.4.32:8080/woniusales")
s = ActionChains(dr)
dr.find_element('id', 'username').send_keys("admin")
dr.find_element('id', 'password').send_keys("123456")
# dr.find_element('id','verifycode').send_keys("0000")
#  截图
#
# dr.find_element('class name','form-control.btn-primary').click()
# dr.save_screenshot(r"C:\Users\Andrew\Desktop\shot.png")
# dr.save_full_page_screenshot(r"C:\Users\Andrew\Desktop\shot1.png")
#
# with open(r"C:\Users\Andrew\Desktop\shot2.png",mode='wb') as file:
#     file.write(png)
# b = dr.get_full_page_screenshot_as_base64()
# print(b)

#  等待时间
wait = WebDriverWait(dr, 10, 0.5)
# ele =wait.until(lambda x:x.find_element('id','verifycode1'))
# ele.send_keys('admin')
ele = wait.until(expected_conditions.presence_of_element_located(['id', 'verifycode']))
ele.send_keys('1234')

#  批次管理
# dr.find_element('link text','批次管理').click()
# dr.find_element('id','batchname').clear()
# dr.find_element('id','batchname').send_keys('GB20220915')
# dr.find_element('id','batchfile').send_keys(r"C:\Users\Andrew\Desktop\autoTest.xls")
# dr.find_element('id','batchfile').click()
# uiautomation.EditControl()


# 库存查询
"""
 修改最早入库时间
dr.find_element('link text', '库存查询').click()
js='document.getElementById("earlystoretime").removeAttribute("readonly")'
dr.execute_script(js)
dr.find_element('id','earlystoretime').send_keys("2012-12-3")
"""

time.sleep(3)
dr.quit()
