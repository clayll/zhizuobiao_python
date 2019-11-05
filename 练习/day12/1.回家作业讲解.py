#实现斐波那契数列（递归）
# def fibo(n):
#     if n <= 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
# num = int(input('请输入数值:'))
# for i in range(num):
#     print(fibo(i),end=' ')

'''
3.构造一个词典：
实现功能如下：
1：用户可以添加单词，并可以添加单词的定义，比如：输入dictionary的同时，定义它的意思位“词典，字典”
2：可以查询单词的意思，
比如，输入bee
则列出：
蜜蜂; （集工作、竞赛、娱乐为一体的） 聚会;
'''

# class Dict(object):
#     def __init__(self, dic):
#         self.dic = dic
#
#     def add(self):
#         en = input("请输入要添加的英文单词:")
#         ch = input("请输入要添加的英文单词的中文翻译:")
#         self.dic.update([(en,ch)])
#         ch = self.dic
#         return ch
#
#     def lookup(self,dic):
#         en2 = input("请输入您要查询的英文单词:")
#         print(dic[en2])
#
# dic = {}
# dict = Dict(dic)
# addword = dict.add()
# dict.lookup(addword)


#4.手动输入5个数字，使用三目运算符，输出最大的那个数字
# a, b, c, d, e = map(int,input('请分别输入5个数字并以空格分开:').split(' '))
#
# f = a if a > b else b
# g = c if c > d else d
# m = f if f > g else g
# print( m if m > e else e)

# print(max(20,30, 40))  #max()内置函数


'''
定义一个类Human, 分别有属性姓名年龄和电话（name,age,tel）
类中定义三个方法，分别获取name,age,和tel
示例：
m = Human(‘tom’, 45, ‘123333333333’)
print(m.getname())
print(m.getage())
print(m.gettel())
输出：
tom
45
123333333333
'''
# class Human:
#     def __init__(self,name,age,tel):
#         self.name = name
#         self.age = age
#         self.tel = tel
#
#     def getname(self):
#         return self.name
#
#     def getage(self):
#         return self.age
#
#     def gettel(self):
#         return self.tel
#
# m = Human('tom', 45,'123333333333')
# print(m.getname())
# print(m.getage())
# print(m.gettel())


# 2.
# 1、阅读下面的代码，写出A0，A1至An的最终值。
# A0 = zip(('a','b','c','d','e'),(1,2,3,4,5))
# print(dict(A0))

# A1 = range(10)
# A2 = [i for i in A1 if i in A0]
#
# A3 = [A0[s] for s in A0]
#
# A4 = [i for i in A1 if i in A3]
#
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]

# 计算桃子数量
def cacalP(n):
    return (n+1)*2

def run1():
    # 天数
    day = 10
    # 桃子数量
    n = 1
    # 循环10次，表示10天
    for i in range(0,day):
        # 递归运算桃子数量
        n = cacalP(n)
    print(n)
run1()

import numpy as np
import matplotlib.pyplot as plt
def run2():

    plt.title(r'$f(x)=\sin^2(x-2)e^{-x^2}$')
    x = np.arange(0,2,0.25)
    y = np.power(np.sin((x-2)),2)*np.exp(-pow(x,2))
    plt.grid(linestyle=':')
    plt.ylabel("f(x)")
    plt.xlabel("x")
    plt.plot(x,y,'o-')

    plt.show()

run2()

