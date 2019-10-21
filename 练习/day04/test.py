def test(arg1,arg2 :list):
    print(arg1,arg2)
    print(type(arg2))

# x= test
#
# x(arg2=[2,3],arg1=1)

# tuple 加一个*号接收的是元组格式
def print_numbers(*args):
    print(type(args))  # tuple
    for n in args:
      print(type(n))   # int


def print_kwargs(**kwargs):
    print(kwargs)

# print(globals())
#
# print(locals())


def q1():
    x = range(1,1,1)
    print(x)
    print(type(x))

def q2():
    # 随机定义集合
    set1 = {11,133,44,42,56,1}
    sortSet=[]
    for i in range(len(set1)):
        temp = min(set1)
        sortSet.append(temp)
        set1.remove(temp)

    print(sortSet)

def q3():
    import math

    l1 = input("请输入三角形的三条边，用逗号分开").split(",")
    a,b,c = float(l1[0]),float(l1[1]),float(l1[2])
    if (a+b) < c or (a+c) <b or (b+c)<a:
        return print("两边之和必须大于第三边")

    p=(a+b+c)/2
    print("海伦公式的值为：%.2f" % math.sqrt(p*(p-a)*(p-b)*(p-c)) )


def q4():

    x = [i.lower() for i in "aisjdfkjsjfsdfslkjf"]
    print(x)


q4()