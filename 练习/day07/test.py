class A():
    name="A"

    __nickName="bbbb"

    @property
    def price(self):
        print(1)

    def go(self):
        print("aaaa")




class B():
    def show(self):
        print(":bbbb")


class A1(A):
    def go(self):
        print("1111111111")
# import numpy as np
#
# print(np.array(list("1123")))
#
# np.arange(10)

def test1():
    rs = [(j+1)*(i+1) for j in range(9) for i in range(9)]
    print(rs)

def test2():

    for i in range(10):
        # 存储结果变量
        rs = ""
        for j in range(i):
            rs += str((j+1))+" "
        print(rs)

# print(test2())

# 调用内建包中sum
ls = [i+1 for i in range(5)]
print(sum(ls))

#自己实现
def sumList(ls):
    rs = 0
    for i in ls:
        rs += i
    return rs
ls = [i+1 for i in range(5)]
print(sumList(ls))


