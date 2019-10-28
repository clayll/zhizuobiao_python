import numpy as np
import matplotlib.pyplot as mp

#数据可视化 matplotlib  (mat-math数学，plot-绘画,lib-library库)
#基本绘图的库

#数据可视化: matplotlib.pyplot (mp)
#1. 基本绘图函数
#1.1  mp.plot(水平坐标数组，垂直坐标数组)
# x:[1 2 3 4]
# y:[5 6 7 8]

#mp.plot(...,linestyle=线型,linewidth=线宽(线宽默认为2),color=颜色)


#1.2 画边界
#mp.xlim(左边界，有边界)
#mp.ylim(底边界，顶边界)


#1.3 画刻度
#mp.xticks(刻度位置数组,刻度文本数组)   #水平方向
#mp.yticks(刻度位置数组,刻度文本数组)   #垂直方向

#1.4画坐标轴
#ax = mp.gca() #获取当前坐标
#ax.spines['left'].set_position(('data', 0)) #设置坐标轴位置
#ax.spines['left'].set_color(颜色)


#画图例
#mp.plot(...,label=图片文本)
#mp.legend(loc='upper left')


#画个散点图连接线
#mp.scatter(水平坐标数组，垂直坐标数组,marker=点型,s=大小,edgecolor=勾边色,facecolor=填充色,zorder=Z序)


#画备注：
'''
mp.annotate(
备注文本,
xy = 目标位置，
xycoords=目标坐标系,
xytext=文本位置,        #常用偏移位置
textcoords=文本坐标系,   #常用偏移坐标系 offset points,
fontsize=字体大小,
arrowporps = 箭头的属性)
'''



x = np.linspace(-np.pi,np.pi,1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
mp.xlim(x.min(), x.max())   #左右边界
mp.ylim(sin_y.min(),sin_y.max()) #上下边界
mp.xticks([-np.pi,-np.pi / 2, 0, np.pi /2,np.pi * 3 / 4, np.pi],
[r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
mp.yticks([-1, -0.5, 0.5, 1])

#设置坐标系，变成十字坐标系
ax = mp.gca()
ax.spines['left'].set_position(('data',0))    #将坐标轴的左边框移到0
ax.spines['bottom'].set_position(('data',0))  #将坐标轴下边框移动到0
ax.spines['right'].set_color('None')        #将坐标轴右边框的颜色设置为None
ax.spines['top'].set_color('None')          #将坐标轴上边框颜色设置为None

#设置图例
mp.plot(x, cos_y,linestyle='--',linewidth=6,color='dodgerblue',label=r'$y=\frac{1}{2}cos(x)$')
mp.plot(x, sin_y,linestyle=':',linewidth=3,color='orangered',label=r'$y=sin(x)$')
mp.legend(loc='upper left')

#画散点



mp.show()


