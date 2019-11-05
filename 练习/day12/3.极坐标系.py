#极坐标系
#mp.gca(projection='polar')
#mp.plot()
#mp.scatter()
#x轴对应是极角
#y轴对应是极径

import numpy as np
import matplotlib.pyplot as mp

t = np.linspace(0, 2 * np.pi, 1001) #线性等分 0,2pi 一圈
r_spiral = 0.8 * t  #螺旋线的公式
r_rose = 5 * np.sin(6 * t)     #玫瑰线 六元回归线，6瓣
mp.figure('Polar',facecolor='lightgray')
mp.gca(projection = 'polar')
mp.title('Polar',fontsize=20)
mp.xlabel(r'$\theta$',fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

mp.plot(t, r_spiral,c='dodgerblue',label=r'$\rho=0.8\theta$')
mp.plot(t, r_rose,c='orangered',label=r'$\rho=5sin(6\theta)$')

mp.legend()
mp.show()