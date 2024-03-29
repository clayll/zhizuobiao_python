#区域填充
#mp.fill_between(水平坐标数组，垂直坐标起点数组，垂直坐标终点数组，条件判断，color=颜色,alpha=透明度)

import numpy as np
import matplotlib.pyplot as mp

n = 1000
x = np.linspace(0, 8 * np.pi, n)#线性分割
sin_y = np.sin(x)
cos_y = np.cos(x / 2) / 2   #周期短频率更高

mp.figure('Fill',facecolor='lightgray')
mp.title('Fill',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(':')
mp.plot(x,sin_y,c='dodgerblue',label=r'$y=sin(x)$')
mp.plot(x,cos_y,c='orangered',label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')
mp.fill_between(x, cos_y, sin_y,cos_y < sin_y,color='dodgerblue',alpha=0.5)
mp.fill_between(x, cos_y, sin_y,cos_y > sin_y,color='orangered',alpha=0.5)
mp.legend(loc=('upper right'))
mp.show()
