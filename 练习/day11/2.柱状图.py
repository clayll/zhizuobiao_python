#柱状图
#mp.bar(水平坐标数组,高度数组,ec=边缘颜色,fc=填充颜色,label=标签文本,alpha=透明度)

#numpy.random.normal() 正态分布相关随机数

#numpy.random.uniform()
#例子:np.random.uniform(0.5, 1.0, n)  取从0.5到1.0内产生的n个随机数

import numpy as np
import matplotlib.pyplot as mp

n = 12

x = np.arange(n)#生成整数数组
y1 = (1 - x / n) * np.random.uniform(0.5, 1.0,n)
y2 = (1 - x / n) * np.random.uniform(0.5, 1.0,n)

mp.figure('Bar',facecolor='lightgray')
mp.title('Bar',fontsize=20)
mp.ylim(-1.25, 1.25)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.xticks(x, x + 1)  #12个数字
mp.tick_params(labelsize=10)
mp.grid(axis='y',linestyle = ':') #axis='y' 只有水平的网格线

for _x, _y in zip(x, y1):
    #取矩形条的位置和高度
    mp.text(_x, _y, '%.2f'%_y,ha='center',va='bottom')#显示文字
    #%.2f两位小数精度的浮点数来表示格式占位符 ；va='bottom' 块在水平底下

for _x, _y in zip(x, y2):
    # 取矩形条的位置和高度
    mp.text(_x, -_y, '-%.2f'%_y,ha='center',va='top')


mp.bar(x, y1, ec='white',fc='dodgerblue',label='Sample 1')
mp.bar(x, -y2, ec='white',fc='dodgerblue',label='Sample 2',alpha=0.5)

mp.legend()
mp.show()

