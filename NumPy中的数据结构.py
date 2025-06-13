# NumPy 数学计算包

# 创建Ndarray
# 引入NumPy包，将其命名为np。在引入NumPy包后方可使用数组结构类型
import numpy as np

# 创建数组对象。在NumPy包中，使用array()方法可以把序列对象转换成数组
# arange()方法可以生成自定义终点的一维数组,起点默认为0
# ones()生成值全为1的数组
# empty()方法会生成一个给定类型和维度且不进行数据初始化的数组
# random()生成随
# 机数组
# linspace()生成指定起始数值和步长的一维数组，例如生成一个从1到10的元素个数为5的数组

import numpy as np

array001=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# 将列表转化成数组
print(array001)
a2=np.arange(5)
# 以0为起始，1为步长，共5个元素
print(a2)
a3=np.ones((2,2))
# 形状为二行二列的数组，其中元素全为1
print(a3)
a4=np.empty((2,2))
# 未初始化，即存储好的元素，不一定是0或1
print(a4)
# random.rand和random.random都可以达到类似生成随机数数组的目的，只是调用形式上略有不同
a5=np.random.rand(4,2)
print(a5)
# 随机生成0到1的数
a6=np.random.random((4, 2))
print(a6)
a7=np.linspace(10,30,5)
                # 起始    终止      步长
print(a7)

# Ndarray的查询操作
# 数组的查询，数组可以通过array[a:b]从数组中提取子集，也可以进行批量赋值操作
array002=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#
print(array001[4:])
print(array002[1:3,2:4])
               # 行   列  2,3行，3,4列
# 二行三四列，三行三四列

# shape可以返回对象的数据结构，例如行数和列数，除了返回一个表示数组各维度的元组，也可以通过reshape改变数组的结构
array004=array001.reshape(3,-1)
# 3表式新数组想要设置的行数，-1是一个特殊标记，表示让NumPy自动计算该维度的大小
print(array004)


# Ndarray增加操作
# append()可以增加元素或者列表类型的数据，但必须注意唯独需要保持一致
array003=np.append(array002,[[1],[2],[3]],axis=1)
# axis=1表示按列方向添加，这里默认加到最后一列
# 如果想添加行，就是axis=0
print(array003)


# 数组的删除
# 数组的删除，使用delete(x,i,axis=)方法可以删除数组对象中行或者列
# 第三个参数axis决定了删除的是行还是列，需要删除的对象可以是一个数，也可以使一个元组进行批量删除
array003=array002.T
# .表示对数组进行转置
print(np.delete(array003,1,axis=0))
# 第二行
print(np.delete(array003,(1,3),0))
# 删除第二行和第四行，这个表示第几行和第几行，不是表示第几行到第几行
# 批量删除
print(np.delete(array003,1,1))
# 表示删除第二列

# Ndarray的修改
# 数组的修改。可以使用索引的方式进行数组数据的批量修改
array002[1:2]=0
# 第2行到第二行，也就是第二行修改为0
print(array002)
array003=array002.T
array003[1][1]=100
# 第二行第二列变成100
print(array003)

# Ndarray的特殊操作
# 二维数组的转置。array.T可以得到数组对象的转置后的结果

# 数组的堆叠
# 首先引入两个数组，之后一次
#使用vstack进行纵向堆叠和  就是表示增加行数
#使用hstack进行横向堆叠    就是表示增加行的长度
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.vstack((arr1,arr2)))
# [[1 2 3]
 # [4 5 6]]
print(np.hstack((arr1,arr2)))
# [1 2 3 4 5 6]

# Ndarray转换成其他数据结构
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3)
import pandas as pd
# pandas会打印行号和列号
dfFromNdarray=pd.DataFrame(arr3)
print(dfFromNdarray)


# Matrix矩阵

# 创建Matrix
# 外部包：引入NumPy包，将其命名为np，在引入NumPy包后方可使用数据结构
import numpy as np

# 矩阵的创建。使用mat()方法可以把其他数据结构的对象转换成矩阵类型
array1=[1,2,3]
array2=[6,7,8]
array3=[11,12,17]
matrix=np.mat([array1,array2,array3])
print(type(matrix))
print(matrix)

# 创建随机矩阵。在numpy中包含许多创建特殊矩阵的方法。这里使用empty()方法创建一个新的数据随机的矩阵
matrix1=np.empty((3,3))
# 创建一个全空矩阵，哪怕有数，也非常非常小，趋近于0
print(matrix1)

# Matrix查询操作
# 矩阵查询。

# 矩阵每维的大小,就是打印(行数，列数)
print(matrix.shape)

# 矩阵所有数据的个数
print(matrix.size)

# 矩阵每个数据的类型
print(matrix.dtype)


# Matrix增加操作
# 矩阵合并
# c_[]方法进行行连接，r_[]方法用于列连接

mat1=np.mat([[1,2],[3,4]])
# 要放一个列表，不要忘了两个中括号外面加上一个中括号

mat2=np.mat([4,5])
matrix_r=np.c_[mat1,mat2.T]
# 括号的顺序决定了排列顺序

print(matrix_r)
matrix_l=np.c_[mat2.T,mat1]
print(matrix_l)
matrix_u=np.r_[np.mat([array1]),matrix]
print(matrix_u)

# Matrix删除操作
# 矩阵删除。delete()方法可删除矩阵的指定行列
matrix2=np.delete(matrix,1,axis=1)
print(matrix2)
matrix3=np.delete(matrix,1,axis=0)
print(matrix3)


# Matrix特殊操作
# 矩阵运算，
# *被重写用于矩阵乘法，要求两个矩阵的形状完全相同
# .dot()则用于计算矩阵的点乘，要求前面矩阵的列数等于后面矩阵的行数
mat3=np.mat([[5,6],[7,8]])
matrix4=mat1*mat3
print(matrix4)
matrix5=mat1.dot(mat3)
print(matrix5)


# 矩阵常用函数。矩阵也可以使用.T进行转置。
# linalg.inv可以用于求逆矩阵，但不存在逆矩阵会报错
matrix6=matrix.T
print(matrix6)
matrix7=np.linalg.inv(mat1)
print(matrix7)

# 求矩阵的特征值（使用的numpy必须是方阵）
# linalg.eig()
matrix8=np.linalg.eig(matrix)
print(matrix8)

# Matrix转换成其他数据结构
print(matrix.tolist())

print(np.array(matrix))









