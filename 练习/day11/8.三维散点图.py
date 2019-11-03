#三维散点
#ax.scatter(x,y,z, s=大小, c=颜色, marker=点型)
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000 #生成1000个随机数
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
d = np.sqrt(x**2 + y**2) #距离正下方的点
mp.figure('Scatter3D')
ax = mp.gca(projection='3d')
mp.title('Scatter3D',fontsize=20)
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
ax.set_zlabel('z',fontsize=14)
mp.tick_params(labelsize=10)

ax.scatter(x, y, z, s=60,c=d, cmap='jet_r',alpha=0.5)
#c=d 用距离来做颜色
#cmap颜色映射
#颜色和距离就对应起来了。
#jet_r: 0对应深红,最大值对应深蓝, marker='*',五角星：*, 方块 s,菱形 :D
mp.show()


