# -*- coding: utf-8 -*-
# @Time    : 2020-10-24 13:06
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 06-输入.py
# @Software: PyCharm
"""
1. 书写input
    input('提示信息')

2. 观察特点
    1. 遇到input， 等待用户输入
    2. 接受input 输入
    3. input 接收到对数据类型都是字符串
"""

password = input("请输入密码：")

print(f"您输入对密码是:{password}")

print(f"input data type is {type(password)}")