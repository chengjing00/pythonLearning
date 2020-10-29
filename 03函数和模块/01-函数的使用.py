# -*- coding: utf-8 -*-
# @Time    : 2020-10-29 13:58
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 01-函数的使用.py
# @Software: PyCharm

# 函数的定义

def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


# m = int(input('m = '))
# n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
# print(fac(m) // fac(n) // fac(m - n))


from random import randint


# 函数中的默认参数
def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))



# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))