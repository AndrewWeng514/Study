# while True:
#     try:
#         n, k = map(int, input().split(' '))
#         li = input().strip().split(' ')
#         print(' '.join(sorted(li)[:k]))
#     except:
#         break
#
#
# # 菜鸟做法
# num1, num2 = input().split(' ')
# list1 = input().split(' ')
# list2 = [int(num) for num in list1]
# list3 = sorted(list2)
# list4 = [str(num) for num in list3]
# print(' '.join(list4[:int(num2)]))
from math import ceil

#
# word = input().split(" ")
# num =input().split(" ")
# num = [int(i) for i in num]
# num.sort()
# for i in num[:int(word[-1])]:
#     print(i,end=" ")
# ['1', '2', '4', '9', '3', '55', '64', '25']


# length = int(input())
# num_list = input().split(" ")
# choice = input()
# num_list = [int(i) for i in num_list]
# if choice == "0":
#     num_list.sort()
#
# elif choice == "1":
#     num_list.sort(reverse=True)
# for i in num_list:
#     print(i,end=" ")

s = "asdfgjfhdgssdgffghg"
list = []
for i in s:
    if i not in list:
        list.append(i)
list.sort()
print(''.join(list))
