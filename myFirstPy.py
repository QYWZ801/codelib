# print("hello world")
# print("hello")
# print("world")
# # print 打印
#
# # python可以用缩进来表示代码块，不需要使用大括号{}
# a=2
# if a==1:
#     print("这是第一种情况")
# else:
#     print("这是第二种情况")

# 数字有四种类型
# 整数：int
# 布尔型:bool
# 浮点型:float
# 复数：complex

# str字符串
# b="hello"
# print(b)

# print("请输入一个数")
# c=input()
# # 要用一个数去接受要输入的值
# d=int(c)
# # 把c变成一个整数
# print("您输入的数字是："+str(d))
# # +是指前后的拼接，前后的类型必须是一样的，前面是字符串
# print("你输入数字的平方是:"+str(d*d))
# # d是整数可以乘,最后将d*d变成字符串
#
# # +c就是相当于把c放入了这个双引号里面了


# 赋值运算，会辨别你是什么类型的变量，而不是默认为字符串
myInt001=15
myDouble001=2019.1026
myString001="World"
myBool001=False
print(myInt001)
print(myDouble001)
print(myString001)
print(myBool001)

myInt002=10
myDouble002=3.1415926
myString002="Hello"
myBool002=True
print(myInt002)
print(myDouble002)
print(myString002)
print(myBool002)

myInt003=myInt001+myInt002
print("结果是：",myInt003)
myDouble003=myDouble002-myDouble001
print("结果是：",myDouble003)
myInt003=myInt001*myInt002
print("结果是：",myInt003)
myInt003=myInt001 / myInt002
print("结果是：",myInt003)
myInt003=myInt001 % myInt002
print("结果是：",myInt003)
myInt003=myInt001**2
print("结果是：",myInt003)
myInt003+=myInt001
print("结果是：",myInt003)
myString003=myString001+myString002
print("结果是：",myString003)

myBool003=myDouble002>myDouble001
print(myBool003)
myBool003=myBool002 and myBool001
print(myBool003)
myBool003=myBool001 or myBool002
print(myBool003)
myBool003=not myBool002
print(myBool003)


# 数学计算函数

import math
# 提供了很多用于数学运算的函数和变量
# 比如：  数学函数math.sqrt(x)  math.sin(x)   math.log(x)
#        数学常量  math.pi圆周率  math.e表示自然常数e

import random
# 用于生成随机数和进行随机操作
# 生成随机浮点数   random.random()可生成一个介于0（包括）和1（不包括）之间的浮点数
# 生成指定范围内随机整数  random.randint(a,b)能生成一个介于a和b（包括a和b）之间的随机整数
# random.choice(sequence)可从给定的序列中随机选择一个元素


myDouble003=math.exp(1)
print(myDouble003)
myDouble003=math.pi
print(myDouble003)
myDouble003=math.sin(30*math.pi/180)
print(myDouble003)
myDouble003=abs(-13.25)
# 取绝对值
print(myDouble003)
myDouble003=max(myDouble001,myDouble002)
print(myDouble003)
myDouble003=random.random()
print(myDouble003)
myDouble003=random.random()*(100-10+1)+10
print(myDouble003)


myInt006=123
print(myInt006)
myString006="213"
print(myString006)
myInt005=int(myString006)
print(myInt005)
myString005=str(myInt006)
print(myString005)


myDouble006=321.321
print(myDouble006)
myInt005=int(myDouble006)
# 整形只保留整数部分
print(myInt005)



















