"""
对浏览器的操作
"""
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
# time.sleep(2)
dr.get('http://192.168.18.128:8080/woniusales')
# time.sleep(2)
# dr.back()  # 操作浏览器的后退按钮
# time.sleep(2)
# dr.forward() # 操作浏览器的前进按钮
# time.sleep(2)
# dr.refresh()  # 刷新页面
# time.sleep(5)
# dr.close() # 关闭浏览器
# dr.quit() # 关闭浏览器，并且结束driver进程
print(dr.current_url)  # 获取浏览器地址栏当前的url地址
print(dr.page_source)  # 获取页面的html源码
print(dr.get_window_size())  # 获取窗口尺寸
