# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 下午7:09
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 05-数据类型转换.py
# @Software: PyCharm
# input 接收输入的类型都是 string 类型
num = input("please input data:")
print(type(num))

# str --> int  int()
print(int(num))

num1 = 10
str = "10"

# float()
print(float(str))

# str()
# print(str(num1))

# tuple()
list1 = [10, 20, 30]
print(tuple(list1))

# list()
t1 = (100, 200, 300)
print(list(t1))

# eval()
# print(eval(list1))
