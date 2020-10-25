# -*- coding: utf-8 -*-
# @Time    : 2020-10-24 17:09
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 09-条件语句.py
# @Software: PyCharm
# if -- else

isTrue = False
if isTrue:
    print("true")
else:
    print("false")

# if-elif-else
age = 80
if age < 18:
    print("age < 18")
# elif (age >= 18) and (age <= 60):
elif 18 <= age <= 60:
    print("18 <= age <= 60")
elif age > 60:
    print("age > 60")
