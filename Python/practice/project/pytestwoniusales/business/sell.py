# @Date   : 2022/9/23 16:27
# @Author : Andrew
# @Name   : sell
import requests
from project.pytestwoniusales.business.login import WoniusalesInterface


class Sell:

    def barcode(self, barcode):
        url_barcode = 'http://192.168.4.32:8080/woniusales/sell/barcode'
        res = WoniusalesInterface().login("admin", "123456", "0000")
        code = {
            "barcode": f"{barcode}"
        }
        res_barcode = requests.post(url_barcode, cookies=res.cookies, data=code)
        return res_barcode
