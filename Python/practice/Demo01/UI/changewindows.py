# @Time    : 2022/9/15 17:19
# @Author  : Andrew
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WaitExcTypes

s = Service(executable_path='./chromedriver.exe')
dr = webdriver.Chrome(service=s)
dr.maximize_window()
dr.get("http://192.168.4.32:8080/index_1.html")
print(dr.current_url)
dr.find_elements('tag name', 'input')[0].send_keys('1111')
dr.find_elements('tag name', 'input')[1].send_keys('2312')
dr.find_element('link text', "首页").click()

time.sleep(5)
dr.quit()
