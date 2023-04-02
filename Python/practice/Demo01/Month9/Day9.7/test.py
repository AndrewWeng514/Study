# @Time    : 2022/9/7 15:21
# @Author  : Andrew
num = 0
count1 = 0
while True:
    x = input()
    if x == 'False':
        break
    else:
        y = int(input())
        count1 += 1
        num += y
num1 = num / count1
print(f'{num1:.2f}')
