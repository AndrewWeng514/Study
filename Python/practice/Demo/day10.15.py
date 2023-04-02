"""
 @Author: Andrew
 @FileName: day10.15.py
 @DateTime: 2022/10/14 17:38
"""
#  ASCII码 A-Z 65-90  a-z 97-122
# def passwd(m):
#     k = ord(m)
#     if k in range(64, 90):
#         m = chr(k + 33)
#     elif k == 90:
#         m = "a"
#     elif k in range(97, 123):
#         if k == 122:
#             m = 9
#         else:
#             if k >= 115:
#                 k -= 1
#             k = k - 97
#             m = k // 3 + 2
#     else:
#         m = m
#     return m
#
#
# s = input()
# for i in s:
#     print(passwd(i), end="")
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(0)
    else:
        num = 0
        while n > 1:
            new = (n + 1) // 3
            num += new
            n = (n + 1) // 3 + (n + 1) % 3 - 1
        print(num)
