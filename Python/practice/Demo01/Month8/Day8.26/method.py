# @Time    : 2022/8/26 14:30
# @Author  : Andrew
def calculator(num1, option, num2):  # 计算器功能
    result = None
    if option == '+':
        result = num1 + num2
    elif option == '-':
        result = num1 - num2
    elif option == '*':
        result = num1 * num2
    elif option == '/':
        result = num1 / num2
    else:
        print('请输入正确的运算符号!')
    return result * 100


while True:
    num3 = int(input("请输入第一个数字:"))
    num4 = int(input('请输入第二个数字:'))
    option1 = input('请输入需要进行的运算:')
    data = calculator(num3, option1, num4)
    print(data)
