from Project_TeleCom.Comm.DBComm import DBOperation
from Project_TeleCom.Comm.FileComm import FileOperation


class TeleCom(DBOperation, FileOperation):  # 继承DBOperation,FileOperation
    def __init__(self, originFile, errorFile):
        print('This is a test')
        # 打开数据库
        # 获取待处理原始话单文件
        # 获取错误话单文件的路径和文件名

    def preDealFile(self):
        pass
        # 读取原始话单记录，使用正则进行数据检测，
        # 如果合法,插入CallInfo表，如果非法，写入error.txt文件

    def ComputeFee(self):
        pass
        # 读取CallInfo表数据，读取FeeStandard表数据，进行计费，
        # 计费结果写入CallFee表
        # 更新CallInfo的SeqNo和ModifyTime信息


if __name__ == '__main__':
    pass
