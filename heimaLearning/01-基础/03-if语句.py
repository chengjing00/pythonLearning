age = 18
if age >= 18:
    print("可是上网")

# input 接收输入的内容都为字符串
age = input("请输入您的年龄:")
age = int(age)
if age >= 18:
    print("可以上网")
else:
    print("age:%d 年龄不够，不可以上网" % age)
