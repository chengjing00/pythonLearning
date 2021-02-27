age = 18
if age >= 18:
    print("可是上网")

# input 接收输入的内容都为字符串
age = input("请输入您的年龄:")
# 将字符串类型转为 int 类型
age = int(age)

# 多重判断
if age >= 18 and 1 == 1:
    print("可以上网")
elif age <= 60:
    print("可以上网")
else:
    print("age:%d 年龄不够，不可以上网" % age)

# if 化简写法
if 18 <= age <= 60:
    print(f"age {age}")
