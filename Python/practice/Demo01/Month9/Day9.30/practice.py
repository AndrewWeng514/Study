"""
 @Author: Andrew
 @FileName: practice.py
 @DateTime: 2022/9/29 13:56
"""
words = input().upper()
choice = input()
dict = {}
for i in words:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
if choice in dict:
    print(dict[choice])
else:
    print(" ")
