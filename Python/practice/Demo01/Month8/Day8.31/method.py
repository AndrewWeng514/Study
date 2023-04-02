# @Time    : 2022/8/31 10:25
# @Author  : Andrew
fd = open(r'./testData.txt', 'w+', encoding='utf-8')
print(fd.tell())
for i in range(5):
    fd.write('hello world !\n')
print(fd.tell())
fd.seek(0)
result = fd.read(3)
print(result)
