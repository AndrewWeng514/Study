# @Time    : 2022/9/16 23:31
# @Author  : Andrew
from selenium.webdriver import ActionChains

from project.work import memberManagement
from project.work.common.common_file import FileOperation
from project.work.config.config import test_result_right_adress, test_result_wrong_adress, test_case_right_adress, \
    test_case_wrong_adress


# 会员姓名：3-15个字符
# 手机号：13/15开头的11位数字
# 生日：必填，无其他要求
# 会员类型：必选

class TestMem:
    def __init__(self):
        self.test_mem = memberManagement.Member()
        self.action = ActionChains(self.test_mem.dr)

    def test_case_right(self, id, name, birth, phonenum, level, ):
        self.test_mem.add_men(name, birth, phonenum, level)
        try:
            self.test_mem.dr.find_element('xpath', '//div[contains(text(),"长度在 3 到 15 个字符")]')
            self.test_mem.dr.find_element('xpath', '//div[contains(text(),"请选择生日")]')
            self.test_mem.dr.find_element('xpath', '//div[contains(text(),"联系电话不能为空")]')
            print("测试失败")
            line = f"{id},{name},{birth},{phonenum},测试失败"
            FileOperation.writeFile(test_result_right_adress, line)
            self.cancel = \
                self.test_mem.dr.find_elements("xpath", '//i[@class="el-dialog__close el-icon el-icon-close"]')[0]
            self.action.click(self.cancel)
            self.action.perform()
        except:
            print("测试成功")
            line = f"{id},{name},{birth},{phonenum},测试成功"
            FileOperation.writeFile(test_result_right_adress, line)
            self.cancel = \
                self.test_mem.dr.find_elements("xpath", '//i[@class="el-dialog__close el-icon el-icon-close"]')[0]
            self.action.click(self.cancel)
            self.action.perform()

    def test_case_wrong(self, id, name, birth, phonenum, level, ):
        self.test_mem.add_men(name, birth, phonenum, level)
        try:
            self.test_mem.dr.find_element('xpath', '//div[contains(text(),"长度在 3 到 15 个字符")]')
            self.test_mem.dr.find_element('xpath', '//div[contains(text(),"请选择生日")]')
            self.test_mem.dr.find_element('xpath', '//div[contains(text(),"联系电话不能为空")]')
            print("测试成功")
            line = f"{id},{name},{birth},{phonenum},测试成功"
            FileOperation.writeFile(test_result_wrong_adress, line)
            self.cancel = \
            self.test_mem.dr.find_elements("xpath", '//i[@class="el-dialog__close el-icon el-icon-close"]')[0]
            self.action.click(self.cancel)
            self.action.perform()
        except:
            print("测试失败")
            line = f"{id},{name},{birth},{phonenum},测试失败"
            FileOperation.writeFile(test_result_wrong_adress, line)
            self.cancel = \
            self.test_mem.dr.find_elements("xpath", '//i[@class="el-dialog__close el-icon el-icon-close"]')[0]
            self.action.click(self.cancel)
            self.action.perform()


if __name__ == '__main__':
    test = TestMem()
    file = FileOperation()
    test.test_case_wrong(1, "张三aaa", 2020 - 1 - 12, 13111111111, "周卡")
    # caselist=file.readFile(test_case_wrong_adress)
    # for i in caselist:
    #     print(i,len(i),type(i))
    #     list = i.split(',')
    #     test.test_case_wrong(*list)
    # caselist1 = file.readFile(test_case_right_adress)
    # for i in caselist1:
    #     list = i.split(',')
    #     test.test_case_wrong(*list)
