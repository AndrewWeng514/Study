"""
 @Author: Andrew
 @FileName: day10.8.py
 @DateTime: 2022/10/8 14:26
"""
"""
创建一个依次包含键-值对'<': 'less than'和'==': 'equal'的字典operators_dict，
先使用print()语句一行打印字符串'Here is the original dict:'，
再使用for循环遍历 已使用sorted()函数按升序进行临时排序的包含字典operators_dict的所有键的列表，
使用print()语句一行输出类似字符串'Operator < means less than.'的语句；
对字典operators_dict增加键-值对'>': 'greater than'后，
输出一个换行，再使用print()语句一行打印字符串'The dict was changed to:'，
再次使用for循环遍历 已使用sorted()函数按升序进行临时排序的包含字典operators_dict的所有键的列表，
使用print()语句一行输出类似字符串'Operator < means less than.'的语句，确认字典operators_dict确实新增了一对键-值对。"""

# operators_dict = {"<": "less than", "==": "equal"}
# print("Here is the original dict:")
# for i in sorted(operators_dict):
#     print(f"Operator {i} means {operators_dict[i]}")
# operators_dict[">"] = "greater than"
# print("\nThe dict was changed to:")
# for i in sorted(operators_dict):
#     print(f"Operator {i} means {operators_dict[i]}")

"""
又到了毕业季，牛牛作为牛客大学的学生会主席，决定对本校的应届毕业生进行就业调查。
他创建了一个依次包含字符串'Niumei'、'Niu Ke Le'、'GURR'和'LOLO'的列表survey_list，作为调查名单；
又创建了一个依次包含键-值对'Niumei': 'Nowcoder'和'GURR': 'HUAWEI'的字典result_dict，作为已记录的调查结果。
请遍历列表survey_list，如果遍历到的名字已出现在 包含字典result_dict的全部键的列表 里，
则使用print()语句一行输出类似字符串'Hi, Niumei! Thank you for participating in our graduation survey!'的语句以表达感谢，
否则使用print()语句一行输出类似字符串'Hi, Niu Ke Le! Could you take part in our graduation survey?'的语句以发出调查邀请。
"""
# survey_list = ['Niumei','Niu Ke Le','GURR','LOLO']
# result_dict = {'Niumei': 'Nowcoder','GURR': 'HUAWEI'}
# for i in survey_list:
#     if i in result_dict:
#         print (f'Hi, {i}! Thank you for participating in our graduation survey!')
#     else:
#         print(f'Hi, {i}! Could you take part in our graduation survey?')

"""
创建一个依次包含键-值对{'name': 'Niuniu'和'Student ID': 1}的字典my_dict_1，
创建一个依次包含键-值对{'name': 'Niumei'和'Student ID': 2}的字典my_dict_2，
创建一个依次包含键-值对{'name': 'Niu Ke Le'和'Student ID': 3}的字典my_dict_3，
创建一个空列表dict_list，使用append()方法依次将字典my_dict_1、my_dict_2和my_dict_3添加到dict_list里，
使用for循环遍历dict_list，对于遍历到的字典，使用print()语句一行输出类似字符串"Niuniu's student id is 1."的语句以打印对应字典中的内容。
"""
# my_dict_1 = {'name': 'Niuniu','Student ID': 1}
# my_dict_2 = {'name': 'Niumei','Student ID': 2}
# my_dict_3 = {'name': 'Niu Ke Le','Student ID': 3}
# dict_list = []
# dict_list.append(my_dict_1)
# dict_list.append(my_dict_2)
# dict_list.append(my_dict_3)
# # print(dict_list)
# for i in dict_list:
#     print(f"{i['name']}'s student id is {i['Student ID']}")


"""
创建一个依次包含键-值对'Beijing': {Capital: 'China'}、'Moscow': {Capital: 'Russia'}和'Paris': {Capital: 'France'}的字典cities_dict，
请使用for循环遍历"已使用sorted()函数按升序进行临时排序的包含字典cities_dict的所有键的列表"，
对于每一个遍历到的城市名，使用print()语句一行输出类似字符串'Beijing is the capital of China!'的语句。
"""
# cities_dict = {'Beijing': {"Capital": 'China'},'Moscow': {"Capital": 'Russia'},'Paris': {"Capital": 'France'}}
# for i in sorted(cities_dict):
#     print(f"{i} is the capital of {cities_dict[i]['Capital']}!")

