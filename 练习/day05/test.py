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

list()

iter


