from functools import reduce
def fn(x, y):
    return x + y
x = reduce(fn, [1, 3, 5, 7, 9])

print(x)


def fun(x):
    if x % 2 ==0:
        return x


L = [0,2,4,6]

ret = filter(fun,L)
for i in  ret:
    print(i)

xx=5

class Foo:
    def getName(self):
        print("xxxx")


f = Foo()

d1 = {1:"ce",2:"jjj",3:type(range(1,2))}


d2 = dict(one="222",tew="333")

d3 =dict(((1,2),(3,111)))
print(d3)

def test1(arg):
    arg=3
    print(arg)
a = 2
test1(a)
print(a)

def test2(arg):
    arg[0]=5
    print(arg)

l1=list((1,2,3,4))
test2(l1)
print(l1)


def f(a,b):

    a = 4

    print(a, b)

def main():
    a = 5

    b = 6
    print(a, b)

    f(a,b)

    print(a, b)

main()



import time

def deco(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        f(*args,**kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
    return wrapper

def after(f):
    def wrapper(*args,**kwargs):
        f(*args, **kwargs)
        print("调用完成")
    return wrapper

def before(f):
    def wrapper(*args,**kwargs):
        print("调用开始")
        f(*args, **kwargs)
    return wrapper

@after
@deco
@before
def f(a,b):
    print("be on")
    # time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f(3,4)



A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)
A1 = range(10)
print(list(A1))

A2 = [i for i in A1 if i in A0]
print(A2)

A3 = [A0[s] for s in A0]
print(A3)

A4 = [i for i in A1 if i in A3]
print(A4)

A5 = {i:i*i for i in A1}
print(A5)

A6 = [[i,i*i] for i in A1]
print(A6)
