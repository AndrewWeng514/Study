
# @Time    : 2022/9/16 9:50
# @Author  : Andrew
import time
from selenium import webdriver
from selenium.webdriver.edge.webdriver import Service
from selenium.webdriver.chrome.webdriver import Service


class GetDriver:
    dr = None

    @classmethod
    def get_driver_edge(cls):
        if cls.dr is None:
            cls.s = Service(executable_path='../../../Demo01/UI/msedgedriver.exe')
            cls.dr = webdriver.Edge(service=cls.s)
            cls.dr.maximize_window()
            cls.dr.get("http://192.168.4.32:8080/woniusales")
        return cls.dr

    @classmethod
    def get_driver1_chrome(cls):
        if cls.dr is None:
            cls.s = Service(executable_path='../../../Demo01/UI/chromedriver.exe')
            cls.dr = webdriver.Chrome(service=cls.s)
            cls.dr.maximize_window()
            cls.dr.get("http://192.168.4.32:8080/woniusales")
            cls.dr.implicitly_wait(2)
        return cls.dr


if __name__ == '__main__':
    dr = GetDriver()
    dr.get_driver1_chrome()

    time.sleep(3)
    dr.get_driver1_chrome().quit()
