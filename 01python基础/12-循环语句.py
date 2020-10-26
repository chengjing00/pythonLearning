# -*- coding: utf-8 -*-
# @Time    : 2020-10-25 11:08
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 12-循环语句.py
# @Software: PyCharm

"""
1. while 条件：
    {}
"""
index = 0
while index < 100:
    print(f"index:{index}")
    index += 1

'''
2. for 临时变量 in 序列:
    
'''
for c in "hello world":
    print(f"c:{c}")

"""
3. while 条件 else ...
    while正常结束之后执行else语句
"""

index = 0
while index <= 10:
    print(f"index:{index}")
    break
    index += 1
else:
    print("over")
