#半对数坐标
#mp.semilogy(y,'o-',c='orangered',label='semilogy')



import numpy as np
import matplotlib.pyplot as mp
y = np.array([1, 10, 100, 1000, 100, 10, 1])
mp.figure('Normal & Log')
mp.subplot(211)
mp.title('Normal',fontsize=16)
mp.ylabel('y',fontsize=12)
ax = mp.gca()
#多点定位器,刻度间隔为1
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))

mp.tick_params(labelsize=10)

#沿着主刻度画标线
mp.grid(which='major',axis='both',linewidth=0.75, linestyle='-',color='lightgray')
mp.grid(which='minor',axis='both',linewidth=0.25, linestyle='-',color='lightgray')
mp.plot(y,'o-',c='dodgerblue',label='plot')
mp.legend()

mp.subplot(212)
mp.title('Log',fontsize=16)
mp.xlabel('x',fontsize=12)
mp.ylabel('y',fontsize=12)
ax = mp.gca()
#多点定位器,刻度间隔为1
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))

mp.tick_params(labelsize=10)

#沿着主刻度画标线
mp.grid(which='major',axis='both',linewidth=0.75, linestyle='-',color='lightgray')
mp.grid(which='minor',axis='both',linewidth=0.25, linestyle='-',color='lightgray')

mp.semilogy(y,'o-',c='orangered',label='semilogy')
mp.legend()

mp.tight_layout()
mp.show()


