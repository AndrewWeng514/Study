# # # @Time    : 2022/8/22 10:08
# # # @Author  : Andrew
# #
# #
# # print('\'how are you\'')
# # words = '\'how are you\''
# # print(words)
# #
# #
# #
# #
# # a='\'how\''
# # b='\'are\''
# # c='\'you\''
# # print(a,b,c,sep='')
# # print('\'how\',\'are\',\'you\'')
# #
# # a='\'how\''
# # b='\'are\''
# # c='\'you\''
# # print(a,b,c,sep='\n')
# # print('\'how\'\n\'are\'\n\'you\'')
# #
# # year = '2011'
# # mouth = '04'
# # day = '20'
# # print(year+'-'+mouth+'-'+day)
# #
# # a='*'
# # print(a,a,a,a,a,sep='  ')
# #
# # cbrand='华为'
# # ctype='mate book 15'
# # csize='15.6'
# # cprice= '4399'
# # print(cbrand,ctype,csize,cprice)
# #
# #
# # print('*\t'*5)
# # print('ho')
# # a = 34
# # a > 10 and print('hello world')
#
#
#
#
#
#
# # a=1
# # b='对方水电费'
# # c=231
# # print(f'我是{a},w叫{b},我的朋友{c}'.format(a=1,
# # b='对方水电费',
# # c=231))
# # name='zhangsa'
# # weight='75KG'
# # birth = '1990-01-01'
# # sex = 'Male'
# # score = 82.5
#
# # print(f'{name} is {sex},his weight is{weight}')
# # print(f'{name}|{weight}|{birth}|{sex}')
# # print(f'{name}\'s score is {score:.2f}分')
#
# # print('{}|{}|{}|{}|{}'.format(name,weight,birth,sex,score))
# #
# # id = 10001
# # passw = 123456
# # print(f'Your id is :{id},Your passwor is:{passw}')
# # a = (1,2,3,4,5,7)
# # b = ['瓮','胡','朱']
# # c = {a[1]:b[0]}
# # print(c)
# # if i=0 ,  < 6
# ### 练习：
#
# # 1. 分别定义6个类型的变量，并打印变量类型
# a = 1
# print(type(a))
# a = '1'
# print(type(a))
# a = (a,1,2)
# print(type(a))
# a = [a,1,2,3]
# print(type(a))
# a = {1:'你好'}
# print(type(a))
# a = {1,2,3,}
# print(type(a))
# # 2. 创建空字符串。
# a = ''
# print(a)
# # 3. 分别使用两种方法创建空列表，空元组，空字典
# a = list()
# b = []
# print(type(a),type(b))
# a = tuple()
# b = ()
# print(type(a),type(b))
# a = dict()
# b = {}
# print(type(a),type(b))
# # 4. 定义一个空集合
# a = set()
# print(type(a))
# # 5. 在元组中，定义一个值
# a = (1,)
# print(a)
# print(type(a))
# ### 练习：
#
# # 1. 将字符串“hello，world” 重复输出10遍
# a = 'hello,world\n'
# print(a*10)
# #
# # 2. 将字符串"I love" 和 "python" 连接起来
# a = 'I love'
# b = ' python'
# print(a+b)
# print ('I love',' python')
# #
# # 3. 1111被19整除后得到的结果是？
# print(1111//19)
# #
# # 4. 总共有100图片，想根据图片的id进行区分，分别存放在4个文件夹中，此时你会采取什么方法对图片进行区分？
# 元祖
# #
# # 5. 判断变量  temp_a 是否等于temp_b，使用什么判断，为什么？
#
# print(temp_a ==temp_b )
# #
# # 6. 写出以下表达式的结果：
# #
# print('a'  in ['1','a','abc','11'])
# print( 5 and 0)
# print(5  or 0)
# print(7>1 and 8< 2)
# print(3>=2 or 4>9)
# print(1==1 and 5>2)
# print(True+5)
# print(False-4)
# print((1+3) > 2 or 4 > 6 and 3 < 2)
# # print(7< 10 and (4 > 1 or 5 < 7)  and  8 > 4)
# import math
# import random
#
# # 1. 求 5的10次方得多少
# print(5**10)
# #
# # 2. 求x的平方
# x = int(input())
# print(math.pow(x,2))
# #
# # 3. 给10开平方根
#
#
# print(math.sqrt(10))
# #
# # 4. 循环输出50个数
# for i in range(50):
#     print(i)
# #
# # 5. 设置变量 a=7 ,b=8,  计算`（a+b）* 3+（4*a+8b）`的结果
# a = 7
# b = 8
# print((a+b)* 3+(4*a+8*b))
# #
# # 6. 打印99~999之间的数，并且设置设置步长为4.
### 练习：

# 1. 定义字符串“helloworld”,  反向输出world
a = 'helloworld'
print(a[9:4:-1])
# 2. 创建字符串变量，mystr='I have a dream'
mystr = 'I have a dream'
# 3. 截取：'have'  字符，使用多种方式截取
print(mystr[2:6])
print(mystr[-12:-7])
# 4. 读取mystr字符串中，第二个字母'e'
print(mystr[-3])
# 5. 将该字符串反向输出
print(mystr[::-1])
# 6. 截取'rd a e' 字符，使用多种方式截取
print(mystr[-4:-10:-1])
print(mystr[10:4:-1])
# 7. 截取'h r' 字符
print(mystr[2::4])
# 8. 截取'av' 字符，使用多种方式
print(mystr[3:5])
print(mystr[-11:-9])
# 9. 截取'mde' 字符
print(mystr[-1:-10:-4])
# 10. 截取 'Ier'  字符，使用多种方式
print(mystr[::5])
print(mystr[-14::5])
### 练习：

stri = 'Everyone have a dream. Someone may want to be rich, someone  may want to be beautiful, and someone may want to have power.'

# 1. 查找字符串 stri 中的“dream” 的下标，使用两种方法。
print(stri.find('dream'))
print(stri.index('dream'))
#
# 2. 统计字符串 stri 中'o' 的个数，统计字符串'may'出现的次数。
print(stri.count('o'))
print(stri.count('may'))
#
# 3. 求字符串 stri 的长度是多少？
print(len(stri))
#
# 4. 求字符串 stri 中的字母的个数。
a = len(stri)
b = stri.count(' ')
c = stri.count('.')
d = stri.count(',')
print(a - b - c - d)

#
# 5. 按如下格式输出内容：
#
#    ```python
#    **************Everyone have a dream***************
#    *********** Someone may want to be rich***********
#    ******** someone  may want to be beautiful********
#    ******* and someone may want to have power.*******
#    ```
word1 = '   python'
word2 = 'Everyone have a dream'
word3 = 'Someone may want to be rich'
word4 = 'Someone may want to be beautiful'
word5 = 'and someone may want to have power. '
print(word1, word2.center(40, '*'), word3.center(40, '*'), word4.center(40, '*'), word5.center(40, '*'), sep='\n')

#
# 6. 新字符串：
newStri = 'Everyone have a dream\n. Someone may want to be rich\n, someone  may want to be beautiful\n, and someone may want to have power\n.'
#
#    将newStri中字符串中的\n去掉，将内容以一行输出（不要换行）。
print(newStri.replace('\n', ''))

for i in range(1, 101, 2):
    a += i

    print(a)
