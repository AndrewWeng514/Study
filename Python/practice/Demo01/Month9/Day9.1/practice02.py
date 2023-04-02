#     EXcel定义函数
def computer(data1, oper, data2):
    if oper == "+":
        result = data1 + data2
    elif oper == "-":
        result = data1 - data2
    elif oper == "*":
        result = data1 * data2
    elif oper == "/":
        result = data1 / data2
    elif oper == "%":
        result = data1 % data2
    else:
        result = -1
    return result


def readExcel(file, sheetIndex):
    import xlrd
    fp = xlrd.open_workbook(file)
    case = fp.sheet_by_index(sheetIndex)
    for rowID in range(0, case.nrows):
        caseList.append(case.row_values(rowID))
    return caseList


def writeExcel(file, sheetName, content):
    import xlwt
    fp = xlwt.Workbook(encoding='utf-8')
    case = fp.add_sheet(sheetName)
    i = 0
    for rowInfo in content:
        j = 0
        for cellInfo in rowInfo:
            case.write(i, j, label=cellInfo)
            j = j + 1
        i = i + 1
    # case.write(i,j,label=content)
    fp.save(file)


caseList = readExcel(r'D:\computerCases.xls', 0)
title = caseList.pop(0)
title.extend(['Acturalresult', 'Status'])

for case2 in caseList:
    print(case2)
    acResult = computer(case2[2], case2[3], case2[4])
    if acResult == case2[5]:
        case2.extend([acResult, 'pass'])
    else:
        case2.extend([acResult, 'fail'])
caseList.insert(0, title)
writeExcel(r'D:\computerCases5.xls', 'computerResult', caseList)
