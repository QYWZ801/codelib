# 遍历（for语句）
# 和C++不同，这里的for不是循环
# eg:
for i in [1,2,3,4,5,6]:
    # for和下面的代码采用正确的缩进，四个空格
    print(i)
for i in range(1,7):
         # 1-6
         # range是左闭右开
    print(i)

myList=["a","b","c"]
# 先写出列表
for eachName in myList:
    print(eachName)

for i in range(0,10,1):
    # 括号中步长可以不加，不加时默认为1
    # 0-9
# 1表示步长，表示每次跨越的长度
    print(i)

myList=["廖烜政","代好好","好朋友"]
for eachName in myList:
    print(eachName)