"""
 @Author: Andrew
 @FileName: close.py
 @DateTime: 2022/10/18 12:04
 @Brief:闭包函数的实现

"""
import time


def get_time(fuc):
    def inner():
        star = time.time()
        time.sleep(1)
        fuc()
        end = time.time()
        print(end - star)

    return inner


@get_time
def test():
    print("你好呀!")


# test()
# f = get_time(test)
# print(f)
# f()
def closer(fun):
    def inner(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        end = time.time()
        print(end - start)

    return inner


@closer
def input1(user, name, age, hobby="游泳"):
    print(f"{user} is {name},he age is {age},hobby is{hobby}")


# input1("1号","张三","15",hobby = "跑步")


def wrapper1(*args, **kwargs):
    def closer(fun):
        def inner():
            start = time.time()
            for i in args:
                fun(*i, **kwargs)
            end = time.time()
            print(end - start)

        return inner

    return closer


@wrapper1(*[["1号", "张三", "15", "跑步"], ["2号", "李四", "18", "游泳"]])
def input2(user, name, age, hobby):
    print(f"{user} is {name},he age is {age},hobby is{hobby}")


input2()
