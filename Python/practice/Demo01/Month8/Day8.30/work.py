# @Time    : 2022/8/29 20:55
# @Author  : Andrew
# 1.
"""
制造场景，对如下异常进行捕获处理：
TypeError
NameError
IndexError
KeyError
AttributeError
"""
# 代码实现

# print(1+'a')

# print(a)

# a=(1,2)
# print(a[3])

# dic={}
# print(dic[1])

# a ='sadsad'
# a.extend

# 2.
"""
定义一个函数进行除法运算，分别在函数内外进行异常处理
"""
#
# def division(num1, ope, num2):
#     num1 = int(num1)
#     num2 = int(num2)
#
#     if ope == '+':
#         result = num1 + num2
#     if ope == '-':
#         result = num1 - num2
#     if ope == '*':
#         result = num1 * num2
#     if ope == '/':
#         result = num1 / num2
# num1, ope, num2 = input().split(' ')
# if ope not in ['-','+','*','/']:
#    print('请输入正确的符号')
# else:
#     division(num1, ope, num2)

# 3.
"""
定义一个computer函数负责进行加减乘除求余等运算；
将如下列表testData中的用例逐一提取出来，传递给computer进行运算，在适当位置添加异常处理，
统计正常用例执行的次数，异常用例执行的次数，已经所有的用例
"""
testData = [(10, '+', 20), (10, '*', 100), (9, '/', 0), (60, '%', 8), (100, '-', '39'), (20, '+')]


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


allcount = 0
errorcount = 0
count = 0
for i in testData:
    try:
        computer(i[0], i[1], i[2])
    except SyntaxError:
        print('这是一个 SyntaxError 错误')
        errorcount += 1
    except TypeError:
        print('这是一个 TypeError 错误')
        errorcount += 1
    except AssertionError:
        print('这是一个 SyntaxError 错误')
        errorcount += 1
    except AttributeError:
        print('这是一个 AttributeError 错误')
        errorcount += 1
    except IOError:
        print('这是一个 IOError 错误')
        errorcount += 1
    except ImportError:
        print('这是一个 ImportError 错误')
        errorcount += 1
    except IndexError:
        print('这是一个 IndexError  错误')
        errorcount += 1
    except:
        print('这是一个 IndexError  错误')
        errorcount += 1
    else:
        print(f'{i}执行通过')
        count += 1
    allcount += 1
print(f'执行成功: {count} \n执行失败: {errorcount}\n共执行用例: {allcount}')
