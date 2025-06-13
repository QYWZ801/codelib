a=111
b=str(a)
#    \可以跳到下一行，使每行代码不用太长
print("保存之前先显示数据:"+ \
      b)
# 键盘上的tab键可以正常缩进

# 变量的命名规则
# Python采用大写字母，小写字母，数字，下划线和汉字等字符，但名字的首字符不能是数字
# 标识符中间不能出现空格，不能使用保留字（Python自带的，像False等）

import keyword
# 打印出Python中所有的保留字
print(keyword.kwlist)

# False和True表示逻辑判断词
print(1>2)

# delete删除
# d=1
# del d  d会消失
# # 会报错
# print(d)

e=[1,2,3]
print(e)
print(e[0])
print(e[2])
del(e[2])
print(e)


# not a #表示a的反
print(not(1>2))

# a and b #表示与操作



#import可以直接使用其他开发者写好的函数、类、变量等，无需自己实现
# 比如import math  引入标准库中的math模块， 后续可以直接使用math.sqrt()计算

import numpy
print(numpy.arange(0,10))
# 左闭右开

import numpy as np
print(np.arange(0,10,2))

from numpy import arange as v  #把arange表示成v函数
# 表示从numpy中借用v作为arange
print(v(0,10))

# 类似于C语言中的结构体
class MyCat():   #定义一个类
      # 定义类中的变量
      age=0
      name="miaomiao"

      # 定义类中的函数
      def shout(self):
            # 这个self代表了myCat00?的意思，写成其他的变量，如x,y等也可以
            print(self.name)
            print(self.age)
myCat001=MyCat()  #先定义一个变量来容纳这个类
myCat001.shout()  #函数运行

myCat002=MyCat()
# 先进行数据的初始化修改
myCat002.age=5
myCat002.name="huahua"
myCat002.shout()

myCat003=MyCat()
# 先进行数据的初始化修改
myCat003.age=5
myCat003.name="huahua"
myCat003.shout()

print(myCat002.age==myCat003.age)
print(myCat002.name==myCat003.name)
print(myCat002.age is myCat003.age)
print(myCat002==myCat003)  #尽管数值相同，但是这两个变量是两个独立的个体，不等同
# ==是比较两个对象的值是否相等，只要包含的元素顺序和值都相同，用==就会返回Ture
print(myCat003 is myCat002)
# is是用于判断两个对象是否为同一个对象，就是比较它们在内存中的地址是否相同

# 条件分支语句
a=11
if a>20:
      print(1)
elif a>10:
      print(2)
else:
      print(3)

# for遍历
for i in range(0,6):
      # 左开右闭
      print(i)

# while循环
i=0
while i<6:
      if i==3:
            i=i+1
            continue
      print(i)
      i+=1

for i in range(0,6):
      if i==3:
            continue #跳过这次遍历
      print(i)

for i in range(0,6):
      if i==3:
            break #剩下的也不会遍历，完全终止
      print(i)


def myFunction(a,b):
      if a>b:
            print(a)
      else:
            print(b)
myFunction(3,5)

def myFunction():
      pass #pass是占位符，没有返回值
print(myFunction())

g=lambda x:x+1
# x表示送进去一个值， ：后面的x+1表示返回的值
print(g(2))

try:
      print(1/1)
except Exception as e:
      print(e)
else:
      print("没有错误")
finally:
      pass


try:
      print(1/0)
except Exception as e:
      print(e)
else:
      print("没有错误")
finally:
      pass


try:
      print(1/0)
except:
      # print("除数不能为0")
      # raise Exception("myError")
      pass
else:
      print("没有错误")
finally:
      pass

# assert后面的语句正确，就执行下面的语句；如果后面的语句不正确，就会报错

assert 5>3
print(1)
print(2)

# assert 1>3
# print(1)
# print(2)

# yield可以将函数转化成生成器

# async和await用于异步编程
# async表示多个程序同时进行
# await作用是挂起协程的执行，等待某个异步操作的完成，await后面必须跟一个可等待对象

import asyncio   #表示引入多线执行的包
async def do1():
      # async函数表示自己执行的时候，别人也可以执行
      await asyncio.sleep(1)

      print("3秒过去了")
async def do2():
      await asyncio.sleep(1)
      print("1秒过去了")
async def do3():
      await asyncio.sleep(2)
      print("2秒过去了")

async def main():
# 不要忘记python中的缩进
# 创建任务
      task1 = asyncio.create_task(do1())
      task2 = asyncio.create_task(do2())
      task3 = asyncio.create_task(do3())
# 将任务放入列表
      tasks=[task1,task2,task3]
#等待所有任务完成
      await asyncio.wait(tasks)

if __name__=="__main__":
      asyncio.run(main())













































