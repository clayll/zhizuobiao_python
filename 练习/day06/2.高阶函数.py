#map,reduce,filter

#1.map函数
#特点：对可迭代对象里的每一个元素进行相同的操作

li = [1, 2, 3]

#第一种写法：普通函数写法
#例1.
# def func1(x):
#     return x + 1
#
# res = map(func1,li)
# print(list(res))
#例2
#map作矢量化操作
# def f1(x):
#     return x + 3
#
# x = [4, 5, 6]
#
# y = list(map(f1,x))
# print(y)


#第二种map函数使用方法 结合lambda
# res1 = map(lambda x: x +1, li)
# print(list(res1))

#总结：map函数上述两种实现方式。（必须掌握！）

#map的其他例子：
# a, b = map(float,input("请输入两个内容，用逗号分隔:").split(','))
# print(a + b)
#============================================================
#reduce函数
#特点：从左至右对一个序列的项累计地应用有两个参数地函数，以此合并序列为一个单一值.（累加或累乘列表元素等)

# from functools import reduce
# nums = [1, 2, 3, 4]

#普通函数方式：
# def func2(x, y):
#     return x * y

#第一种使用reduce函数地方式 和lambda搭配
# res3 = reduce(lambda  x, y:x*y, nums)
# print(res3)

#第二种使用reduce函数方式 --普通函数
# res4 = reduce(func2,nums)
# print(res4)
#==========================================
#filter函数
#特点：对可迭代对象中的元素按照特定的条件进行筛选。

# L =  [0, 1, 2, 3, 4, 5, 6]

#定义筛选偶数的两种函数写法
# def func3(x):
#     if x%2==0:
#         return x
#
# def func4(x):
#     return x%2==0

#第一种使用filter函数和lambda搭配
# res5 = filter(lambda x: x%2==0, L)
# print(list(res5))

#第二种使用filter函数方式---普通函数一
# res6 = filter(func3,L)
# print(list(res6))

#第二种使用filter函数方式---普通函数二
# res7 = filter(func4,L)
# print(list(res7))
