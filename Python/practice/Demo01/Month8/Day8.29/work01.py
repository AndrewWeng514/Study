# @Time    : 2022/8/29 9:39
# @Author  : Andrew

'''
1. 一个班级有10个同学，
['Kate','Linda','Simon','Jack','John','Jane','Mike','Joyce','Windy','Rose']
使用随机方式进行抽奖，抽出五名中奖者，已经中奖的不重复抽取
抽奖方式：
1.1 抽中的名单从列表中删除，从剩下的名单中继续抽取
1.2 抽中的名单不从列表中删除，继续抽取
'''
import os
import random

# 第一种
'''
import random
list = ['Kate','Linda','Simon','Jack','John','Jane','Mike','Joyce','Windy','Rose']
list1 = [ ]
while True:
    num = random.randint(0,len(list)-1)
    if num not in list1:
         list1.append(num)
    if len(list1) == 5:
        break
for i in list1:
    print('中奖人员是:',list[i])
'''
# 第二种
'''
list = ['Kate','Linda','Simon','Jack','John','Jane','Mike','Joyce','Windy','Rose']
list1= []
while True:
    num = random.randint(0,len(list)-1)
    name = list.pop(num)
    list1.append(name)
    if len(list1) == 5:
        break
print('中奖人员是:\n',list1)
# 2.1
list = ['Kate','Linda','Simon','Jack','John','Jane','Mike','Joyce','Windy','Rose']
while True:
    num = random.randint(0,len(list)-1)
    list.pop(num)
    if len(list) == 5:
        break
print('中奖人员是:\n',list)
'''

# 第三种
'''
list = ['Kate','Linda','Simon','Jack','John','Jane','Mike','Joyce','Windy','Rose']
list1 = []
while True:
    num = random.randint(0,9)
    if num not in list1:
        list1.append(num)
        print('中奖人员:', list[num])
        if len(list1) == 5:
            break
    else:
        continue
'''
list = ['Kate', 'Linda', 'Simon', 'Jack', 'John', 'Jane', 'Mike', 'Joyce', 'Windy', 'Rose']
print(f'中奖人员:\n{random.sample(list, 5)}')
'''
3. 获取你当前正在编码的这个文件的文件名称，文件的路径信息，文件的大小信息
'''

import os

print(os.getcwd())  # 路径信息
print(os.path.basename('/E/practice/Demo1/Day8.29/work01.py'))  # 文件名称
print(os.path.getsize('work01.py'))  # 文件的大小

'''
5. 对如下列表中的元素进行类型的判断：
	[100,'hello',[20,30,40],('a','b','c'),{'ID':'1001'},{9,True,100}]
	说明：
		如果是number，按照格式'100 是number类型'进行显示
		如果是list，按照格式'[20,30,40]是list列表'进行显示
	.....

'''
'''
list = [100,'hello',[20,30,40],('a','b','c'),{'ID':'1001'},{9,True,100}]
for i in list:
    print(f'{i}是{str(type(i))[8:-2]}类型')
'''
