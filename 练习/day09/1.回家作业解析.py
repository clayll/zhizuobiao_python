# 1.你是如何理解Python装饰器的？
#装饰器就是用于拓展原来函数功能的一种函数，它的目的是在不改变原函数名（类名）情况下，
#给函数增加新的功能

# import time
# #装饰器
# def wrap(func):
#     def wrapper():
#         start_time = time.time()
#         print(start_time)
#         func()
#         end_time = time.time()
#         print(end_time)
#         execution_time = (end_time - start_time) * 1000
#         print("time is %d ms" % execution_time)
#     return wrapper
#
# @wrap
# def func():
#     print("hello")
#     time.sleep(1)
#     print("world")
#
# func()


#1.列表推导式实现乘法口诀表

# for i in range(10):
#     print(" ".join(["%dX%d=%-2d"%(m,i,m*i) for m in range(1, i+1)]))
#-号 代表左对齐，2表示数字不足2位则补齐两位，不足的位置用空格填补


# 2.请使用for嵌套方法打印1-9三角形阵列:
# for i in range(1,10):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# 求列表list=[1,2,3,4,5]之和（1：通过调用库函数实现。2：自己写逻辑实现）
# import math
# list=[1,2,3,4,5]
# sumlist = sum(list)
# print(sumlist)

# from functools import reduce
# list=[1,2,3,4,5]
# sumlist = reduce(lambda x, y: x + y,list)
# print(sumlist)

# sum = 0
# list = [1,2,3,4,5]
# for i in list:
#     sum += i
# print(sum)
    # 0  + 1 =1
    # 1 + 2 =3
    # 3 + 3 = 6
    # 6 + 4 = 10
    # 10 + 5 =15


