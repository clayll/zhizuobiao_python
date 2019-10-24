#1.类的成员
#类的成员分为三大类:字段、方法、属性

#1.1字段
#普通字段 属于对象
# 静态字段 属于类

# class Province:

    #静态字段
    # country = '中国'
    #
    # def __init__(self, name):
    #     #普通字段
    #     self.name = name

#直接访问普通字段
# obj = Province("河北省")
# print(obj.name)

#直接访问静态字段
# print(Province.country)
#静态字段内存中只保存一份
#普通字段在每个对象中都要保存一份


#1.2方法
#普通方法
#由 对象 调用；至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self

#静态方法：由类调用；没有默认参数

#类方法
#由类调用；至少一个cls参数；执行类方法时，自动将调用该方法的类扶着给cls

#三种方法内存都归于类
#区别：调用的方式不同

# class Foo:
#
#     def __init__(self,name):
#         self.name = name
#
#
#     def ord_func(self):
#         """定义普通方法，至少一个self参数"""
#         print(self.name)

    # @classmethod
    # def class_func(cls):
    #     """定义类方法，至少一个cls参数"""
    #     print('类方法')
    #
    # @staticmethod
    # def static_func():
    #     """定义静态方法，无默认参数"""
    #     print('静态方法')

#调用普通方法
# f = Foo("name")
# f.ord_func()

# #调用类方法
# Foo.class_func()

#调用静态方法
# Foo.static_func()


#三者区别：
#相同点：对于所有的方法而言，均属于类（非对象）中，所以在内存中也只保留一份。
#不同点:方法调用者不同，调用方法时自动传入的参数不同。

#1.3属性
# class Foo:
#
#     def func(self):
#         print('hello')
#
#     #定义属性
#     @property
#     def prop(self):
#         print('这是属性中的内容')
#
#
# foo_obj = Foo()
# foo_obj.func()
#
# foo_obj.prop    #调用属性

# class Goods:
#
#     @property
#     def price(self):
#         return "mianxiangduixiang"
#
# obj = Goods()
# ret = obj.price
# print(ret)


#注意：属性的定义和调用需要注意以下几点:
#1.定义时，在普通方法的基础上添加 @property装饰器
#2.定义时，属性仅有一个self属性
#3.调用时,无需括号
#方法:obj.price()
#属性:obj.price

#-------------------------------定义-------------------------------------
# class Pager:
#
#     def __init__(self,current_page):
#         self.current_page = current_page
#         self.per_items = 10
#
#     @property
#     def start(self):
#         val = (self.current_page - 1) * self.per_items
#         return val
#
#     @property
#     def end(self):
#         val = self.current_page * self.per_items
#         return val
#
#
# #--------------------调用---------------------
# p = Pager(1)
# print(p.start) #起始值
# print(p.end)   #终止值




# class Goods(object):#新式类写法
# class Goods:#旧式类写法










# print(m.getname)
# print(m.getage,m.gettel)


#2.类成员的修饰符
#类成员的两种形式:
#公共成员:在任何地方都能访问


#私有成员:只有在类的内部才能访问:
#特点: 私有成员命名时，前面两个字符都是下划线(例:__init__,__call__,__dict__)

# class C:
#     def __int__(self):
#         self.name = '公有字段'
#         self.__foo = '私有字段'

#两种静态字段的区别：
#公有静态字段:类可以访问；类内部可以访问，派生类中可以访问
#私有静态字段:仅类内部可以使用。

# class C:
#     name = '公有静态字段'
#
#     def func(self):
#         print(C.name)
#
# class D:
#     def show(self):
#         print(C.name)
#

# print(C.name)   #类访问
#
# obj = C()
# obj.func() #类内部可以访问

# obj_son = D()
# obj_son.show() #派生类中可以访问


# class C:
#     __name = '私有静态字段'
#
#     def func(self):
#         print(C.__name)
#
# class D(C):
#     def show(self):
#         print(C.__name)


# print(C.__name)   #类访问    报错

# obj = C()
# obj.func() #类内部可以访问 正确

# obj_son = D()
# obj_son.show() #派生类中可以访问   报错


#两种普通字段的区别：
#公有普通字段:类可以访问；类内部可以访问，派生类中可以访问
#私有普通字段:仅类内部可以使用。

class C:

    def __init__(self):
        self.__foo = '私有普通字段'
    def func(self):
        print(self.__foo)

class D(C):

    def show(self):
        print(self.__foo)

obj = C()
obj.func()


#类的特殊成员
#1. __doc__ 2.__module__,3. __main__
