"""
驼瑞驰调查了班上部分同学喜欢哪些颜色，并创建了一个依次包含键-值对'Allen': ['red', 'blue', 'yellow']、'Tom': ['green', 'white', 'blue']和'Andy': ['black', 'pink']的字典result_dict，作为已记录的调查结果。
现在驼瑞驰想查看字典result_dict的内容，你能帮帮他吗？
使用for循环遍历"使用sorted()函数按升序进行临时排序的包含字典result_dict的所有键的列表"，对于每一个遍历到的名字，先使用print()语句一行输出类似字符串"Allen's favorite colors are:"的语句，然后再使用for循环遍历该名字在字典result_dict中对应的列表，依次输出该列表中的颜色。"""
# result_dict = {'Allen': ['red', 'blue', 'yellow'],'Tom': ['green', 'white', 'blue'],'Andy': ['black', 'pink']}
# for i in sorted(result_dict):
#     print(f"{i}'s favorite colors are:")
#     for j in result_dict[i]:
#         print(j)

"""
描述
牛牛有两份列表，一份记录了牛客网用户的名字，另一份记录他们使用的语言。假设两份列表一一对应，请使用zip函数将两份列表封装为字典，以名字为key，语言为value，然后直接输出字典。
输入描述：
第一行输入多个字符串表示用户名字，以空格间隔。
第二行输入多个字符串表示使用的语言，以空格间隔。
输出描述：
直接输出两个列表组成的字典。
示例1
输入：
Niuniu NIumei Niukele
C C++ Python
复制
输出：
{'Niuniu': 'C', 'NIumei': 'C++', 'Niukele': 'Python'}
"""
# list  = input().split(" ")
# list1  = input().split(" ")
# dict1 =dict()
# for i in range(len(list)):
#     dict1[list[i]]=list1[i]
# print(dict1)

"""
描述
正在学习英语的牛妹笔记本上准备了这样一个字典：{'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}。
请你创建这样一个字典，对于牛妹输入的字母，查询有哪些单词？
输入描述：
输入一个字母，必定在上述字典中。
输出描述：
同一行中依次输出每个单词，单词之间以空格间隔。
示例1
输入：
a
复制
输出：
apple abandon ant 
"""
# dict1 = {'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}
# word = input()
# for i in dict1[word]:
#     print(i,end=" ")

"""
正在学习英语的牛妹创建了一个字典：{'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}。现牛妹新学了一个字母letter，以及一个新单词word，请把它们增加到字典中，再输出更新后的字典。
输入描述：
第一行输入一个新字母letter，
第二行输入一个新单词word。
输出描述：
输出更新后的整个字典。
示例1
输入：
e
egg
复制
输出：
{'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down', 'e': 'egg'}
"""
# dict1 =  {'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}
# letter = input()
# word =input()
# dict1[letter]=word
# print(dict1)


"""
Python的字典可以用来计数，让要被计数的元素作为key值，它出现的频次作为value值，只要在遇到key值后更新它对应的value即可。现输入一个单词，使用字典统计该单词中各个字母出现的频次。
输入描述：
输入一个字符串表示单词，只有大小写字母。
输出描述：
直接输出统计频次的字典。
示例1
"""


# word = input()
# dict1 ={}
# for i in word:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# print(dict1)


# num_list = input().split(" ")
# num_list = [int(num_list[i]) for i in range(len(num_list))]
# # print(sum(num_list))


# word = int(input())
# print(hex(word))  #转化为十六进制
# print(bin(word))  #转化为二进制

# nums = input().split()
# nums = [int(nums[i]) for i in range(len(nums)) ]
# print(nums[0]**nums[1])
# print(nums[1]**nums[0])

# num_list = input().split()
# num_list = [int(num_list[i]) for i in range(len(num_list))]
# print(num_list.count(0))


# name_list = input().split()
# print(name_list.index("NiuNiu"))

# word = input()
# print(word.isalpha())
# print(word.isdigit())
# print(word.isspace())


# words = []
# while True:
#     word = input()
#     if word != "0":
#         words.append(word)
#     else:
#         break
# print(" ".join(words))

# word = input()
# print(word.replace("*","b"))

# float1 = float(input())
# print(round(float1,2))

# words = input()
# print(eval(words))

# name_list = input().split(" ")
# print(sorted(set(name_list)))

# 计算机
# def cal(x,y):
#     print(x-y)
#     print(y-x)
# x = int(input())
# y = int(input())
# cal(x,y)

#  递归函数
def f(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n > 2:
        return f(n - 1) + f(n - 2)


nums = int(input())
print(f(nums))
