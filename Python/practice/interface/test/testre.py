# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : testre.py
@desc: 
@Created on: 2022/9/20 14:55
"""
import time

"""
使用代码开展接口自动化 需要安装一个第三方库  pip install requests 
    requests库就是python专门用来模拟发送请求的库

requests库用法
    1.基本使用
        1.导入 import requests
        2.模拟发送请求并获取响应       res = requests.请求方式(url,相关参数)/ requests.request(请求方式,请求地址,相关参数)
    2.res响应对象的相关属性和方法
        res.text     获取响应正文 返回的是一个字符串格式
        res.content  获取响应正文 返回的是一个字节格式 res.content.decode(指定编码格式)
        res.json()   如果响应正文是json字符串 可以使用该方法 直接得到python数据类型 (使用它替代 json.loads(res.text ) )
        res.headers  获取响应头信息
        res.status_code  获取响应状态码
        res.encoding  获取响应对象的编码
        res.request.headers 获取请求头信息
        res.request.body 获取请求正文
        res.cookies    获取响应的cookie 它是一个cookiejar对象
    3.解决响应内容乱码的方式
        方案1: 设置res.encoding =指定编码 然后 res.text查看响应正文
        方案1: res.content.decode(指定编码格式) 查看响应正文
    
    4.自定义请求头
        1.构建一个字典 h={键:值,键2:值2} #键值就是请求头数据
        2.字典和请求产生关联  res = requests.请求方式(url,headers=h)
    
    5.发送带有查询字符串参数的请求
        查询字符串参数 (?后面接查询字符串参数 格式  键=值&键2=值2&。。。。)
        方式1:推荐使用
            参数直接写在url中 该怎么操作就怎么操作
        方式2:
            1.构建一个字典 p={键:值,键2:值2} #键值就是查询字符串参数
            2.字典和请求产生关联  res = requests.请求方式(url,params=p)
    
    6.发送post请求 参数类型为application/x-www-form-urlencoded
        方法1:推荐使用
            1.构建一个字典 d={键:值,键2:值2} #键值就是表单参数数据
            2.字典和请求产生关联  res = requests.请求方式(url,data=d)
            使用该方式会底层自己声明 请求头 'Content-Type': 'application/x-www-form-urlencoded'
        方法2:
            1.直接复制原始的表单数据正文   d=复制的内容
            2.声明请求正文的类型  h={'Content-Type': 'application/x-www-form-urlencoded'}
            3.参数和请求产生关联 res = requests.请求方式(url,data=d,headers=h)
    7.请求携带cookie的操作
        方法1:不推荐使用  复制的是死值 容易过期 后期变更需要重新复制
            1.构建头部字典 页面复制当前地址的cookie信息  h={"Cookie":复制的cookie信息}
            2.字典和请求产生关联  res = requests.请求方式(url,headers=h)
        
        方法2: 推荐使用
            1.先模拟成功登陆的接口 并得到响应对象  提取cookie res.cookies
            2.访问需要cookie的请求携带res.cookies 
                res = requests.请求方式(url,cookies=res.cookies )
        
        方法3: 推荐使用
            使用会话机制传递多个请求之间的信息
            1.实例化一个会话对象  sess = requests.session()
            2.使用会话对象成功登陆  res = sess.post("http://localhost:8080/WoniuSales-20180508-V1.4-bin/user/login",data=d)
            3.使用成功登陆的会话对象进行需要cookie的接口访问
                res = sess.get("http://localhost:8080/WoniuSales-20180508-V1.4-bin/sell")

    8.涉及文件上传的请求
        1.未涉及到文件的参数 构建一个字典 d={键:值,键2:值2} #键值就是未涉及到文件的参数数据
        2.涉及到文件的参数  构建一个字典 f={键:文件对象}--->f={  键:open(文件路径,"rb"),   键2:open(文件路径2,"rb")   }
        3.参数和请求产生关联  res=requests.请求方式(url,data=d,files=f) #分开描述 分开关联
    
    9.发送json格式数据的请求
        方案1:
            1.复制请求正文的原始json数据    d=复制的数据
            2.在请求头声明请求正文类型   h={"Content-Type":"application/json"} 
            3.请求和参数产生关联  res = requests.请求方式(url,data=d,headers=h)
        方案2:
            1.将请求的json数据变成python数据类型(建议使用火狐可以直接复制)   j=json数据转化后的python数据
            2.请求和参数产生关联  res=requests.请求方式(url,json=j) #底层会自动声明头部中 "Content-Type":"application/json"
            
接口测试的流程
    1.模拟构建请求数据包(url,请求方式,请求头,请求正文) 
    2.通过工具或者代码 模拟发送请求并获取响应
    3.校验响应数据是否和期望一致  
        1.常数校验（直接拿期望值和具体的值进行比较 不严谨  但是使用最频繁 ）
        2.结合数据库进行数据校验 保证接口的逻辑正常 
        
