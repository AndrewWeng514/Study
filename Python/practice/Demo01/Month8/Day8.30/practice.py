# @Time    : 2022/8/29 20:55
# @Author  : Andrew

def factorial(n):
    if n == 1:
        return 1
    else:
        return (factorial(n - 1)) * n


print(factorial(4))


def rabbit(n):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit(n - 1) + rabbit(n - 2)


print(rabbit(12))

# def height():
#     height1 = 0.01
#     i = 0
#     while height1 < 884800.00:
#         height1 *=2
#         i+=1
#     return (i)
