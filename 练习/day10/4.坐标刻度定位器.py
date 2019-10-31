#定位器对象 = mp.XXXLocator(...)

import numpy as np
import matplotlib.pyplot as mp

mp.figure()

#定位器:

locators = [
    'mp.NullLocator()',#空定位器
    'mp.MaxNLocator(nbins=3,steps=[1, 3, 5, 7, 9])',#最多分三段，从列表里选一个等分的点
    'mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])',#固定定位器
    'mp.AutoLocator()',#自动定位器
    'mp.IndexLocator(offset=0.5,base=1.5)',#索引定位器
    'mp.MultipleLocator()',#次刻度定位器
    'mp.LinearLocator(numticks=21)', #线性均分定位器 21就是分成20份
    'mp.LogLocator(base=2,subs=[1.0])'] #指数定位器，base=2:2为底,subs=[1.0]:指数增长量1.0

n_locators = len(locators)

for i,locator in enumerate(locators):
    mp.subplot(n_locators,1, i+1)
    mp.xlim(0,10)
    mp.ylim(-1,1)
    mp.yticks(())
    mp.xticks(())
    ax = mp.gca()
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data',0)) #底轴放中间。因为1到-1 中间是0，所以放0
    ax.xaxis.set_major_locator(eval(locator))
    #eval函数解释执行，产生类的对象：主刻度执行器
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1)) #次刻度定位 ,0.1为间隔

    mp.plot(np.arange(11),np.zeros(11),c='none') #zeros全部为零 y坐标全为0
    mp.text(5, 0.3, locator[3:],ha='center',size=12)


mp.show()