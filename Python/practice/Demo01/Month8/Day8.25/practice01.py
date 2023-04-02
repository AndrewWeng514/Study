# @Time    : 2022/8/25 9:21
# @Author  : Andrew
# 1. 执行如下操作，看两个变量a和b是否一致？
a = (5)
print(type(a))
b = (5,)
print(type(b))
a = (100)
print(type(a))
a = ("hello")
print(type(a))
a = ([1, 2, 3])
b = ((1, 2, 3),)
print(a)
print(b)

# 2. 分别计算如下元组的元素数量，最大，最小
# ("how","are","you")   -> 分别查看 how 和 How 是否存在
# (100,87,99,True)           -> 分别查看 100,100.00是否存在
tuple1 = ('how', 'are', 'you')
result = 'how' in tuple1
print(result)
result2 = 'How' in tuple1
print(result2)
tuple2 = (100, 87, 99, True)
result3 = 100 in tuple2
print(result3)
result4 = 100.00 in tuple2
print(result4)
# 3. 将如下信息存储到一个元组stu中
stu = (1001, "Mike", "2020-01-01", 165, True, ["唱歌", "跳舞", "跑步"])
# 对stu元组分别执行切片操作，查看如下数据
# 场景1: 返回学生ID
print(stu[0])
# 场景2：返回学生兴趣爱好
print(stu[-1])
# 场景3：返回学生姓名，出生日期，身高
print(stu[1:4])
# 场景4：返回身高及以后的所有信息
print(stu[-3:])
# 场景5：修改身高165为178
list1 = list(stu)
print(list1, type(list1))
height = list1.index(165)
list1[height] = 178
stu = tuple(list1)
# 场景6：返回学生兴趣爱好的个数
tuple4 = stu[-1]
print(len(tuple4))  #
# 4. 在2的基础上，判断如下信息是否在元组中
# 场景1：Mike
# 场景2：跳舞
stu = (1001, "Mike", "2020-01-01", 165, True, ["唱歌", "跳舞", "跑步"])
result5 = 'Mike' in stu
result6 = '跳舞' in stu[-1]
print(result5)
print(result6)

# 5. 在2的基础上，将元组stu中元素转化成列表存储   list(元组)    tuple(列表)
list2 = list(stu)
print(list2, type(list2))

tuple5 = tuple(stu)
print(tuple5, type(tuple5))

# 6. 在2的基础上，删除元组stu
# del stu
del stu
