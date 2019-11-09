# class Student:
# 	def __init__(self,name,age,score):
# 		self.name,self.age,self.score = name,age,score
# 	def __repr__(self):
# 		return "Hello world"
# 	def infos(self):
# 		m = "Hello China"
# 		return m
# 	def __str__(self):
# 		return self.infos()
#
# s1 = Student("Bob",30,88)
# # print(str(s1))  #等价于print(s1)
# print(repr(s1))


# import time
# while True:
#     print('\r'+ time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),end='')
#
#     time.sleep(1)

# def fac(i):
#     if i == 0:
#         return 1
#     else:
#         return i * fac(i - 1)
# print(fac(5))
#
# import matplotlib.pyplot as mp
# import matplotlib
#
# font = {'family':'MicroSoft YaHei'}
# matplotlib.rc('font',**font)    #支持中文
#
# x = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
# y = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
#
# mp.figure(figsize=(20,8),dpi=80)
# mp.title('票房前20电影')
# mp.barh(range(len(x)),y,height=0.3,color='orange')
# mp.yticks(range(len(x)),x)
# mp.ylabel('影片名称')
# mp.xlabel('票房')
# mp.grid(linestyle=':',alpha=0.3)
# mp.show()
'''
1.题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃
了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半多一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少？（4分

peach(n - 1) =  peach(n) / 2 - 1 ==>peach(n) = (peach(n-1)+1)* 2

peach(n) = peach(n-1) * 2 + 2

'''

# def peach(n):
#     if n == 1:
#         return 1
#
#     else:
#         return (peach(n-1)+1) * 2
#
# ret=peach(10)
# print(ret)

import matplotlib.pyplot as mp
import numpy as np


x = np.linspace(0, 2, 40)
y = (np.sin(x - 2) ** 2) * np.exp(-2 ** 2)

mp.xlabel('x')
mp.ylabel('f(x)')
mp.title(r'$f(x) =\sin^2(x-2)e^(-x^2)$')
mp.grid(linestyle='-')
mp.plot(x,y)

mp.show()

