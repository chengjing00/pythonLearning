# -*- coding: utf-8 -*-
# @Time    : 2020-10-24 12:05
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 04-格式化输出.py
# @Software: PyCharm

# %s -- string
# %f -- float
# %d -- int
# %u -- unsigned int (无符号整数)

name = "tom"
age = 12
weight = 89.1
id = 231

print("我的名字是%s, 今年%d岁，体重%0.2f斤，学号是%05d" % (name, age, weight, id))
