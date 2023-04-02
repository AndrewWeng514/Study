"""
 @Author: Andrew
 @FileName: main.py
 @DateTime: 2022/10/17 11:12
"""
import time

from Demo01.framework.practice.test_login import TestLogin
from Demo01.framework.asset.test_assets import TestAssets

if __name__ == '__main__':
    l = TestLogin()
    l.login_test()
    a = TestAssets()
    a.test_asset()

    time.sleep(2)
    a.dr.quit()
