# @Time    : 2022/9/1 16:43
# @Author  : Andrew
import json

# 1.
# json.dumps
# 将
# Python
# 对象编码成
# JSON
# 字符串
# 2.
# json.loads
# 将已编码的
# JSON
# 字符串解码为
# Python
# 对象

# !/usr/bin/python
import json

stu = [{'ID': 1001, 'Name': 'Kate', 'Sex': 'Female', 'Height': 187}]
print(type(stu))
stuJson = json.dumps(stu)  # 将python对象编码成Json字符串
print(stuJson)
print(type(stuJson))
text = json.loads(stuJson)  # 将Json字符串解码成Python对象
print(text[0]["Name"])

# 补充：
import json

# 1. Json标准字符串，可以转变成Python对应的数据类型
content = '{"status":0,"message":"Success"}'
content = json.loads(content)
print(content)
print(type(content))

# 2. 非Json标准字符串，不能通过loads转变成python数据类型
content = "{'status':0,'message':'Success'}"
content = json.loads(content)
print(content)
print(type(content))

# 3. 非Json标准字符串，通过eval可以转变成python数据类型
content = "{'status':0,'message':'Success'}"
content = eval(content)
print(content)
print(type(content))

# 4. Json标准字符串，可以转变成Python对应的数据类型
content = '{"status":0,"message":"Success"}'
content = eval(content)
print(content)
print(type(content))

# 5. Json标准字符串，可以通过eval转换成python对应数据类型
content = '["status","message"]'
content = eval(content)
print(content)
print(type(content))

# 6. Python字典，转化成json字符串
content = {'status': 0, 'message': 'Success'}
content = json.dumps(content)
print(content)
print(type(content))

# 7. Python列表,可以转化成json字符串
content = ['status', 'message']
content = json.dumps(content)
print(content)
print(type(content))

# 8. Python元组，可以转换成json字符串，但转换后是[]
content = ('status', 'message')
content = json.dumps(content)
print(content)
print(type(content))

# 9. Python集合，不支持转化成Json字符串
content = {'status', 'message'}
content = json.dumps(content)
print(content)
print(type(content))
