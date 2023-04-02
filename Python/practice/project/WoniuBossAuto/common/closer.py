"""
 @Author: Andrew
 @FileName: closer.py
 @DateTime: 2022/10/19 10:53
 @Brief:闭合函数  装饰器
"""


def wrapper(*args, **kwargs):
    def get_time(fuc):
        def inner(self):
            for i in args:
                fuc(self, *i, **kwargs)

        return inner

    return get_time


#  测试
from Demo01.framework.basic.xls import read_xls_up

data = read_xls_up("../testdata/assets-test-case.xls", 'Sheet1')


@wrapper(*data)
def test(case_id, case_name, asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
         asset_owner, by, values, exp):
    print(case_id, case_name, asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
          asset_owner, by, values, exp)
