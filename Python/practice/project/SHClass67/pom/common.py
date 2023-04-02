from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""
单例：整个运行过程中，公用同一个对象，对于ui自动化来说，就是整个测试过程中都公用同一个浏览器
类变量和实例变量的区别：
类变量：不会随类的实例化而改变，通过类方法类改变
实例变量：随着类的实例化而改变

"""


class GetDriver:
    dr = None

    @classmethod
    def get_driver(cls):
        """
        打开浏览器
        """
        if cls.dr is None:
            cls.s = Service(executable_path='../ui/chromedriver.exe')
            cls.dr = webdriver.Chrome(service=cls.s)
            cls.dr.maximize_window()
        cls.dr.implicitly_wait(10)
        return cls.dr

    def get_element(self, what, value):
        try:
            wait = WebDriverWait(self.dr, 10, 0.5)
            ele = wait.until(ec.presence_of_element_located((what, value)))
            return ele
        except:
            print(f"{what}={value}定位方法没有找到元素")
        # self.dr.find_element(what,value)
