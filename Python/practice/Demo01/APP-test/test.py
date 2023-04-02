"""
 @Author: Andrew
 @FileName: test.py
 @DateTime: 2022/10/12 17:01
"""
import os

# cmd ="adb shell monkey -p com.wondertek.paper -v -v -v 300 > monkey.log"
# os.system(cmd)

# 获取设备代号
# cmd = "adb devices"
# result_devices_list = os.popen(cmd).read().strip().split("\n")[1:]
# devices_list = []
# for i in result_devices_list:
#     devices_list.append(i.split("\t")[0])
# print(devices_list)

# 执行监控指令
# cmd ="adb shell dumpsys cpuinfo | findstr com.wondertek.paper"
# result_cpu = os.popen(cmd).read().strip().split(" ")[0]
# print(result_cpu)

# 执行monkey
# cmd = "adb shell monkey -p com.wondertek.paper -v -v -v 3000 > monkey.log"
# os.system(cmd)


a = ['--------20221013-104409-------', 'd_click,752,490,无', 'r_click,431,883,无', 'd_click,142,353,无',
     'd_click,1196,556,无']
b = '--------20221013-104409-------'
if b in a:
    c = a.index(b)
    print(c)
