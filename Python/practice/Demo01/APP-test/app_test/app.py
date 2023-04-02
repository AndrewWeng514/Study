"""
 @Author: Andrew
 @FileName: app.py
 @DateTime: 2022/10/14 9:36
"""
import os
import re
import sys

import requests


class Testing:
    def __init__(self, apk):
        add = rf"{sys.path[0]}\app\{apk}"
        cmd1 = f"aapt dump badging {add}|findstr package"
        package_name = os.popen(cmd1).read().strip()
        # print(package_name, type(package_name))
        self.package_name = re.search("name='(.*?)'", package_name).group(1)
        # print(package_name, type(package_name))

        cmd2 = f"aapt dump badging {add}|findstr launchable-activity"
        launch_name = os.popen(cmd2).read().strip()
        # print(launch_name, type(launch_name))
        self.launch_name = re.search("name='(.*?)'", launch_name).group(1)
        # print(launch_name, type(launch_name))

    def install(self, apk):
        add = rf"{sys.path[0]}\app\{apk}"
        cmd = f"adb install {add}"
        try:
            result_instll = os.popen(cmd).read()
            # print(result_instll)
            if "Success" in result_instll:
                print("安装成功")
            else:
                print("安装失败")
        except:
            print("安装失败")
        # cmd1 = "adb shell pm list package -3"
        # package_list = os.popen(cmd1).read()
        # print(package_list)
        print(add)

    def start_app(self, apk):
        cmd = f"adb shell am start {self.package_name}/{self.launch_name}"
        os.popen(cmd)
        cmd1 = f"adb shell ps "
        runings = os.popen(cmd1).read().strip()
        # print(runings,type(runings))
        # 启动断言
        if self.package_name in runings:
            print(f"{apk}启动成功")
        else:
            print(f"{apk}启动失败")

    def monkey(self, apk):
        cmd = rf"adb shell monkey -p {self.package_name} -v -v -v 3000 > .\result\{apk}.log"
        monkey_result = os.popen(cmd).read()
        if "crash" in monkey_result or "error" in monkey_result:
            print(f"{apk}monkey测试有错误")
        else:
            print(f"{apk}monkey测试通过")

    def uninstall(self, apk):
        cmd = f"adb uninstall {self.package_name}"
        os.popen(cmd)
        cmd1 = "adb shell pm list package -3"
        packages = os.popen(cmd1).read().strip()
        if self.package_name in packages:
            print(f"{apk}删除失败")
        else:
            print(f"{apk}删除成功")

    def download_app(self):
        url = "https://www.wandoujia.com/top/app"
        result = requests.get(url).text
        print(result)
        # apk_url = re.findall( <a class="cate-link" href="https://www.wandoujia.com/category/5029">,result.text)
        # print(apk_url)


if __name__ == '__main__':
    apks = os.listdir("./app")
    # print(apks)
    c = Testing("TapTap_2.36.0-rel.200200_seo.apk")
    c.download_app()
    for apk in apks:
        pass
        # t = Testing(apk)
        # t.install(apk)
        # t.start_app(apk)
        #
        # t.monkey(apk)
        # t.uninstall(apk)
