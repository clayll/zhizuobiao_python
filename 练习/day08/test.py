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

# f(2)
# f(3,[3,2,1])
# f(3)

from functools import reduce

'''
输入斐波拉契数列的位数
'''
def fbncText(n):
    # 生成斐波拉契数列
    lis = []
    for i in range(n):
        # 第1,2项 都为1
        if i == 0 or i == 1:  # 第1,2项 都为1
            lis.append(1)
        else:
            lis.append(lis[i - 2] + lis[i - 1])

    rs = reduce(lambda x,y: x+y ,lis)
    print(rs)

fbncText(10)

d = {}



class MyDictionary:

    def __init__(self):
        self.dictionary = dict()

    def start(self):
        while True:
            v = input("请选择功能：1 添加单词，2 查询单词解释 3 退出 :")
            if v.strip() == '1':
                self.addDiction()
            elif v.strip() == '2':
                self.getDictionByKey()
            elif v.strip() == '3':
                break
            else:
                print("输入有误!")

    def addDiction(self):
        ls = input("请输入单词和解释并用空格隔开：").split(' ')
        self.dictionary.setdefault(ls[0],ls[1])

    def getDictionByKey(self):
        try:
            v = self.dictionary[input("请输入单词名称：")]
            print("您输入的单词的解释是：", v)
        except Exception:
            print('未找到该单词!')

def test3():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != k and i != j and j != k:
                    print(i,j,k)
#
# k = MyDictionary()
# k.start()
def test4():

    l1 = list(map(float,input("输入5个数，请用空格隔开:").split(' ')))
    if len(l1) != 5:
        print("输入有误")
        return

    (x,y,z,w,q)= l1

    v =  ((x if x > y else y) if (x if x > y else y) > z else z) if  ((x if x > y else y) if (x if x > y else y) > z else z)  > w else w
    (((x if x > y else y) if (x if x > y else y) > z else z) if ((x if x > y else y) if (
                                                                                           x if x > y else y) > z else z) > w else w ) if (((x if x > y else y) if (x if x > y else y) > z else z) if ((x if x > y else y) if (
                                                                                           x if x > y else y) > z else z) > w else w ) > q else q

    print("最大值为：",v)




test4()