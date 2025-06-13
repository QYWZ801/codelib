# Pandas中的数据结构，包括Series和DataFrame
# 序列Series

# 创建Series
# 引入pandas包并取别名pd
import pandas as pd

# 创建序列对象。首先建立一个字典，使用Series()方法将字典转换成序列对象
# 字典的key会自动变成series的index(索引)
# 若转换列表，则生产的序列对象会自动赋予index值,会自动在前面弄上序号
sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
s0=pd.Series(sdata)
print(s0)
print(type(s0))
s1=pd.Series([6,1,2,9])
print(s1)

# 添加索引。通过指定index为series增加索引
s1=pd.Series([6,1,2,9],index=['a','b','c','d'])
print(s1)


# Series查询操作
# values显示series中的值，index显示索引，此外还可以按照索引值显示元素

# 序列的值
print(s0.values)

# 序列的索引
print(s0.index)

# 按照下标查找序列的值
print(s0.iloc[2])

# 按照索引值查找索引的值
print(s0['Utah'])

# 按照下标批量查找序列
print(s0[:2])
# 默认起始为0，这就是第
# s0[start:stop] 不包括右边的边界

# 按照索引值批量查找元素
print(s0[['Ohio','Oregon']])

# Series增加操作
# append()方法为series增加元素，index可以指定序列值
# 新版本删除了append()为series增加元素的操作，而是用concat()

newSeries=pd.Series([12],index=['e'])
s2=pd.concat([s1,newSeries])
# 要在括号中加上中括号
print(s2)

# Series删除操作
# 删除series中的元素（只能通过index来删除元素）
s3=s1.drop('a')
print(s3)

# Series的修改操作
s1['a']=4
print(s1)

# Series特殊操作
# 序列排序  sort_values()方法可以使series的值按照升序排序
print(s1.sort_values())

# 序列求中位数。median()方法可以直接得到序列的中位数，在此之上可以进行比较等操作
print(s1)
print(s1.median())
print(s1[s1>s1.median()])
# 把大于中位数的找出来


# 序列的运算。两个series之间的运算，可加减乘除（必须保证index是一致的）
s2=pd.Series([4,3,5,8],index=['a','b','c','d'])
print(s2+s1)

# 时间序列。pandas包中的data_range()方法可以生产时间序列，便于进行数据的处理
s3=pd.Series([100,150,200])
print(s3)
idx=pd.date_range(start='2019-9',freq='M',periods=3)
                        # 'M'表示以每个月的月末为时间点
s3.index=idx
print(s3)


# Series转换为其他数据结构示例

dfFromSeries=s2.to_frame()
print(dfFromSeries)
print(type(dfFromSeries))

dictFromSeries=s2.to_dict()
# 转换成字典
print(dictFromSeries)
print(type(dictFromSeries))



# 数据框DataFrame

# 创建DataFrame
# 引入pandas包，创建DataFrame对象。
# 首先创建字典
# 之后使用DataFrame()方法创建数据框对象
# 通过index.name给索引命名
# 最后使用to_csv和to_excl方法将其保存为csv和excl文件

import pandas as pd

dic1={'name':['Tom','Lily','Cindy','Petter'],'no':['001','002','003','004'],'age':[16,16,15,16],'gender':['m','f','f','m']}
df1=pd.DataFrame(dic1)
print(type(df1))
df1.index.name='id'
df1.to_csv('students.csv')
df1.to_excel('students.xlsx')
print(df1)

dict2={'name':['liaoming','xiaohong','xiaowang','xiaoli'],'score':[100,34,27,99],'IQ':[120,111,109,102]}
df2=pd.DataFrame(dict2)
df2.index.name='id'
df2.to_csv('students.csv')
df2.to_excel('students.xlsx')
print(df2)

# DataFrame查询操作
# 通过DataFrame.name可以返回索引值为name的整列数据，
# 而DataFrame.iloc[i]可以返回指定行数的全部数据。
column=df1.no
row=df1.loc[3]
print(row)

# DataFrame增加操作
# 使用append()方法增加一名同学的信息，这里根据行索引分别添加值,新版本不存在
# 使用concat
# update()方法可以给数据框增加列
print(df1)
new_data = pd.DataFrame([{'name': 'Stark', 'no': '005', 'age': 15, 'gender':'m'}])
df3 = pd.concat([df1, new_data], ignore_index=True)
print(df3)
df3['new_Col']=[1,2,3,4,5]
print(df3)

# DataFrame删除操作
# 使用drop方法删除'address'列，还可以通过修改参数删除行
# 通过del指令可以删除指定索引值的整列数据
df4=df3.copy()
print(df4)
df4b=df4.drop(['name'],axis=1)
# 删除列
print(df4b)

df4c=df4.drop([2])
# 删除行
print(df4c)


# DataFrame修改操作

# 数据按列合并
df5=pd.DataFrame({'address':['school','home','school','school','home']})
df6=pd.concat([df3, df5], axis=1)
print(df6)

# 数据按行合并
df7=pd.DataFrame({'name':['Tony'],'no':['005'],'age':[16],'gender':['m']})
df8=pd.concat([df1, df7], axis=0, ignore_index=True)
                                       # ignore_index=True可以使增加的那一行id自动调号
print(df8)


# DataFrame特殊操作
# 通过date_range函数生成序列并加入数据中，列如创建从2019年9月21日开始的连续4天的时间序列。
# 使用pandas包中的read_csv()方法读取之前保存的学生数据
# 更新数据后会发现生成的时间序列已经加入到数据框中
i1=pd.date_range('2019/9/21',periods=4,freq='7D')
df10=pd.read_csv('students.csv')
df10.index=i1
print(df10)

# 时间序列查询
print(df10.loc["2019-09-21":"2019-09-30",['gender','age','name']])

# DataFrame转换成其他数据结构



























