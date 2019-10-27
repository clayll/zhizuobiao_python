#numpy多维数组
#用numpy.ndarray类(n代表多个，d代表dimension维度)
#ndarray本身就是一个类，由这个类实例化出来的对象，就是多维数组
#多维数组也是一个对象。
#一、创建多维数组的方法:
#1. numpy.arange(起始值,终止值,步长)
#它时间通过numpy来访问，是numpy的一个函数
#它返回的数组是一个等差数列的一维数组。
import numpy as np
#np.arange(方法)
# a = np.arange(10)
# print(a)
#
# b = np.arange(1,10)
# print(b)
#
# c = np.arange(1,10,2)
# print(c)

#2.numpy.array()
#注：这个array不是类，只是numpy中的一个方法（函数）
#在numpy.array()函数的括号里，可以输入任何可被解释为数组的容器(列表和元组)。
#np.array方法
# d = np.array([])
# print(d)

# e = np.array([10, 20, 30, 40, 50])
# print(e)
# e = np.array((10, 20, 30, 40, 50))
# print(e)

# f = np.array([
#     [1, 2, 3],
#     [4, 5, 6]])
# print(f)
# print(type(f)) #numpy.ndarray
# print(type(f[0][0]))#numpy.int32
# print('这个',f.dtype) #dtype 表示元素的数据类型

# g = np.array(['1', '2', '3'])
# print(type(g[0]))  #方法一：python取类型的方法
# print(g.dtype)  #方法二： numpy取类型的方法
#<U1 :U代表Unicode,< 代表小端字节序，1代表每个字串里有1个字符。

# g = np.array(['1', '2', '3'],dtype=np.int32)
# print(type(g[0]))
# print(g.dtype)
#int32 ：32位=4个字节；int32就是4个字节的整型数
#思考:为什么是int32？
#答：在定义时未指定具体类型，而现在使用4个字节整型正好能保存g的数据。
#所以default（默认）缺省值就是4个字节。



#astype:作为某种类型的意思
#--思考：用了astype作类型转换后，g里面的类型是否会有转换？
#--没有任何影响。

#numpy中所有和数据类型转换有关的内容，其实都不是真正的数据转换，都是复制
#都是按新的类型再给你复制一份，但是对于原数据是不变的。
# h = g.astype(np.str_) #转回字符串类型，转回去了
# print(type(h[0]))
# print(h.dtype)#转回字符串类型后，元素数据类型变成<U11，而不是<U1了
#<U11: 因为转回来之后，从内存会预留一些空间，所以显示<U11。
#str_ 表示字符串，为了和python区别，str后加了"_"作区分


