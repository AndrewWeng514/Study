"""
 @Author: Andrew
 @FileName: get_path.py
 @DateTime: 2022/10/19 10:33
 @Brief:获取路径
"""
import os.path

ROOTPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(ROOTPATH)
TOOLPATH = os.path.join(ROOTPATH, 'tools\\')
# print(TOOLPATH)
# 公共工具地址
COMMONPATH = os.path.join(ROOTPATH, "common\\")
# 报告地址
REPOTRPATH = os.path.join(ROOTPATH, "report\\")
# 页面地址
PAGEPATH = os.path.join(ROOTPATH, 'page\\')
# 测试用例文件地址
DATAPATH = os.path.join(ROOTPATH, 'testdata\\')
