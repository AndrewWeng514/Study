"""
键盘和鼠标的操作
"""
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

s = Service(executable_path='chromedriver.exe')
dr = webdriver.Chrome(service=s)
dr.maximize_window()
dr.get('http://192.168.18.128:8080/woniusales')
# dr.find_element().send_keys()

action = ActionChains(dr)
ele = dr.find_element('id', 'username')
action.click(ele)  # 调用鼠标操作方法在某个元素上点击
action.send_keys('admin')  # 调用键盘方法输入
# action.perform() # 执行键盘和鼠标的操作
#
# pwd = dr.find_element('id','password')
# action.click(pwd)
# action.send_keys('123456')
# action.perform()
# ele = dr.find_element('link text','商品入库')
# action.move_to_element(ele) # 调用鼠标的移动方法
# # action.click(ele) # 调用鼠标的单击方法
# # action.context_click(ele) # 调用鼠标的右键单击方法
# action.move_by_offset(-100,0) # 偏移。在某个位置的基础上移动多少
# time.sleep(2)

# action.send_keys('aaa') # 调用键盘的输入
# action.send_keys(Keys.CONTROL,'a')
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
# action.send_keys_to_element(ele,'admin') # 在某个元素上输入
action.perform()  # 执行动作
