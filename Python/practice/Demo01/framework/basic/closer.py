"""
 @Author: Andrew
 @FileName: closer.py
 @DateTime: 2022/10/18 23:01
 @Brief:
"""
import time


def wrapper(*args, **kwargs):
    def get_time(fuc):
        def inner(self):
            start = time.time()
            for i in args:
                fuc(self, *i, **kwargs)
            end = time.time()
            # print(end-start)

        return inner

    return get_time


from Demo01.framework.basic.xls import read_xls_up

data = read_xls_up("../testdata/assets-test-case.xls", 'Sheet1')


@wrapper(*data)
def test(case_id, case_name, asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
         asset_owner, by, values, exp):
    print(case_id, case_name, asset_name, asset_type, asset_code, asset_price, asset_purchase_employee, asset_note,
          asset_owner, by, values, exp)
