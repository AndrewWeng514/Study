# @Time    : 2022/8/23 18:23
# @Author  : Andrew
# 1. 统计100-999之间有多少个数字个位，十位，百位上的数字相加=15

from ast import main

for i in range(100, 1000):
    bai = i // 100
    shi = i // 10 % 10
    ge = i % 10
    if bai + shi + ge == 15:
        print(i)

# 2. 有1,2,3,4 四个数字，能组成多少个互相不相同且无重复数字的三位数，分别都是多少？
count = 0
for a in range(1, 5):
    for b in range(1, 5):
        if a == b:
            continue
        else:
            for c in range(1, 5):
                if a == c or b == c:
                    continue
                else:
                    print(a, b, c, sep='')
                    count += 1
print('总计', count)
# 3. 输入1个3位的正整数，判断这个数是否为水仙花数（每一位上数字的立方和等于这个数本身，比如：153=5**3+3**3+1**3
while True:
    num = input('请输入3位正整数')
    if num.isdigit():
        if len(num) == 3:
            i = int(num)
            bai = i // 100
            shi = i // 10 % 10
            ge = i % 10
            if bai ** 3 + shi ** 3 + ge ** 3 == i:
                print(i, '是水仙花数')
            else:
                print(i, '不是水仙花数')
        else:
            print('请输出3位整数')
    elif num == 'q':
        break
    else:
        print('请输入数字')
# 4.例子3:将字符串'asd%^&dasDFGH@#$%^&123435DFGH$%^&*'中的特殊符号去除
str = 'asd%^&dasDFGH@#$%^&123435DFGH$%^&*'
str1 = '!@#$%^&*?<>:"'
str2 = list()
for i in str:
    if i in str1:
        continue
    else:
        str2.append(i)
str3 = ''.join(str2)
print(str3, type(str3))
# 5. 查找每个want单词在字符串stri中的位置，
stri = 'Everyone have a dream. Someone may want to be rich, someone  may want to be beautiful, and someone may want to have power.'
# i=stri.find('want')
# print(i)
# i=stri.find('want',i+1)
# print(i)
# i=stri.find('want',i+1)
# print(i)
# i=stri.find('want',i+1)
# print(i)


if __name__ == '__main__':
    stri = 'Everyone have a dream. Someone may want to be rich, someone  may want to be beautiful, and someone may want to have power.'
    i = 0
    while True:
        if i != -1:  # 查找不到返回-1
            i = stri.find('want', i)
            print(i)
            i = stri.find('want', i + 1)
        else:
            False

# 6.对下列列表进行处理：
stuInfo = [
    [1001, 'Kate', 185, 'Female', [70, 90, 98]],
    [1002, 'Mike', 165, 'Male', [75, 90, 100, 50, 98]],
    [1003, 'John', 170, 'Male', [100, 88, 98, 76]]
]
#
# 场景1. 支持性别查询操作，输入'Female'，统计女生有多少个？输入'Male',统计男生有多少个，支持反复统计
while True:
    str = input("请输入性别:")
    m = 0
    count = 0
    while m < len(stuInfo):
        i = stuInfo[m][3]
        if i == str:
            count += 1
            m += 1
        else:
            m += 1
    print(count)

#   场景2：对该stuinfo学生信息，使用while编写代码统计有多少个学生成绩平均分超过90分
# list= stuInfo[0][4]
# print(list)
# sum = sum(list)
# print(sum)
# avgscore = sum/len(list)

m = 0
count = 0
while m < len(stuInfo):
    i = stuInfo[m][4]
    avgscore = sum(i) / len(i)
    if avgscore > 90:
        print(stuInfo[m][2], avgscore)
        count += 1
        m += 1
    else:
        m += 1
print(count)
