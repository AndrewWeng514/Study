# -*- coding: utf-8 -*-
# @Time : 2022/9/27 23:42
# @Author : Andrew
# @File : work.py
# @Project : practice
import os
import re
import threading

import requests


class Woniu:
    def __int__(self):
        pass

    def performance(self):
        url = "https://woniuxy.com"
        res = requests.get(url)
        # print(res.text)
        js_names = re.findall('src="(.+?).js"', res.text)
        print(js_names)
        js_list = [url + js_name + ".js" for js_name in js_names]  # 拼接js下载地址
        print(js_list)
        for url in set(js_list):  #
            dir_name = threading.current_thread().name
            if dir_name not in os.listdir():
                os.mkdir(dir_name)
            filename = url.split("/")[-1]
            if filename not in os.listdir(f"./{dir_name}"):
                res = requests.get(url)
            with open(f"{dir_name}/{filename}", "wb") as file:
                file.write(res.content)


if __name__ == '__main__':
    T = Woniu()
    T.performance()
