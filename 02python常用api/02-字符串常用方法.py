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
