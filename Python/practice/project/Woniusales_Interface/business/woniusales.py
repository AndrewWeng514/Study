# @Date   : 2022/9/20 17:27
# @Author : Andrew
# @Name   : woniusales
'''
woniusales的接口测试

'''
import requests


class WoniusalesInterface:

    def login(self, username, password, verifcode):
        agent = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
        info = {
            "username": f"{username}",
            "password": f"{password}",
            "verifycode": f"{verifcode}"
        }
        URL = "http://192.168.6.4:8080/woniusales/user/login"
        res = requests.post(URL, data=info)
        with open('./woniu.thml', 'w+', encoding='utf-8') as myfile:
            myfile.write(res.content.decode("utf-8"))
        return res


if __name__ == '__main__':
    test = WoniusalesInterface()

    res = test.login("admin", 123456, "0000")
    print(res.headers)
    print(res.request.headers)
    print(res.request.body)
