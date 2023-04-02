"""
 @Author: Andrew
 @FileName: websocket.py
 @DateTime: 2022/9/29 16:27
"""
word = input()
if word == "":
    print(word)
elif len(word) < 8:
    print(f"{word:08s}")
else:
    print(word)
