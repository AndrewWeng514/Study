"""
基础操作
手工测试操作步骤：
1、打开浏览器
2、访问woniusals首页
3、用户名输入框中输入admin
4、密码框输入123456
5、验证码框中输入0000
6、点击登录


url地址的格式：
http://ip:port/file
http://192.168.18.128:8080/woniusales
https://www.woniuxy.com/
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 实例化chromedriver服务
s = Service(executable_path='chromedriver.exe')
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

# if dr.find_element('link text','注销1'):
#     print("测试通过")
# else:
#     print("测试失败")
try:
    dr.find_element('link text', '注销')
    print("测试通过")
except:
    print("测试失败")
