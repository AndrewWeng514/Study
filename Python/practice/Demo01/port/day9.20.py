# @Date   : 2022/9/20 15:32
# @Author : Andrew
# @Name   : day9.20
import requests

text = input('请输入搜索内容:')
agent = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}

res = requests.get(f"https://cn.bing.com/search?q= {text}", headers=agent)
with open('./baidu.html', 'w+', encoding='utf-8') as myfile:
    myfile.write(res.content.decode("utf-8"))
# res.encoding = 'utf-8'
# print("text:",res.text)
# print('headers:',res.headers)
# print("content:",res.content.decode("utf-8"))
# myfile = open('./baidu.html','w+',encoding='utf-8')
# myfile.write(res.content.decode("utf-8"))

# print(res.request.headers)
# print(res.request.url)
# print(res.request.method)
# print(res.request.body)
