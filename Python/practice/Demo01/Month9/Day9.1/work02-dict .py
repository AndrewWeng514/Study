# @Time    : 2022/9/1 18:24
# @Author  : Andrew
import json

#   方法一  eval 转 dict
"""
words=input('请输入一个字典:')
dic1 =eval(words)
if str(type(dic1))[8:-2] == "dict":
    print(f'{words}是一个字典')
else:
    print(f'{words}不是一个字典')
"""

#  异常抛出
words = input('请输入一个字典:')
try:
    if words[0] != '{' and words[-1] != '}':
        raise Exception(f'{words}不是一个字典')
    else:
        words1 = words.replace('{', '')
        words1 = words.replace('}', '')
        if ',' not in words:
            raise Exception(f'{words}不是一个字典')
        else:
            words1 = words1.split(',')
            # print(words[0],type(words[0]))
            for i in words1:
                # print(words[i],type(words[i]))
                if ':' not in i:
                    raise Exception(f'{words}不是一个字典')
                else:
                    list = i.split(':')
                    # print(list,type(list))
                    element = list[0]

                    if str(type(list[0]))[8:-2] not in ('int', 'str', 'tuple'):
                        raise Exception(f'{words}不是一个字典')
        # print(f'{words}是一个字典')

except Exception as e:
    print(e)
else:
    print(f'{words}是一个字典')
