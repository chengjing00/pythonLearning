# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 上午10:48
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 09-循环语句.py
# @Software: PyCharm


index = 0
result = 0
while index <= 100:
    if index % 2 == 0:
        index += 1
        continue
    result += index
    index += 1

print(f"result:{result}")
