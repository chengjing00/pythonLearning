# -*- coding: utf-8 -*-
# @Time    : 2020-10-26 10:57
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 04-元组tuple.py
# @Software: PyCharm
"""
Python中的元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，
不同之处在于元组的元素不能修改，在前面的代码中我们已经不止一次使用过元组了。
"""
# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(t)

# 获取元组中的元素
print(t[0])
print(t[3])

# 遍历元组中的值
for member in t:
    print(member)

# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)

# 将元组转换成列表
person = list(t)
print(person)

# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)

# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)