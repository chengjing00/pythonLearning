# -*- coding: utf-8 -*-
# @Time    : 2020-10-24 13:11
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 07-数据类型转换.py
# @Software: PyCharm

# 数据类型转换
#  数据类型转换函数
"""
    int(x,base)
    float(x)
    str(x)
    eval(x)
    tuple(x)
    list(x)
"""

# str --> int
# age = int(input("age:"))
# print(f"age:{age}")
# print(f"age type:{type(age)}")

# 1. float()
num1 = 1
print(f"float:{float(num1)}")
print(f"float:{type(float(num1))}")

str1 = 10.123
print(f"float:{float(str1)}")
print(f"float:{type(float(str1))}")

# 2. str(): int --> str
print(f"str:{str(num1)}")
print(f"str:{type(str(num1))}")

# 3. tuple() -- 元素 list --> tuple
list1 = [10, 20, 30]
print(f"tuple:{tuple(list1)}")
print(f"tuple:{type(tuple(list1))}")

# list() -- 列表  tuple -- list
t1 = (10, 20, 30)
print(f"list:{list(t1)}")
print(f"list:{type(list(t1))}")

# eval() -- 计算在字符串中有效对python表达式（转换为数据原来的类型），并返回一个对象
str2 = '1'
print(f"eval:{eval(str2)}")
print(f"eval:{type(eval(str2))}")

str3 = '1.1'
print(f"eval:{eval(str3)}")
print(f"eval:{type(eval(str3))}")

str4 = '(100,200,300)'
print(f"eval:{eval(str4)}")
print(f"eval:{type(eval(str4))}")

str5 = '[100,200,300]'
print(f"eval:{eval(str5)}")
print(f"eval:{type(eval(str5))}")
