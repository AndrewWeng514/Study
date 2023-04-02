# @Time    : 2022/9/16 22:42
# @Author  : Andrew
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from project.work.config.config import auto_address, web_address


class GetDriver:
    dr = None

    @classmethod
    def get_driver_chrom(cls):
        if cls.dr is None:
            cls.s = Service(executable_path=auto_address)
            cls.dr = webdriver.Chrome(service=cls.s)
            cls.dr.maximize_window()
            cls.dr.get(web_address)
            cls.dr.implicitly_wait(3)
        return cls.dr


if __name__ == '__main__':
    dr = GetDriver().get_driver_chrom()

    time.sleep(2)
    dr.quit()
