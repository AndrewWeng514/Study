import os
import re
import threading
import time
from math import ceil
import requests

time_list = []


class Performance:
    def __init__(self):
        pass

    def performance(self):
        start_time = time.time()

        url = "https://www.woniuxy.com"
        res = requests.get(url, verify=False)  # 获取网页数据
        # print(res.text)
        pngs = re.findall('src="(.+?).png"', res.text)  # 查找所有响应正文中所有图片路径
        print(pngs)
        png_list = [url + png + ".png" for png in pngs if not png.startswith("http")]  # 拼接图片获取网页获取路径 并进行判断
        # print(png_list)
        # 去重
        # png_list_distinct = []
        # for i in png_list:
        #     if i not in png_list_distinct:
        #         png_list_distinct.append(i)

        for url in set(png_list):  # set  集合不重复
            dir_name = threading.current_thread().name  # 获取当前线程的名字
            if dir_name not in os.listdir():  # 判断文件名称是否存在
                os.mkdir(dir_name)  # 如果文件名称不存在  则新建一个文件夹
            filename = url.split("/")[-1]  # 获取每个图片的文件名
            if filename not in os.listdir(f"./{dir_name}"):
                res = requests.get(url)
            with open(f"./{dir_name}/{filename}", "wb") as file:  # 写入读取的图片
                file.write(res.content)

        end_time = time.time()
        time_list.append(end_time - start_time)


if __name__ == "__main__":
    threading_list = []
    for i in range(6):  # 创建线程组
        T = Performance()
        th = threading.Thread(target=T.performance, args=())
        threading_list.append(th)
    for i in threading_list:  # 同时运行线程组
        i.start()

    for i in threading_list:  # 阻塞主线程,使主线程等待子线程运行完毕后
        i.join()
    print(time_list)
    print(f"共有用户{len(time_list)}访问,最长等待时间{max(time_list)},平均时间{sum(time_list) / len(time_list)}")
    time_list.sort()
    time95 = ceil(len(time_list) * 0.95)
    time_list1 = time_list[time95 - 1]
    print(f"共有用户{len(time_list)},95%用户最长时间不超过{time_list1}")
