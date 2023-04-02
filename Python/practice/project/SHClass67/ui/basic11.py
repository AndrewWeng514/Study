"""
页面嵌套的处理
iframe标签：页面嵌套页面

"""
from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(10)
dr.get('http://192.168.18.128:8080/index_1.html')
dr.find_elements('tag name', 'input')[0].send_keys('yonghuming')
# dr.switch_to.frame(0) # 切换进内嵌页面，使用索引值来切换，索引从0开始
# dr.switch_to.frame('iframe12') # 使用iframe的id或者name属性的值来切换
ele = dr.find_element('xpath', '//iframe[@src="https://www.woniuxy.com"]')
dr.switch_to.frame(ele)  # 使用iframe元素来切换
dr.find_element('link text', '首页').click()
# dr.switch_to.parent_frame() # 切换到父级页面
dr.switch_to.default_content()  # 切换到默认的页面
dr.find_elements('tag name', 'input')[1].send_keys('mima')
