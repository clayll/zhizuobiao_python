#前言：numpy时一个模块，把所有matlab的功能都包括了。涵盖了所有已知数学函数领域的内容。
#数据类型是数组 Numpy都是围绕数组展开。一般称之为ndarray。
#引入numpy包
import numpy as np

#1.创建数组的方法:a = np.array(),括号中接受任何numpy可接受的容器(元组和列表)，转换成数组

# a = np.array([0, 1, 2, 3, 4])
# print(a)#[0 1 2 3 4] <class 'numpy.ndarray'>
# print(a[1]) #下标查询方式基本同python
#
# b = np.array((0, 1, 2, 3, 4))
# print(b) #[0 1 2 3 4]
#
# #2. np.arange(5)
# c = np.arange(5)
# print(c) #[0 1 2 3 4]
#
# # #3.线性空间创建数组 linespace
# # #np.linspace(0, 2*np.pi, 5) 生成从0到2Π的5个数字
# # d = np.linspace(0, 2*np.pi, 5)
# # print(d)
#
# e = np.array([[11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25],
#      [26, 27, 28, 29, 30]])
# print(e) #生成一个四行五列的数组
#
# #二维数组，行和列称为二维数组。
# #三维数组，页，行，列称之为三维数组
#
# #2.多维数组的切片
# print(e[0,1:4])
#     #   行  列
#
# print(e[1:4, 0])
#    #    行   列
#
# print(e[:, ::2])
#        # 行  列
#
# print(e[:,1])
       #行，列   :代表所有行或所有列

#3.使用数组
#3.1基本操作符  +-*/
#reshape的使用，可以改变数组的维度
a = np.arange(25)
# print(a)

a = a.reshape(5, 5)    #改为5行5列
print(a)

b = np.array([10, 62, 1, 14, 2,56,79,2,1,45,4,92,5,55,63,43,35,6,53,24,56,3,56,44,78])
# print(b)

b = b.reshape(5, 5)
print(b)

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
print(a < b)
print(a)
print(a[a<b])
# print(a > b)
#dot() 计算两个数组中的点积，它返回时一个标量，而不是数组
# print(a.dot(b))      #数组A逐行*数组B逐列