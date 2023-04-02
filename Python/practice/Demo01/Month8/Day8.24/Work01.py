# @Time    : 2022/8/24 18:47
# @Author  : Andrew
# 1. 给出一个字符串，在程序中赋初值为一个句子，例如comment=“To improve is to change;to be perfect is to change often.”
# 需要：计算句子中各字符出现的次数
comment = 'To improve is to change;to be perfect is to change often.'
dic = {}
for i in comment:

    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic.fromkeys(i)
        dic[i] = 1
print(dic)
# for k,v in dic.items():
#     print(f'{k}出现了{v}次')

# 2. 生成100个卡号，具体要求如下：
# ---1. 卡号以6102009开头， 后面3位依次是 （001， 002， 003…… 100）
# ---2. 生成关于银行卡号的字典， 默认每个卡号的初始密码为"redhat";
dic = dict()
list = []
for i in range(1, 101):
    str = ('6102009%.3d' % i)
    #   str=(f'6102009{i:03d}')
    list.append(str)
print(list)
new = dic.fromkeys(list, 'redhat')
print(new)
