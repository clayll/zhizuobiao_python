import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma



#简单动画
#第一种方式：给定一个更新函数，我们自己定义一个回调函数，自己不调用，让别人调用。

#ma.FuncAnimation(图形对象,更新函数,interval=间隔时间(毫秒))





n_bubbles = 100

#自定义结构 每个数组就是每个气泡(气泡数组)
#dtype自定义符合结构
# ('position',float,2)  数字2代表是x轴和y轴
#('size',float,1)
#('growth',float,1)
#('color',float,4) 数字4代表红 绿 蓝 透明度
bubbles = np.zeros(n_bubbles,dtype=[
    ('position',float,2),
    ('size',float,1),
    ('growth',float,1),
    ('color',float,4)])

#初始化位置数组
#np.random.uniform均匀分布随机数(最小值)
bubbles['position'] = np.random.uniform(0, 1, (n_bubbles,2))
bubbles['size'] = np.random.uniform(50, 750, n_bubbles)
bubbles['growth'] = np.random.uniform(30,150,n_bubbles)
bubbles['color'] = np.random.uniform(0,1,(n_bubbles,4))
mp.figure('Bubbles',facecolor='lightgray')
mp.title('Bubbles',fontsize=20)
mp.xticks(())
mp.yticks(())
#画散点图
#x轴:bubbles['position'][:,0]; y轴: bubbles['position'][:,1]
#不能使用s=数值，如果这样写所有气泡都一样大
sc = mp.scatter(bubbles['position'][:,0],
           bubbles['position'][:,1],
           s=bubbles['size'],
           c=bubbles['color'])

def update(number):
    bubbles['size'] += bubbles['growth']
    #气泡破裂方法：
    #根据number数，让不同的气泡发生破裂
    #变成0-99之间的循环，作取余运算，让下标总是合理
    burst = number % n_bubbles
    bubbles['position'][burst] = np.random.uniform(0, 1, 2)
    bubbles['size'][burst] = 0 #初始大小为0
    bubbles['growth'][burst] = np.random.uniform(30,150) #更新膨胀的速度
    bubbles['color'][burst] = np.random.uniform(0, 1, 4)
    #修改位置的值
    sc.set_offsets(bubbles['position'])
    #修改颜色
    sc.set_facecolor(bubbles['color'])
    sc.set_sizes(bubbles['size'])
    #修改尺寸的值
    sc.set_sizes(bubbles['size'])

anim = ma.FuncAnimation(mp.gcf(),update,interval=10)
mp.show()




