#numpy的矢量
#矢量是指一堆数组成的集合
#标量是指单独一个数。
#多维数组也叫矢量化计算

#numpy和python执行计算的效率比较
import datetime as dt
import numpy as np
n = 100000
start = dt.datetime.now()   #记录当前时间
A, B = [], []
for i in range(n):
    A.append(i**2)
    B.append(i**3)
C = []
for a, b in zip(A,B):
    C.append(a + b)
print(type(C))
print('python执行',(dt.datetime.now() - start).microseconds)

#numpy来写
start = dt.datetime.now()
C = np.arange(n)** 2 + np.arange(n)**3
print(type(C))
print('numpy执行',(dt.datetime.now() - start).microseconds)

'''
1.arange，和python的range非常相似，只是多了个a
2.arange也是产生一个连续序列，但是不是列表，而是数组。
3.两数组可直接做运算（比如：直接加减乘除）
4.numpy内部完成循环，无需类似python的for循环遍历。
'''





