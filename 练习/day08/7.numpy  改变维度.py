import numpy as np
#numpy变维方式 有4种

#1.视图变维
'''
针对一个数组对象获取不同维度的视图
方法:数组.reshape(新维度) =>数组新维度视图
     数组.ravel()  => 数组的一维视图
'''

# a = np.array([np.arange(1, 9)])
# # print(a)
#
# b = a.reshape(2, 4)
# # print(b)
#
# c = b.ravel()
# print(c)

#2.复制变维度(不同维度拷贝)
'''
针对一个数组对象获取不同维度的副本
方法：flatten()  ==> 数组的一维副本
功能：在获得原数据实例的同时获得拷贝（也就是副本）
'''
# d = b.flatten()
# print(d) #复制成一维

# e = b.reshape(2, 2, 2).copy()
# print(e)


#3.就地变维
'''
数组.shape = (新维度)
等价于
数组.resize(新维度)
'''
# a = np.array([np.arange(1, 9)])
# a.shape = (2, 2, 2)
# # a.resize(2,2,2)
# print(a)#变成一个新的2页2行2列得三维数组

#4.视图转置
'''
可理解为行列互换
数组.transpose()  => 数组得转置视图
等价于
数组.T => 转置视图属性

'''

a = np.array([np.arange(1, 9)])
a.shape = (4,2) #a 是4行2列
# print(a)
# g = a.transpose()
# print(g)

# g = a.T
# print(g)

print(np.array([a]).T) #先转职成多维数组
print(a.reshape(-1, 1)) #输入-1这个无效值






