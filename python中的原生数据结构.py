# 8种经典的数据结构
# 分为三大类：
# 1.python原生数据结构：
# （不用·引入包）
# 元组Tuple()
# 列表List[]
# 集合Set{}
# 字典Dictionary{A:B} 键和值

# 2.NumPy包中的数据结构：
# 数组Ndarray(带多种操作)，
# 矩阵Matrix(多种线性代数计算)

# 3.Pandas包中的数据结构：
# 序列Series(索引+1列数据)
# 数据框DataFrame(索引+多列数据表)


# 元组的查询和列表是相通的

# 元组一旦创建就无法对齐元素进行增加、删除和修改(可以全部整体删除)
# 可以用（）创建元组，元组可以为空且元素类型可以不同。但是元组中仅包含一个数时，应该添加空格，如tup2
# 都好以区别运算符号。也将列表对象转换为元组对象，使用tuple（）函数可以根据原对象生成一个新的元组对象
tup1=('Google','Runoob',1997,2000)
print(tup1)
tup2=(1,)
print(tup2)
tup3="a","b","c","d"
print(tup3)
# 打印的结果的形式和tup1是类似的
tup4=()
print(tup4)

# 转换前seq的类型是class list
# 转换后tup的类型是class tuple
seq=['a','b','c','d']
print(seq)
# 转换前后，打印形式不一样，一个是方括号，一个是圆括号
tup=tuple(seq)
print(tup)

# Tuple可以连接和复制
tup4=tup1+tup2
print(tup4)
# ('Google','Runoob',1997,2000,1)
tup5=tup2*3
print(tup5)
# 此时tup5中不是一个数，不用考虑空格了
# (1,1,1)

# Tuple的查询
print(tup1[0])
# (索引编号从0开始)
# Google
print(tup4[1:5])
# 如果超出了元素个数，就是能访问多少就访问多少
# 方括号索引左闭右开，第二个元素到第5个元素
print(tup1[-1])
# 从后往前数第1个
print(tup1[-2:])
# 从倒数第二个数一直到最后一个数
print(tup1[::2])


# 在python中，这些像len(),max()等函数可以直接使用
print(len(tup1))
print(max(tup2))
print(min(tup2))

# tuple可以转化成其他数据类型
print(list(tup1))
# 列表型
print(tup1.__str__())
# 字符串型


# 列表  可以随时添加和删除列表中的元素
students=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(students)
empty=[]
print(empty)
lists=[[1,2],['a','b']]
print(lists)
# 多维列表


# List查询
print(students[1:8])
# (list[a:b]返回一个含有列表中第a+1个至第b个元素的列表对象)
# 编号从0开始，切片左闭右开!!!
# [2,3,4,5,6,7,8]

print(students[::2])
# (list[::a]返回一个从列表第一个元素起始，步长为a的列表对象)
# [1,3,5,7,9,11,13,14]

print(students[-3])
# 从后往前访问
# 13
print(students[2::2])
# 从下标为2的数开始，步长为2
print(students[::-1])
# 从最后一个数开始，倒着向前遍历


# List增加操作
# append()可以在列表末尾增加新的项目，可以增加一个元素，也可以增加一个list对象而成为多维列表
# append的返回值是None，它会直接改变students的值，所以不能直接打印appent，而是要先操作，在打印操作之后列表
students.append(11)
print(students)
# [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,11]
lists.append(['hello',5])
print(lists)
# [[1,2],['a','b'],['hello',5]]


# List删除操作
# remove()可以删除指定的元素，若不存在就报错，pop()可以删除指定下标的元素，默认为列表对象的最后一个元素
# list.pop(i)将删除下标为i的元组
# pop如果直接打印，打印的结果是它所要移除的元组，先操作再打印则是打印移除过后的原列表
students.remove(5)
print(students)
# [1,2,3,4,6,7,8,9,10,11,12,13,14,15]
students.pop(5)
print(students)
lists.pop()
print(lists)
# [[1,2],['a','b']]

# List修改操作
# list[i]=x可以直接替换列表指定下标的元素
students[0]=100
print(students)

# List的特殊操作
# reverse()可以使列表倒置，len()可以返回列表的元素个数，sort()可以使列表元素升序排列
students.reverse()
print(students)
# [11,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
students.sort()
print(students)
# [1,2,3,4,5,6,7,8,9,10,11,11,12,13,14,15]
students.sort(reverse=True)
# 降序
print(students)
# [15,14,13,12,11,11,10,9,8,7,6,5,4,3,2,1,]

