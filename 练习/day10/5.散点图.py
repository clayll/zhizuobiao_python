#散点图
#可以让一个点附带更多信息
#它总是用两个坐标x,y坐标表示

#np.random.normal() #正态分布规律的随机数
#np.random.normal(0,        1,      n)
#                 平均值   标准差 n个
#最后会以数组形式返回
import numpy as np
import matplotlib.pyplot as mp

n = 1000 #生成1000个随机数
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
d = np.sqrt(x**2 + y**2) #距离正下方的点
mp.figure('Scatter',facecolor='lightgray')
mp.title('Scatter',fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)    #标签文字的字体
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c=d, cmap='jet_r',alpha=0.5,marker='+')
#c=d代表用距离做颜色，cmap颜色映射，让颜色和距离对应起来
#'jet_r'对应深红，最大值对应深蓝
mp.show()

