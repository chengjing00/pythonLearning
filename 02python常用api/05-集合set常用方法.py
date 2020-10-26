# -*- coding: utf-8 -*-
# @Time    : 2020-10-26 11:08
# @Author  : chengj-f
# @Email   : chengj-f@glodon.com
# @File    : 05-集合set常用方法.py
# @Software: PyCharm

# Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算


# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))

# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)

# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 向集合添加元素和从集合删除元素。
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)

print("集合的交集、并集、差集、对称差运算")
print(f"set1:{set1}")
print(f"set2:{set2}")
# 集合的交集、并集、差集、对称差运算

# 交集
print(f"交集:{set1 & set2}")
# print(set1.intersection(set2))

# 并集
print(f"并集:{set1 | set2}")
# print(set1.union(set2))

# 差集
print(f"差集:{set1 - set2}")
# print(set1.difference(set2))

# 对称差集
print(f"对称差集:{set1 ^ set2}")
# print(set1.symmetric_difference(set2))

# 判断子集和超集
# 子集
print(f"子集:{set2 <= set1}")
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))


