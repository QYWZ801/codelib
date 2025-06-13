# 函数 （function定义与调用）

# 函数的定义

# def 函数名（参数名1，参数名2，……）
#     函数体
#      return的返回值

# 函数的调用

# 变量（接收返回值）=函数名（参数1，参数2）

def max(a,b):
    if a>b:
        print(a)
        return a
    # return可以起到避免后续运行的作用
    # 还可以将一个值返回给调用函数的地方
    # 如果没有return，会默认返回空值None
    else:
        print(b)
        return b

myMax=max(12,13)
print(myMax)


def myMax(a,b):
    if a>b:
        print("A is bigger")
        return a
    elif a==b:
        print("B is equal to A")
        return b
    else:
        print("B is bigger")
        return b

max=myMax(12,13)
print(max)
















