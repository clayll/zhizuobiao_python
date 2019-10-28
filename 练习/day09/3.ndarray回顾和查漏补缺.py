import numpy as np
#回顾ndarray属性
""""
dtype元素类型
shape数组维度
T转置视图
ndim维度数
size元素数，等价于python的len()
npytes 元素的总字节数

len() 永远得到shape里的第一个元素, size得到的是shape里的乘积
itemsize 元素的字节数，即一个元素占多少字节
flat 扁平迭代器。 得到一个迭代对象，可进行迭代遍历
tolist 数组改列表
imag 虚部数组
real 实部数组
"""
#
# a = np.array([
#     [1+1j,2+4j,3+6j],
#     [1+1j,2+4j,3+6j],
#     [1+1j,2+4j,3+6j]
# ])
#
# print(a.dtype) #complex128 16个字节  8位实部 8位虚部
#
# print(a.shape) #(3, 3) 3行3列
#
# print(a.ndim) # 2维
#
# print(a.size) #9个元素
#
# print(len(a)) #3行
#
# print(a.itemsize) #每个元素占16个字节
#
# print(a.nbytes) #144个字节 16 * 9 =144
#
# print(a.T)
#
# print(a.real) #取实部
# print(a.imag) #取虚部
#
# for i in a.flat:
#     print(i)
# #flat扁平迭代器

#补充:append

def fun(z,zz):
    z.append(zz)
    return z

x = np.array([1,2,3])
y = 40

# ret = fun(x, y) #会报错，因为数组没有append方法
ret = fun(x.tolist(),y)  #x.tolist()数组转列表
print(ret)

