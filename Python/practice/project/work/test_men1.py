# @Time    : 2022/9/16 23:31
# @Author  : Andrew
import time

from selenium.webdriver import ActionChains

from project.work import memberManagement
from project.work.common.common_file import FileOperation
from project.work.config.config import test_result_adress, test_case_right_adress, test_case_wrong_adress


# 会员姓名：3-15个字符
# 手机号：13/15开头的11位数字
# 生日：必填，无其他要求
# 会员类型：必选

class TestMem:
    def __init__(self):
        self.test_mem = memberManagement.Member()
        self.action = ActionChains(self.test_mem.dr)

    def test_case(self, id, name, birth, phonenum, level, expect):
        self.test_mem.add_men(name, birth, phonenum, level)
        try:
            #    信息确认后会有添加成功弹框   查找到
            # self.test_mem.dr.find_element('xpath','//p[@class="el-message__content"]')
            self.test_mem.dr.find_element('xpath', f'//p[contains(text(),"{expect}")]')
            # self.test_mem.dr.find_element('xpath','//div[contains(text(),"长度在 3 到 15 个字符")]')
            print("测试成功")
            line = f"{id},{name},{birth},{phonenum},测试成功\n"
            FileOperation.writeFile(test_result_adress, line)
            self.test_mem.dr.refresh()
        except:
            print("测试失败")
            line = f"{id},{name},{birth},{phonenum},测试失败\n"
            FileOperation.writeFile(test_result_adress, line)
            self.test_mem.dr.refresh()


if __name__ == '__main__':
    test = TestMem()
    file = FileOperation()
    #    测试错误的测试用例   返回值全部为测试成功
    # caselist=file.readFile(test_case_wrong_adress)
    # for i in caselist:
    #     print(i,len(i),type(i))
    #     list = i.split(',')
    #     test.test_case(*list)

    # 测试正确的测试用例   返回值全部为测试成功
    caselist1 = file.readFile(test_case_right_adress)
    for i in caselist1:
        # print(i,len(i),type(i))
        list = i.split(',')
        test.test_case(*list)

    time.sleep(5)
    test.test_mem.dr.quit()
