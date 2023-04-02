"""
图像识别

"""
import time

import pyautogui

# pyautogui.click(315,347) # 在给点坐标处单击
#
# pyautogui.typewrite('abcdef',interval=0.5) # 输入一个字符串，间隔0.5s
#
time.sleep(3)
pyautogui.screenshot('base.png')  # 截图。截取当前屏幕，跟浏览器无关
# time.sleep(4)
# x,y = pyautogui.locateCenterOnScreen('./ok.png') # 返回给定图片在屏幕上的中心点位置
# print(x,y)
# pyautogui.click(x,y)
