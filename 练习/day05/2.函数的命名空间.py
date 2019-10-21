#namespace 命名空间，名称空间
#局部命名空间：每一个函数都有自己的命名空间
#全局命名空间:写在函数外面的变量名
#内置命名空间:python解释器启动之后就可以使用的名字。


# n = 10
#
# def func():
#     m = 1
#     print(n)
#
# func()

# def func2():
#     m = 2


# def func2():
#     print('in func2 now')
#     print('多写的一行')
#     if True:
#         print('又多写了一行')
#     return 'func2的返回值'
#
# def func():
#     ret = func2()
#     print(ret)
#     n = 20
#     print(n)
#
# func()

#python的解释器要运行起来
#加载顺序：
    #先所有内置命名空间中的名字 --> 然后按照顺序加载全局命名空间中的名字
    #局部命名空间中的名字：在调用函数的时候产生，并且随着调用的结束而消失


#函数的嵌套定义
# def func():
#     def qqxing():
#         print('我是qq星')
#     qqxing()
#
# func()


# def func1():
#     n = 3
#     def func2():
#         n = 2
#         print(n)
#     func2()
# func1()

# n = 0
# def func1():
#     def func2():
#         print(n)
#     func2()
# func1()

#作用域：一个名字可以使用的区域
#全局作用域： 内置名字空间和全局命名空间中的名字都属于全局作用域
#局部作用域：局部名字空间中的名字属于局部作用域
#局部作用域可以使用全局作用域中的变量
#而全局作用域不能使用局部作用域中的变量
#局部作用域中还可以嵌套更小的局部作用域
#作用域链:小范围作用域可以使用大范围的变量，但作用域链是单向的，不能反向应用。


# def func():
#     a = 10
#     b = 20
#
# n = 10
# m = 22
# print(globals()) #保存在全局作用域中的名字和值
# func()

#globals(): #保存在全局作用域中的名字和值
#locals(): #会根据执行的位置来决定作用域中的内容
#如果在全局执行：
#globals和locals打印的结果是一致的。



#函数的嵌套调用和函数的嵌套定义
#命名空间： 三种： 内置 全局 局部
#作用域：全局作用域 局部作用域
#作用域链：名字的使用从小范围到大范围的就近时间
#globals和locals的方法
#小范围可以使用大范围的，但是不能修改
    #如果想要修改:使用global关键字  --> 尽量避免使用
    #如果想要修改最近拥有该变量的外层函数的：使用nonlocal ---不影响全局


# n = 1
# def func():
#     global n
#     n += 1
#
# func()
# print(n)


n = 0
def func():
    n = 1
    def func2():
        global n
        n += 1
    func2()
    print(n)

func()
print(n)





