# @Date   : 2022/9/20 17:53
# @Author : Andrew
# @Name   : 12212
# 方法二：使用params参数为格式为字典，当有多个数据时会自动拼接
import requests

url = 'https://www.baidu.com/s?'
# 定义自定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
# 发送自定义请求头
par = {"wd": "蜗牛", "pn": 30}
response = requests.get(url, headers=headers, params=par)
with open('./woniu1.thml', 'w+', encoding='utf-8') as myfile:
    myfile.write(response.content.decode("utf-8"))
