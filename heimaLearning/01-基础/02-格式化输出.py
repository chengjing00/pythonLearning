# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 下午8:23
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 02-格式化输出.py
# @Software: PyCharm

# %s 字符串
# %d 整数
# %f 浮点数
# %c 字符
# %u 无符号整数
# %o 八进制
# %x 十六进制
# %e 科学计数法

age = 18
name = "tom"
weight = 75.5
stu_id = 1

print("my age is %d" % age)
print("my name is %s" % name)
print("my weight is %f" % weight)
print("my stu_id is %d" % stu_id)
print("my name is %s, age is %d" % (name, age))
print("my name is %s, age is %d ,weight is %f , stu_id is %d" % (name, age, weight, stu_id))