接口测试其他
    常见加密算法类型
        1.对称加密   加密和解密使用同一个密钥  des
            优点:速度相对较快
            缺点:只要有一方泄漏就没有安全可言
        2.非对称加密  有两个密钥 公钥加密私钥解密 私钥加密 公钥解密   rsa
            优点:更加安全  私钥保留给自己 公钥随便发 只要私钥不泄露就不会泄漏
            缺点:需要更多的cpu算了 浪费时间
            
        3.hash散列加密   md5
            单向加密 只能加密不能解密  固定输入固定输出  唯一输入唯一输出（不同的内容会产生不同的加密数据 理论上不存在 不同的数据 同样的加密结果）

    如何定位bug属于前端bug还是后端bug
        如果是页面显示类的错误 页面效果动态行为 属于前端bug
        如果是页面数据类的错误  通过抓包找到接口
            看请求参数是否正确  如果参数不正确 属于前端bug
            如果参数正确 看响应结果  看是否与预期一致  如果不一致 后端bug
            如果参数 响应结果都正确 但是页面显示错误 前端bug
            
        
"""
"""
补充:
    编码和解码
        计算机底层只能识别二进制   0/1  二进制又称比特位  1个二进制表示 1bit
        我们会用8个二进制(8bit) 表示一个数据  00000000-11111111
        那么8bit我们一般又称为  一个字节  1bytes 字节是计算机存储的最小单位
        1K=1024bytes  1M=1024K
        
        字符 每个字就可以称之为字符 a  C   中   , 
        字符集  字符集记录字符对应的二进制关系
        ascii码表就是一种记录128个字符的字符集  
        
        随着互联网的发展 ascii不能支持足够多的字符
        中国有一套自己的字符集 gbk （记录中文字符对应的二进制关系）  两个字节表示一个中文字
        utf-8 万国码 不定长字符集 我们中文在这个字符集占用三个字节
        
        字符串.encode(指定字符集)  字符---->字节  这个叫编码  
        字节.decode(指定字符集)  字节---->字符串  这个叫解码
    
    python中专门生成随机数据的模块 faker   pip install faker
        1.导入  from faker import Faker
        2.实例化对象 交代语言 f = Faker("zh_cn") #默认英文
        3.生成相关随机数据  
            f.name()
            f.phone_number()
            f.ssn()
            f.address()
            f.simple_profile()
            f.profile()
          
"""

import requests


def output(res, filename="a.html"):
    # 提取响应对象的头部中的Content-Type  判断是否为html
    if 'text/html' in res.headers.get("Content-Type") if res.headers.get("Content-Type") else []:  # 条件成立 说明是html
        with open(filename, "wb") as f:
            f.write(res.content)
        print(f"内容是html格式 保存到 {filename}中")

    else:
        print("查看响应正文", res.text)
    print("查看响应头", res.headers)
    print("查看响应状态码", res.status_code)
    print("查看请求头", res.request.headers)
    print("查看请求正文", res.request.body)
    print("查看请求url", res.request.url)


import requests

url = "http://localhost:8080/WoniuSales-20180508-V1.4-bin/goods/deletebatch"

payload = 'batchname=GB20220927'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=D39E8A57FFC53A63C377FE92348BDF73; password=123456; username=admin'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

import requests
import json

url = "https://demo.halo.run/api/admin/login"

payload = json.dumps({
    "username": "demo",
    "password": "P@ssw0rd123..",
    "authcode": None
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# output(loginres)
#
#
# res = requests.get("http://localhost:8080/WoniuSales-20180508-V1.4-bin/sell",cookies=loginres.cookies)
# output(res)

# # 1.实例化一个会话对象
# sess = requests.session()
#
# d={"username":"admin","password": "123456","verifycode": "00"}
# #2.使用会话对象进行成功登陆 成功登陆后 会话对象就会存储cookie相关数据
# # sess.headers["abcde"]="asss"
# sess.headers["aaaa"]="asassaf"
#
#
#
# res = sess.post("http://localhost:8080/WoniuSales-20180508-V1.4-bin/user/login",data=d)
# print("登陆接口的请求头:", res.request.headers)
# print("登陆接口的响应头:", res.headers)
#
# #3.使用会话对象访问需要携带cookie的请求
# res = sess.get("http://localhost:8080/WoniuSales-20180508-V1.4-bin/sell")
# print("首页接口的请求头:", res.request.headers)
# print("首页接口的响应头:", res.headers)
# output(res)
# 登陆流程接口
# d={"username":"admin","password": "123456","verifycode": ""}
# d="username=admin&password=123456&verifycode="
# h={'Content-Type': 'application/x-www-form-urlencoded'}
# res = requests.post("http://localhost:8080/WoniuSales-20180508-V1.4-bin/user/login",data=d,headers=h)
# output(res)


# name = input("请输入要搜索的明星")
# h={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
# p={"q":name}
# res = requests.get(f"https://cn.bing.com/search",headers=h,params=p)
# cont = res.content
# with open("a.html","wb") as f:
#     f.write(cont)
#
# print("headers:",res.request.headers)
# print("url:",res.request.url)

# print("method:",res.request.method)
# print("body:",res.request.body)
# print(res.headers)
# print(res.status_code)

# res.encoding="utf-8"
# print(res.encoding)
# print(res.text,type(res.text))
# # print(res.content.decode("utf-8"))
# print(res.content,type(res.content))
