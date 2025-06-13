# 1.回归算法
# 一元一阶线性回归

import numpy as np
t=np.arange(1,10,1)  #设置时间链
print(t)

y=0.9*t+np.sin(t)
#sin表示引入一个波动的数组
# 0.9*t体现线性增长趋势，np.sin(t)表示波动变化
print(y)

import matplotlib.pyplot as plt

plt.plot(t,y,"o")
# t为横轴，y为纵轴
# o表示小圆点，-表示实线，--表示虚线
# 表示不同颜色就加上颜色的首字母   特殊的，蓝色是r，黑色是k
# plt.show()
plt.plot(t,y,"r--")
# plt.show()
plt.plot(t,y,"-")
# plt.show()

model=np.polyfit(t,y,deg=2)
# deg=1表示进行一次多项式拟合，也就是线性拟合，返回的是斜率和截距
# deg=n表示的是进行n次多项式拟合，返回的依次是系数和常数项

print(model)


t2=np.arange(-2,12,0.5)
print(t2)

y2predict=np.polyval(model,t2)
# polyval可以计算出预测值，即已知方程和横坐标，求纵坐标



print(y2predict)

plt.plot(t,y,"o",t2,y2predict,'x')
plt.show()





# 2.分类算法(既有特征值又有标签值，就是分类已知)
# K最近邻(kNN,k-NearestNeighbor)
# 离自己最近的K个数决定分类

# 3.聚类算法（不知道分类）


# 4.推荐算法
# 基于用户的协同过滤(根据项目找相似用户)
# 基于项目的协同过滤(根据用户找相似项目)



# 5.降维算法





























































































































