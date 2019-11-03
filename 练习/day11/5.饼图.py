#饼图(扇形)

#mp.pie(值列表,间隙列表,标签列表,颜色列表,格式串,shadow=是否有阴影,startangle=起始角度)


import numpy as np
import matplotlib.pyplot as mp


mp.figure('Pie',facecolor='lightgray')
mp.title('Pie',fontsize=20)
mp.pie(
    [26, 17, 21, 29, 11],
    [0.05, 0.01, 0.01, 0.01, 0.01],
    ['Python','JavaScript','C++','C','PHP'],
    ['dodgerblue','orangered','limegreen','violet','gold'],
    '%d%%',shadow=True,startangle=90)

mp.axis('equal') #等轴;画出的圆不变形

mp.show()




