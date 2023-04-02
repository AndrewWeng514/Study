# @Time    : 2022/9/1 12:33
# @Author  : Andrew
for i in range(1, 100):
    age = i ** 3
    age1 = i ** 4
    if 999 < age < 10000:
        if 99999 < age1 < 1000000:
            a = str(age) + str(age1)
            for j in a:
                if a.count(j) != 1:
                    break
            else:
                print(i)

    #     continue

    # else:
    # break
