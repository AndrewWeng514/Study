"""
 @Author: Andrew
 @FileName: report.py
 @DateTime: 2022/10/18 17:12
 @Brief:生成login的测试报告
"""
from Demo01.framework.basic.database import Common
from Demo01.framework.config.config import resultdb


class Reporter:
    result_ad = "../report/login.html"

    def __init__(self):
        self.db_object, self.sheet_object = Common.openDB(*resultdb)

    def generate_report(self):
        #  打开报告的文件
        with open(self.result_ad, mode="r", encoding="utf-8") as file:
            content = file.read()
            # print(content)
        # 数据库中查询所有的测试结果
        sql = "SELECT result,COUNT(result) FROM login group by result"
        result = Common.readDB(self.sheet_object, sql)
        # print(result,len(result))
        #  统计所有的结果的个数
        pass_count = result[0][1]
        fail_count = result[1][1]
        # 生成失败个数的百分数
        fail_rate = fail_count / (pass_count + fail_count)
        fail_rate = f"{fail_rate:.2%}"
        # print(fail_rate)
        # 获取报告的名称 并对文件中的内容进行替换
        title_name = self.result_ad.split("/")[-1].split(".")[0] + "-report"
        content = content.replace('$test-date', title_name)
        # print(content)
        #  统计用例成功的个数 失败的个数
        content = content.replace("$pass-count", str(pass_count))
        content = content.replace("$fail-count", str(fail_count))
        content = content.replace("$fail-rate", str(fail_rate))
        # 写入每条用例执行的情况
        sql = "SELECT * from login"
        result_case = Common.readDB(self.sheet_object, sql)
        print(result_case)
        tem = ''
        for i in result_case:
            test_id = i[1]
            name = i[2]
            result = i[3]
            picture = i[4]
            exp = i[5]
            fact = i[6]
            tem += '<tr bgcolor="white">'
            tem += f'\n<td width="5%">{test_id}</td>'
            tem += f'\n<td width="15%">{name}</td>'
            tem += f'\n<td width="15%">{result}</td>'
            tem += f'\n<td width="15%">{exp}</td>'
            tem += f'\n<td width="5%">{fact}</td>'
            # 判断如果用例执行结果为成功 则在图片出写无,否则写入图片
            if result == "success":
                tem += f'\n<td width="8%">无</td>'
            else:
                tem += f'\n<td width="8%"><a href="./{picture}" target="_blank">{picture}</a></td>'
            tem += '\n</tr>'
            print(tem)
        content = content.replace('$test-result', tem)

        # 写入html文件
        with open(self.result_ad, mode="w", encoding="utf-8") as file:
            file.write(content)


if __name__ == '__main__':
    r = Reporter()
    r.generate_report()
