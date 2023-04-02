"""
 @Author: Andrew
 @FileName: common.py
 @DateTime: 2022/10/19 14:43
 @Brief:脚本文件
"""
import pymysql
import requests
import os.path

import xlrd

ROOTPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(ROOTPATH)
TOOLPATH = os.path.join(ROOTPATH, 'tools\\')
# print(TOOLPATH)
# 公共工具地址
COMMONPATH = os.path.join(ROOTPATH, "common\\")
# 报告地址
REPOTRPATH = os.path.join(ROOTPATH, "report\\")
# 页面地址
PAGEPATH = os.path.join(ROOTPATH, 'page\\')
# 测试用例文件地址
DATAPATH = os.path.join(ROOTPATH, 'testdata\\')


class Common:
    sess = None

    def __init__(self):
        pass

    @classmethod
    def get_session(cls):
        if cls.sess is None:
            cls.sess = requests.session()
        return cls.sess

    @classmethod
    def operate_db(cls, mode, sql):
        import pymysql
        db_object = pymysql.Connect(host="101.34.13.184", user="root", password="123456", db='woniuboss4.0', port=3306,
                                    charset="utf8")
        sheet_object = db_object.cursor()
        if mode == 'r':
            sheet_object.execute(sql)
            read_result = sheet_object.fetchall()
            return read_result
        if mode == "w":
            try:
                sheet_object.execute(sql)
                db_object.commit()
            except:
                db_object.rollback()

    @classmethod
    def generate_report(cls, tablename):
        #  打开报告的文件
        with open(REPOTRPATH + "template-new.html", mode="r", encoding="utf-8") as file:
            content = file.read()
            # print(content)
        # 数据库中查询所有的测试结果
        sql = f"SELECT result,COUNT(result) FROM {tablename} group by result "
        result = cls.operate_db("r", sql)
        # print(result,len(result))
        #  统计所有的结果的个数
        pass_count = result[0][1]
        fail_count = result[1][1]
        # 生成失败个数的百分数
        fail_rate = fail_count / (pass_count + fail_count)
        fail_rate = f"{fail_rate:.2%}"
        # print(fail_rate)
        # 获取报告的名称 并对文件中的内容进行替换
        title_name = tablename + "-report"
        content = content.replace('$test-date', title_name)
        # print(content)
        #  统计用例成功的个数 失败的个数
        content = content.replace("$pass-count", str(pass_count))
        content = content.replace("$fail-count", str(fail_count))
        content = content.replace("$fail-rate", str(fail_rate))
        # 写入每条用例执行的情况
        sql = "SELECT * from login"
        result_case = cls.operate_db('r', sql)
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
        report_name = tablename + ".html"
        with open(report_name, mode="w", encoding="utf-8") as file:
            file.write(content)

    @classmethod
    def read_excel(cls, filename, sheetname):
        file_ad = DATAPATH + filename
        wb = xlrd.open_workbook(file_ad)
        sheet = wb.sheet_by_name(sheetname)
        testcases = []
        for i in range(1, sheet.nrows):
            cases = sheet.row_values(i)
            # print(cases)
            tem = cases[0:2]
            tem.append(eval(cases[2]))
            tem.append(eval(cases[3]))
            tem.append(cases[4])
            testcases.append(cases)
        # print(testcase)
        return testcases

    @classmethod
    def read_excel1(cls, filename, sheet):
        wb = xlrd.open_workbook(DATAPATH + filename)
        sheet = wb.sheet_by_name(sheet)
        nrows = sheet.nrows
        cases = []
        for info in range(1, nrows):
            row_value = sheet.row_values(info)
            tmp = row_value[0:2]
            tmp.append(eval(row_value[2]))
            tmp.append(eval(row_value[3]))
            tmp.append(row_value[4])
            cases.append(tmp)
        return cases

    @classmethod
    def wrapper(cls, *args, **kwargs):
        def get_time(fuc):
            def inner(self):
                for i in args:
                    fuc(self, *i, **kwargs)

            return inner

        return get_time
