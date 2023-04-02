"""
 @Author: Andrew
 @FileName: day10.11.py
 @DateTime: 2022/10/11 9:20
"""
import math

# word = input()
# # if len(word)%8 == 0:
# #     print(word)
# if len(word)<=8:
#     print(f"{word:0<8}")
# else:
#     for i in range((len(word)//8)):
#         print(word[i*8:(i+1)*8])
#     if len(word)%8 != 0:
#         a=len(word)//8
#         # print(a)
#         word1 = word[a*8:]
#         print(f"{word1:0<8}")
#
#     # print(f"{word:08s}" )
#     # a = math.ceil(len(word) / 8) * 8 - len(word)
#     # word = word+"0"*a
#     # for i in range(len(word)//8):
#     #     print(word[])

# list=[]
# def f (n):
#     for i in range(2,10):
#         if n%i == 0 :
#             list.append(i)
#             n = n // i
#             if n == 1:
#                 print(list)
#
#             # else:
#             #     f(n)
#
# a = f(180)
# print(a)

# n = int(input())
# dict = {}
# for i in range(n):
#     key,values = input().split(" ")
#     key = int(key)
#     values = int(values)
#     if key in dict:
#         dict[key] += values
#     else:
#         dict[key] = values
#         # print(dict)
# for key in sorted(dict):
#     print(int(key),int(dict[key]))
#
# def  f() :
#     list1 = []
#     word = input()
#     for i in word:
#         if i not in list1:
#             list1.append(i)
#     print(len(list1))
# f()
#
# num = int(input())
# num = str(num)
# print(num[::-1])

# a = "asdsad"
# print()

# word = input()
# word = word.split(" ")
# for j in word:
#     i = j[::-1]
# print(' '.join(word[::-1]))

# def f():
#     word_list = []
#     n = int(input())
#     for i in range(n):
#         word = input()
#         word_list.append(word)
#     word_list = sorted(word_list)
#     return word_list
# words = f()
# for i in words:
#     print(i)

# num = int(input())
# num = bin(num)
# num = num[2:]
# print(num.count("1")
