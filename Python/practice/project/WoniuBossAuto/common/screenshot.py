"""
 @Author: Andrew
 @FileName: screenshot.py
 @DateTime: 2022/10/19 11:01
 @Brief:截图  输入文件名  保存到指定位置
"""
import pyautogui
from project.WoniuBossAuto.config.get_path import REPOTRPATH


def screenshot(picturename):
    picture_ad = REPOTRPATH + picturename + '.png'
    # print(picture_ad)
    pyautogui.screenshot(picture_ad)

# screenshot("sdasd")
