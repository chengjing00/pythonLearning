# -*- coding: utf-8 -*-
# @Time    : 2020-10-24 11:46
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 03-数据类型.py
# @Software: PyCharm

"""
1. 不同的数据，存储为不同的数据类型
2. 验证数据类型， 检测数据类型--- type(数据)
3. int float bool string list tuple dict
"""

# int -- 整型
num1 = 1
print("num1 type is", type(num1))

# float -- 浮点型
num2 = 1.1
print("num2 type is", type(num2))

# string --> str -- 字符串
num3 = "hello python"
print("num3 type is", type(num3))

# bool -- 布尔
b = True
print("b type is", type(b))

# list -- 列表
c = [10, 20, 30]
print("c type is", type(c))

# tuple -- 元组
d = (10, 20, 30)
print("d type is", type(d))

# set -- 集合
e = {10, 20, 30}
print("e type is", type(e))

# dict -- 字典（键值对）
f = {'name': 'tom', 'age': 18}
print("f type is", type(f))
