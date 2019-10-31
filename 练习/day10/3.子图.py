import matplotlib.pyplot as mp
import matplotlib.gridspec as mg    #栅格布局器
#子图：大图里创建小图

#1.默认(缺省)布局
#缺点：比较嗲版
# mp.figure(facecolor='lightgray')
# for i in range(2):
#     for j in range(3):
#         k = i * 3 + j + 1
#         print(k)
#         # mp.subplot(231)#2行3列第一张
#         mp.subplot(2,3,k)
#         mp.xticks(()) #不带刻度线
#         mp.yticks(())
#         mp.text(0.5,0.5,str(k),ha='center',va='center',size=36,alpha=0.5)
# mp.show()

#mp.text(对文字中的比例, 对文字中心的比例, 字符串,ha=水平对齐, va=垂直对齐, size=字体大小, alpha=透明度)

#2.栅格布局
#先建一个栅格布局器
#import matplotlib.gridspec as mg
#gs = mg.GridSpec(行数,列数)
#mp.subplot(gs[行,列])

# mp.figure(facecolor='lightgray')
#生成栅格布局器
# gs = mg.GridSpec(3,3)   #3行3列  九宫格
# mp.subplot(gs[0,:2])    #形状
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5,0.5,1,ha='center',va='center',size=36,alpha=0.5)
#
# mp.subplot(gs[1:,0])    #形状
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5,0.5,2,ha='center',va='center',size=36,alpha=0.5)
#
#
# mp.subplot(gs[2, 1:])    #形状
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5,0.5,3,ha='center',va='center',size=36,alpha=0.5)
#
#
# mp.subplot(gs[:2, 2])    #形状
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5,0.5,4,ha='center',va='center',size=36,alpha=0.5)
#
# mp.subplot(gs[1,1])    #形状
# mp.xticks(())
# mp.yticks(())
# mp.text(0.5,0.5,5,ha='center',va='center',size=36,alpha=0.5)

#3.自由布局: 没有格子
#mp.axes([左下角水平坐标,左下角垂直坐标,宽度,高度])

mp.figure(facecolor='lightgray')
mp.axes([0.03, 0.038, 0.94, 0.924])

mp.xticks(())
mp.yticks(())
mp.text(0.5,0.5,1,ha='center',va='center',size=36,alpha=0.5)


mp.axes([0.63, 0.076, 0.31, 0.308])
mp.xticks(())
mp.yticks(())
mp.text(0.5,0.5,2,ha='center',va='center',size=36,alpha=0.5)


mp.show()








