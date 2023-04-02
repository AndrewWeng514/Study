# @Time    : 2022/8/23 11:10
# @Author  : Andrew
# 输入一个学生学的姓名、成绩，如果成绩在90-100，等级为A；80-89，等级为B；70-79，等级为C；60-69，等级为D；小于60，等级为E
name = input('请输入学生姓名:')
score = input('请输入学生成绩:')
if score.isdigit():
    if int(score) > 100:
        print('请输入0-100的分数')
    elif 90 <= int(score):
        print(name, '的成绩为A')
    elif int(score) >= 80:
        print(name, '的成绩为B')
    elif int(score) >= 70:
        print(name, '的成绩为C')
    elif int(score) >= 60:
        print(name, '的成绩为D')
    else:
        print(name, '的成绩为E')
else:
    print('请输入正确的分数')

# stra='I am a  good student '
# # 1. 查找'good' 字符串下标位置
# print(stra.find('good'))
# # 2. 统计stra中，包含'a'的个数
# print(stra.count('a'))
# # 3. 将每个单词的首字母都大写
# print(stra.title())
# # 4. 将字符串stra中的所有单词都转换成大写，并打印输出
# print(stra.upper())
# # 5. 判断字符串“hello45” 是否只有数字，使用哪个函数？
# a = 'hello45'
# print(a.isdigit())
