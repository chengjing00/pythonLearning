# -*- coding: utf-8 -*-
# @Time    : 2020-10-25 17:37
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 02-字符串常用方法.py
# @Software: PyCharm

mystr = "hello world and itcast and itheima and python"
# 查找 find(子串，开始位置下标，结束位置下标)  不存在返回-1
f = mystr.find('l', 0, len(mystr))
print(f"find-f:{f}")

f = mystr.find("and")
print(f"find-f:{f}")

# index
f = mystr.index("and")
print(f"index-f:{f}")

# count(子串，开始位置下标，结束位置下标)
c = mystr.count("and")
print(f"count-c:{c}")

# * 操作 --> 重复 n 次
m = "hello "
mm = m * 3
print(f"*-mm:{mm}")

# + 操作， 拼接字符串
m = "hello "
n = "world"
mn = m + n
print(f"m+n:{mn}")

# len() 计算字符串的长度
str = "hello world"
print(f"length:{len(str)}")

# capitalize   获得字符串首字母大写的拷贝
print(f"capitalize:{str.capitalize()}")

# title 获得字符串每个单词首字母大写的拷贝
print(f"title:{str.title()}")

# upper 获得字符串变大写后的拷贝
print(f"upper:{str.upper()}")

# find() 从字符串中查找子串所在位置, 如果未找到返回-1
print(f"find():{str.find('or')}")
print(f"find():{str.find('shit')}")

# index 与find类似但找不到子串时会引发异常
# print(f"index:{str.index('or')}")
# print(f"index:{str.index('shit')}")

# startswith()  检查字符串是否以指定的字符串开头
print(f"startswith:{str.startswith('Hel')}")
print(f"startswith:{str.startswith('hel')}")

# endswith() 检查字符串是否以指定的字符串结尾
print(f"endswith:{str.endswith('ld')}")
print(f"endswith:{str.endswith('lD')}")

# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(f"center:{str.center(50,'*')}")
