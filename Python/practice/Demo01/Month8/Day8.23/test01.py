# @Time    : 2022/8/23 13:07
# @Author  : Andrew
# 1. 提示用户进行[1]注册和[2]登录的选择
#    如果用户选择1：提示"欢迎用户进行注册"
#    如果用户选择2：提示用户"欢迎登录,您想做什么操作？[1]查询，[2]取款，[3]存款，[4]转账"
#    	  如果用户选择1：提示"Welcome to search"
#    	  如果用户选择2：提示"welcome to get money"
#    	  如果用户选择3：提示"welcome to save money"
#    	  如果用户选择4：提示"welcome to transfer money"
# print('[1]注册','\n[2]登录')
# n = int(input())
# if n == 1:
#     print('欢迎用户进行登录')
# elif n==2:
#     print('欢迎登录,您想做什么操作?','[1]查询','[2]取款','[3]存款','[4]转账',sep='\n')
#     m = int(input())
#     if m ==1:
#         print('Welcome to search')
#     elif m==2:
#      print('welcome to get money')
#     elif m == 3:
#         print('welcome to save money')
#     elif m==4:
#      print('welcome to transfer money')
# else:
#     print('请输入正确选项')

# 2. 通过键盘接收输入，判断
#    3.1 如果输入的数据长度超过一位，提示"请输入一位数"
#    3.2 如果输入的数据长度刚好一位，判断输入的字符
#        如果是数字，打印："您输入了一个数字"
#        如果是字母，打印："您输入的是一个字母"
#        如果是空格，打印："您输入的是一个空格"
# #        如果是其他字符，打印："您输入的不是数字，字母，空格"
# n =input()
# if len(n)>1:
#     print('请输入一位数')
# elif len(n) == 1:
#     if n.isdigit()== True:
#         print('您输入了一个数字')
#     elif n.isalpha()==True:
#         print('您输入的是一个字母')
#     elif n == ' ':
#         print('您输入的是一个空格')
#     else:
#         print('您输入的不是数字，字母，空格')

# 1. 使用while死循环接收键盘数据，并把用户输入的数据打印处理
# while True :
#     n = input()
#     print()
# 2. 使用while循环，打印1-100之间的偶数
# m =2
# while m<101:
#     print(m)
#     m=m+2
# 3. 使用while循环，计算1-100之间的奇数之和
# m = 1
# n = 0
# while m <101:
#     n= n+m
#     m= m+2
# print(n)
# # 4. 输入1个正整数n,计算1~n的和，如果n=1,则和为1。
# n = int(input())
# m= 0
# d =1
# while d<=n:
#     m = m+d
#     d=d+1
# print(m)
# # 5. 使用while循环打印出100以内能够被9整除的数
# m = 1
# while m<100:
#     if m%9 == 0:
#         print(m)
#     m = m + 1

# # 1. 定义列表：NameBalanc=[['张三','1000'],['李四','800'],['王五','3000'],['孙七','2000']]
# NameBalanc=[['张三','1000'],['李四','800'],['王五','3000'],['孙七','2000']]
# # 2. 求NameBalance列表的长度是多少？
# print(len(NameBalanc))
# # 3. 查询王五的账户余额是多少？
# print(NameBalanc[-2][1])
# # 4. 将李四和王五的姓名及账户余额显示显示出来?
# print(NameBalanc[1],NameBalanc[-2])
# # 5. 查询李四名字的长度是多少？
# print(len(NameBalanc[1][0]))
# # 1. 创建一个空列表，命名为names, 往里面添加： Luna，Jack，Rain，Jam，Lucy，Young
# names=list()
# str =('Luna','Jack','Rain','Jam','Lucy','Young')
# names.extend(str)
# print(names)
# # 2. 在names列表中 Young 元素前面插入一个 Jane
# names.insert(-1,'Jane')
# print(names)
# # 3. 把names列表中的 Jack的名字改成 David
# names[1]='David'
# print(names)
# # 4. 在names 列表中，删除Lucy的名字(至少使用3种方法)，也可以使用for循环
# names.remove('Lucy')
# print(names)
# del names[-2]
# print(names)
# names.pop(-2)
# print(names)
# # 5. 在names列表中 插入一个子列表['Tom','Jerry'] ，并打印出Jerry的名字。
# list=['Tom','Jerry']
# names.append(list)
# print(names[-1][-1])
#
# # 6. 在names列表中，打印出Rain 的索引值（下标值）
# a=names.index('Rain')
# print(a)
# # 7. 创建列表[1,2,3,4] ，合并到names列表中（使用2种方法）
# list2=[1,2,3,4]
# names.extend(list2)
# names=names+list2
# print(names)
# # 8. 取出names列表中，最后3个元素。
# print(names[-3:])
# # 9. 删除name 列表中末尾的元素，删除两 次
# i= 1
# while i<3:
#     names.pop(-1)
#     i +=1
# print(names)
# # 10. 在name列表末尾添加 “Alex”。
# names.append('Alex')
# print(names)
# # 11. 在names列表中，添加三个Lucy，并在列表中统计Lucy的个数
# list =['Lucy']
# names = names +3*list
# num=names.count('Lucy')
# print(num)
# # 12. 将names列表中的内容反向输出
# print(names[::-1])
# for i in range(10):
#     j=1
#     while j<=i:
#         sum=i*j
#         print('%d×%d=%d'%(i,j,sum),end=' ')
#         j=j+1
#     print( )
# for i in range(1,10):
#     j = 1
#     while j<=i:
#         sum = i * j
#         print(f' {i}*{j} ={sum} ',end=' ')
#         j = j+1
#     print()
#
#
# for i in range(1, 10):
#     for j in range(1, i+1):
#         rs = i * j
#         print(f' {i}x{j}={rs:2}', end='')
#     print()

for i in range(1, 10):
    for j in range(i, 10):
        rs = i * j
        print(f' {i}x{j}={rs:2}', end='')
    print()
