class FileOperation:
    @staticmethod
    def readFile(file):
        fp = open(file, 'r', encoding='utf-8')
        result = fp.readlines()
        fp.close()
        return result

    @staticmethod
    def writeFile(file, mode, strList):
        fp = open(file, mode, encoding='utf-8')
        for line in strList:
            fp.write(line)
        fp.close()
