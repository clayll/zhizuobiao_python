#lambda函数
#匿名函数：是指一类无需定义标识符（函数名）的函数或子程序
#lambda函数可以接收任意多个参数（包括可选参数）并且返回单个表达式的值。
#语法：
# lambda [arg1,arg2...argn]:expression
#冒号前是参数，可以有多个，用逗号隔开；冒号右边为表达式（只能为一个）
#简单地说：lambda返回值是一个函数的地址，也就是函数对象。


#1.将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数
#普通函数
# def sum(x, y):
#     return x + y
# print(sum(1, 2))

#用lambda函数
# sum = lambda x, y: x + y
# print(sum(1, 2))


#2.将lambda函数作为参数传递给其他函数。 （部分python内置参数接收函数作为参数）
# def odd(x):
#     return x % 2
# temp = range(10)
# show = filter(odd, temp)
# print(list(show))

#lambda表达式改写
# print(list(filter(lambda x:x % 2,range(10))))

#3.和高阶函数搭配
#3.1
# map(函数,数值)
# sum = map(lambda x:x + 1, [1, 2, 3])
# print(list(sum))#[2, 3, 4]
#lambda函数用于指定过滤列表元素的条件
#3.2
#两外的还有:sorted()、 map()

#4. 将lambda函数作为其他函数的返回值,返回给调用者。
#函数返回值也可以是函数。
#例如： return lambda x, y: x+y
#这时，lambda函数实际是定义在某个函数内部的函数，称之为嵌套函数。
#对应的，包含在嵌套函数的函数之外称为外部函数。
#内部函数能够访问外部函数的局部变量，这个特性是闭包编程的基础。

# def sum(n):
#     return lambda x: x+n
# ret = sum(5)
# print(ret(20))

#5.将lambda函数赋值给其他函数，从而使其他函数用该lambda函数替换
# import time
# time.sleep(3)
#要求再后续代码中调用time库的sleep函数不会执行原有的功能
# time.sleep = lambda x:None.
#设置完上面的代码再执行time.sleep(3)，程序将不再休眠3秒，什么都不做。


#6.将if..else语句缩减为单一的条件表达式
#语法为:expression1 if A else expression2
#如果A为True，条件表达式的结果为expression1，否则为expression2
# def s(x):
#     if x == 1:
#         return "yes"
#     else:
#         return "no"

# print(s(1))
# print(s(0))

# s = lambda x:"yes" if x == 1 else "no"
# print(s(1))
# print(s(0))

