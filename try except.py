# 异常检验 （try except）

# try:
    # 主体程序
    # 发生异常时，程序终止，跳转到
# except Exception as e:
#     异常处理程序
# else
# 程序没问题的时候执行的代码块

# eg:
try:
    print(1/0)
except Exception as e:
    print(e)
else:
    print("no exception")


# eg:0
try:
    print(1/1)
    # 如果可以运行，这个也可以打印
except Exception as e:
    # 可以将错误放进e中
    # e是具体报错原因
    print(e)
else:
    print("no exception")


try:
    print(1/0)
except ZeroDivisionError as e:
    print("exception happen")
    print(e)
else:
    print("try success")
finally:
    # 无论try块中的代码是否发生异常，也无论except块是否捕获并处理异常，
    # finally中的代码都会在最后执行，避免资源泄露
    # finally可以确保文件在使用后会被关闭
    pass
# pass是占位符，可以保证finally块的完整







