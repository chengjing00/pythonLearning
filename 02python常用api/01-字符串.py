# -*- coding: utf-8 -*-
# @Time    : 2020-10-25 16:43
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 01-字符串.py
# @Software: PyCharm
"""
1. 字符串
"""
a = "hello world"
print(f"a:{a}")
print(f"a:{type(a)}")

b = '''i love python'''
print(f"b:{b}")
print(f"b:{type(b)}")

str1 = "abcdefg"
print(f"str1:{str1}")

# 字符串下标
print(f"str1[2]:{str1[2]}")

# 切片 [开始位置下标:结束位置下标:步长] （左闭右开）
str = str1[1:3:1]
print(f"str:{str}")

# 倒序
str = str1[::-1]
print(f"str:{str}")

# 倒数
str = str1[-4:-1:1]
print(f"str:{str}")

#

