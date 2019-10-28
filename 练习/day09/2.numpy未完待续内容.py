import numpy as np
a = np.arange(11, 20).reshape(3, 3)
# print(a)
b = np.arange(21, 30).reshape(3, 3)
# print(b)
#组合和拆分
#1.1 垂直组合:
#numpy.vstack((上,下)) 栈
# c = np.vstack((a,b))
# print(c.shape)

#1.2 垂直拆分：
#numpy.vsplit(数组，份数)
# a, b = np.vsplit(c, 2)
# print(a)
# print("="*120)
# print(b)

#2.1水平组合
#numpy.hstack((左 右)) 栈
c = np.hstack((a, b ))
# print(c)
'''
[[11 12 13 21 22 23]
 [14 15 16 24 25 26]
 [17 18 19 27 28 29]]
'''

#2.2水平拆分
#numpy.hsplit(数组,份数)

# a, b = np.hsplit(c,2)
# print(a)
# print("*" * 120)
# print(b)

#3.1 深度组合
c = np.dstack((a, b))
# print(c)

#3.2深度拆分
a, b = np.dsplit(c, 2)
# print(a)
# print("-"*120)
# print(b)
#特点：只能组合不能拆分

#注：如需要恢复成二维数组样式，需要手工来操作

# print(a.T[0].T) #先T转置取0号元素后再转置
# print('='*120)
# print(b.T[0].T) #先T转置取0号元素后再转置

#numpy.row_stack((上 下))等价于numpy.vstack
#numpy.column_stack((左 右)) 等价于numpy.hstack
#numpy.column_stack((左 右))有简略写法np.c_[左 右]
