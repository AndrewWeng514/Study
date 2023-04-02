"""
多窗口切换

handle:句柄。浏览器窗口的一个唯一标识
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='chromedriver.exe')
dr = webdriver.Chrome(service=s)
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('https://www.woniuxy.com')
# print(dr.window_handles)
dr.find_element('link text', '就业培训').click()
# dr.switch_to.window()
# print(dr.window_handles)
print(dr.current_url)
windows = dr.window_handles  # 获取所有窗口的句柄
dr.switch_to.window(windows[1])  # 切换到指定的窗口
print(dr.current_url)
dr.find_element('xpath', '//span[@onclick="hide_floatWindow();"]').click()

dr.find_element('xpath', '//a[@href="https://www.aduobi.com/ui.html"]').click()