# List转换成其他数据结构
print(tuple(students))
# 直接对整体打印，不要对改过的打印
print(str(students))



# 集合Set

# 集合不会出现重复值，所有的元素按一定的顺序排列，若元素为数字则按照数字大小排列
# 使用set()函数创建集合会自动拆分多个字母组成的字符串,set()最多只能输入一个元素，如果要放入几个元素，就要写成set[]
mySet=set('abcgefa12312123')
print(mySet)
# {'1','2','3','a','b','c','g','e','f'}
myset1=set('大小点多')
print(myset1)
myset2=set(['大','小','点','多'])
# 把列表弄成集合
print(myset2)
# {'多','大','点','小'}
myset3=set(('Hello','World'))
# 将元组弄成集合
print(myset3)
# {'Hello','World'}

# Set查询操作
# 集合的查询，使用in可以判断a是否在集合中,直接打印,存在为真，反之为假
mySet={'a','b','c','d','e','f'}
print('a' in mySet)
# True

# Set增加操作
# add()函数可以在集合对象中加入新元素，但若是元素已经存在了，则无效果
# 使用update表示添加（并非修改）是一个一个添加（即可以把字符串分开），并且按照顺序添加进集合

mySet.add('ghk')
print(mySet)
# {'a','b','c','d','e','f','ghk'}
mySet.update('tyu')
print(mySet)
# {'a','b','c','d','e','f','u','y','ghk','t'}

# Set删除操作
# remove()可以将集合中的元素删除，如果不存在会抛出KeyError 异常。
# discard()可以删除集合中指定元素，且元素若不存在不报错
# pop可以随机删除集合中的一个元素（在交叉模式中删除最后一个元素）
# clear()函数可以清空集合

mySet.remove('a')
print(mySet)
# {'b','c','d','e','f','u','y','ghk','t'}
mySet.discard('z')
print(mySet)
# mySet.discard('x') 删除不存在的元素，不会报错
# {'b','c','d','e','f','u','y','ghk','t'}
mySet.pop()
print(mySet)
# {'b','c','d','e','f','u','ghk','t'}
mySet.clear()
print(mySet)
# set()

# Set特殊操作
# len()查询集合的长度
# copy()可以复制集合中的元素并生成一个新的集合
print(len(mySet))



# 集合的运算。首先建立两个新的集合用于计算。
# '-'表示求差集
# '&'表示求交集
# |表示求并集
# ^表示两个集合的并集减去交集

a=set('apple')
b=set('banana')
print(a-b)
print(a&b)
print(a|b)
print(a^b)



# 字典Dict
# 字典的创建。生成一个字典和一个包含三个字典对象的字典列表
# （列表中嵌套字典，studets实际是一个列表，students中的元素是字典）

dict1={"ID":"L100","Name":"COCO"}
        # 字典由键名和键值构成  ID:L100     Name:COCO
students=[{'name':'n1','id':'001'},{'name':'n2','id':'002'},{'name':'n3','id':'003'}]
print(type(dict1))
print(dict1)
print(students)


# 使用zip方法创建字典。zip()方法可以组成元组组成的列表
mydict=dict(zip('abcde','12345'))
# 如果前后数量不对应，从第一个向后面匹配，直到数量最少弄完的
print(mydict)


# Dict查询操作
# 查找第一个字典元素id键的值，此外还可以用get(key,default=None)方法获取指定键的值
print(students[0]['id'])
print(students[0].get('id'))

# Dict增加操作
# 字典的增添。
# 添加一名学生的信息（增加行，其实是增加列表中的一个元素），之后再添加一个学生信息科目（增加列，其实是增加字典中一个键值对）
students.append({'name':'n4','id':'004'})
print(students)
students[0]['school']='school1'
students[1]['school']='school2'
students[2]['school']='school3'
print(students)

# Dict删除操作
# 字典的删除。使用del删除一名学生的信息（删除行，其实是删除列表中的一个元素）
# 再使用pop删除第一个学生的学号(删除某一行中的列，其实是删除字典中的一个键值对)
del students[3]
print(students)
students[0].pop('id')
# 删除第一个元素的id列
print(students)

# 删除所有学生的学号（删除某一列，其实就是删除所有字典中的一个键值对）
# 用for循环遍历
for i in range(0,len(students)):
    students[i].pop('school')
    print(students)

# Dict转换成其他数据结构示例
























































