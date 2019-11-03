#三维曲面  三维贴面和三维线框
#from mpl_toolkits.mplot3d import axes3d  绘制3d图形
#ax.plot_wireframe(x, y, z, rstride=行距, cstride-列距,linewidth=线宽,color=颜色)

import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3,n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2) #结果是生成一个曲面

mp.figure('3d Wireframe')#三维线框
ax = mp.gca(projection='3d') #生成ax 3d对象
#在3d图里不能再使用mp画标签，mp是2d的。
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
ax.set_zlabel('z',fontsize=14)
mp.tick_params(labelsize=10)
ax.plot_wireframe(x, y, z, rstride=30,cstride=30,linewidth=0.5,color='orangered')

mp.show()








