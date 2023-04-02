# -*- coding: utf-8 -*-
# @Time : 2022/10/4 15:44
# @Author : Andrew
# @File : Day10.4.py
# @Project : practice


def query():
    print(f"你的余额是{money}")


def add(num):
    global money
    money += int(num)
    print(f"当前余额是{money}")


def reduce(num):
    global money
    money -= int(num)
    print(f"当前余额是{money}")


def menu():
    print("1.查询当前余额"
          "\n2.存款"
          "\n3.取款")


money = 5000
name = input()
while True:
    menu()
    choice = int(input("请输入你的选择"))
    if choice == 1:
        query()
        continue
    elif choice == 2:
        num = input("请输入存款金额")
        add(num)
    elif choice == 3:
        num = input("请输入存款金额")
        reduce(num)
    else:
        break
