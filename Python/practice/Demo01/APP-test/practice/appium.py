"""
 @Author: Andrew
 @FileName: appium.py
 @DateTime: 2022/10/13 20:06
"""
import os


class Appium:

    def __init__(self):
        pass

    #  使用无界面Appium  连接指定设备  并且输出日志到指定位置
    def start_appium(self):
        cmd = r"start appium -a 127.0.0.1 -p 4723 -bp 4724 -U 127.0.0.1:62001 " \
              r"--no-reset --session-override --log-timestamp --log D:\appium.log"
        os.system(cmd)

    # 获取当前运行设备信息
    def get_devices_info(self):
        # 获取当前运行设备的UID
        cmd = "adb devices"
        result_uids = os.popen(cmd).read().strip().replace("\tdevice", "").split("\n")[1:]
        print(result_uids)


if __name__ == '__main__':
    m = Appium()
    m.get_devices_info()
