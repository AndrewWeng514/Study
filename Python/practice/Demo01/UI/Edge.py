# @Time    : 2022/9/13 17:34
# @Author  : Andrew
from selenium import webdriver
from selenium.webdriver.edge.webdriver import Service

s = Service(executable_path='./msedgedriver.exe')
dr = webdriver.Edge(service=s)  # 实例化浏览器  相同目录下自动引用
dr.maximize_window()  # 最大化浏览器
dr.get("http://192.168.4.32:8080/woniusales/")  # 打开蜗牛进销存
dr.find_element("id", "username").send_keys("admin")  # 寻找用户名框并输入
dr.find_element("id", "password").send_keys("123456")  # 寻找密码框并输入
dr.find_element("id", "verifycode").send_keys("0000")  # 寻找验证码框并输入
dr.find_element('class name', "form-control.btn-primary").click()  # 寻找登录按钮并点击
