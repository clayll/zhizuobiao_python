import numpy as np

# a = np.ndarray((1,10))
# print(a)
#
# a = np.arange(1,10,3)
# print(a)
# a = np.array((1,10))
#
# a = np.empty((1,10))
# print(a)
# print(a .std())
#
# a = np.ones((1,5))
# print(a)

# a1 = np.array(['123','2','3'],dtype=np.int64)
# # a = a1.astype(np.str)
# # print(a)
# # print(type(a[1]))
# # print(a.dtype)
# #
# #
# # print(eval("4 * 2 + 5 % 2 + 4/3"))

def calculateAge(personno,age):

    if personno == maxPersonNumber:
        return age
    age += 2
    personno+=1
    return calculateAge(personno,age)

# 求第5个人
maxPersonNumber = 5
#第一个人的年纪
firstPersonAge = 10

print("第%d个人的年纪为：%d" % (maxPersonNumber,calculateAge(1,firstPersonAge)) )




def carInfo():

    def getDisplacement():
        return '1.6排量'



def carInfo1():
    displacement = lambda  : '1.6排量'

    print("发动机排量是%s" % displacement())

def f(x,l=[]):

    for i in range(x):

        l.append(i*i)

    print (l)

f(2)
f(3,[3,2,1])
f(3)

import numpy as np
np.hstack