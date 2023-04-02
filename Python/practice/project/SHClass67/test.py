from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()
dr.get('http://192.168.18.128:8080/test.html')
dr.switch_to.frame('iframe1')
dr.find_element('link text', '就业培训').click()
