# @Time    : 2022/9/17 11:29
# @Author  : Andrew
class FileOperation:
    @staticmethod
    def readFile(file):
        fp = open(file, 'r', encoding='utf-8')
        result = fp.readlines()
        fp.close()
        return result

    @staticmethod
    def writeFile(file, line):
        fp = open(file, 'a', encoding='utf-8')
        fp.write(line)
        fp.close()
