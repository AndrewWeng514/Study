comment = 'To improve is to change;to be perfect is to change often.'
dic = {}
for i in comment:
    dic.fromkeys(i)
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
print(dic)
