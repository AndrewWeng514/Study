"""
截图操作
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

# 截图，并保存文件
# dr.save_screenshot('./test.png')

# 截图，保存文件
# dr.get_screenshot_as_file('./test1.png')

# 截图，返回图片的b64二进制编码
# png = dr.get_screenshot_as_png()
# print(png)

# with open('./test2.png',mode='wb') as file:
#     file.write(png)

# 截图，返回图片base64编码
png = dr.get_screenshot_as_base64()
print(png)
