"""
 @Author: Andrew
 @FileName: appium.py
 @DateTime: 2022/10/13 16:43
"""
import os
import threading
import time
from appium_test import Appium


class Cloud:
    # 获取当前设备id 返回列表
    # ['127.0.0.1:62001', '127.0.0.1:62025', '127.0.0.1:62026']
    def get_devices_id(self):
        cmd = 'adb devices'
        result = os.popen(cmd)
        results = result.read().strip().replace("\tdevice", '').split("\n")[1:]
        return results

    def phone_argument(self):
        argument_list = []
        p = 4723
        bp = 4724
        uid_list = self.get_devices_id()
        for i in uid_list:
            cmd = f"adb -s {i} shell getprop ro.build.version.release"
            platformVersion = os.popen(cmd).read().strip()
            tem = {}
            tem['platformVersion'] = platformVersion
            tem['udid'] = i
            tem["bport"] = p
            p += 1
            tem["bpport"] = bp
            bp += 1
            argument_list.append(tem)
        return argument_list

    def start_appium(self, bport, bpport, udid):
        cmd = rf'start appium -a 127.0.0.1 -p {bport} -bp {bpport} -U {udid} --no-reset --session-override --log-timestamp --log D:\{bport}.log'
        os.system(cmd)

    def start_test(self, bport, platformVersion, udid, bpport):
        self.start_appium(bport, bpport, udid)
        m = Appium(bport, platformVersion, udid)
        m.test()


# cmd = r'start appium -a 127.0.0.1 -p 4723 -bp 4724 -U 127.0.0.1:62001 --no-reset --session-override --log-timestamp --log D:\appium.log'
# os.system(cmd)
if __name__ == '__main__':
    c = Cloud()
    argument_list = c.phone_argument()
    thread_list = []
    for i in argument_list:
        udid = i['udid']
        bport = i['bport']
        bpport = i['bpport']
        platformVersion = i['platformVersion']
        th = threading.Thread(target=c.start_test, args=(bport, platformVersion, udid, bpport))
        thread_list.append(th)

    for i in thread_list:
        i.start()
    for i in thread_list:
        i.join()
    print("测试结束")
    os.system("chcp 65001")
    os.system("taskkill /F /IM cmd.exe")
    os.system("taskkill /F /IM node .exe")
