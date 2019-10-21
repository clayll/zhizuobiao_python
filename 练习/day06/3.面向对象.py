#面向对象
#1.创建类和对象
#创建类, foo是类名
# class Foo(object):
#     #创建类中的函数,self特殊参数，必填！
#     def Bar(self):
#         #做事情
#
# #根据类Foo创建实例化对象obj
# obj = Foo()

#1.1例:
# class Foo(object):
#
#     def Bar(self):
#         print('BAR')
#
#     def Hello(self,name):
#         print('i am %s'%name)
#
# obj = Foo()
# obj.Bar()#执行了Bar方法
# obj.Hello('xiangxiang') #执行了Hello方法

#2.特征：
#2.1封装:本质将十五相关属性和方法封装在一个类里面。
#第一步：将内容封装到某处
# class Foo(object):
#     #构造方法
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj1 = Foo('liangliang',18) #自动执行__init__方法
# #将liangliang和18分别封装到self(obj1)的name和age属性中
#
# obj2 = Foo('huifang',15) #自动执行__init__方法
#将huifang和15分别封装到self(obj2)的name和age属性中

#第二步：从某处调用被封装的内容
# print(obj1.name)
# print(obj2.age)

#完整的例子：

# class Foo(object):
#     #构造方法
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def detail(self):
#         print(self.name)
#         print(self.age)
#
#
# obj1 = Foo('liangliang',18)
# obj1.detail()
#
#
# obj2 = Foo('huifang',15)
# obj2.detail()

#继承:子类需要复用父类里面的属性或者方法。
#例1:
# class Cat(object):#
#     def cry(self):
#         print("喵喵叫")
#     def eat(self):
#         print("吃东西")
#     def drink(self):
#         print("喝东西")
#     def pee(self):
#         print("拉便便")

# class Animal(object):
#     def eat(self):
#         print("%s 吃" % self.name)
#     def drink(self):
#         print("%s 喝" % self.name)
#     def shit(self):
#         print("%s 拉" % self.name)
#     def pee(self):
#         print("%s 撒" % self.name)
#
# class Cat(Animal):
#
#     def __init__(self, name):
#         self.name = name
#         self.breed = '猫'
#
#     def cry(self):
#         print('喵喵叫')
#
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#         self.breed = '狗'
#
#     def cry(self):
#         print('汪汪叫')
#
#
# ######执行#####
# c = Cat('小白家的小花猫')
# c.shit()
#
# c2 = Cat('小花家的小白猫')
# c2.drink()
#
# d = Dog("胖子家的小瘦狗")
# d.eat()
#对于面向对象的继承而言,其实就是将多个类共有的方法提取到父类中，子类仅需继承父类二不必一一实现每个方法。
#注：除了子类和父类，python中还有 派生 和 基类。它们只是和 父类与子类的叫法不同而已。

#多态:同一个方法不同对象调用同一个方法功能的表现形式不一样。

#python中普通的多态
# a = 1
# b = 2
# print(a + b) #3 算数做加法
# c = 'hello'
# d = 'world'
# print(c + d)
# print(2*2)
# print('*' * 120)
# print(10%3)
# print('%s'%('我'))

#面向对象多态，显示类型---鸭子类型。
#特点：哪怕两个对象是继承不同的父类，只要对象a和b中都有同名的方法(fly),a对象能调用fly做事情，b对象也能做到。
#实例
# class Animal:
#
#     def kind(self):
#         print('i am animal')

# class Dog(Animal):
#
#     def kind(self):
#         print('i am a dog')
#
# class Cat(Animal):
#
#     def kind(self):
#         print('i am a cat')
#
# class Pig(Animal):
#
#     def kind(self):
#         print('i am a pig')
#
# #这个函数是接收一个animal参数，并调用其kind方法
# def show_kind(animal):
#     animal.kind()
#
# d = Dog()
# c = Cat()
# p = Pig()
#
# show_kind(d)
# show_kind(c)
# show_kind(p)
#例子总结：由于python动态语言特性，传递给函数show_kind的参数animal可以是任何类型，只要它
#有一个kind()方法即可。动态语言调用实例方法时不检查类型，只要方法存在，参数正确，就可以调用。

#例2 鸟
#
# class Bird(object):
#     def fly(self):
#         print("鸟飞起来")
#
# class Swan(Bird):
#     def fly(self):
#         print("天鹅飞起来了")
#
# class Animal(object):
#     def eat(self):
#         print("吃东西")
#
# class Duck(Animal):
#     #在python里 多态不关心类型，只关心对象是否有对应的方法。即只关心fly()这个方法。
#     def fly(self):
#         print("鸭子飞了")
#
#
# def FlyTwice(args):
#     args.fly()
#     args.fly()
#
# duck = Duck()
# FlyTwice(duck)


#================================
#补充:super()函数
#特点：在子类中如果有与父类同名的成员，那就会覆盖父类的成员。
#那如果要强制调用父类中的成员---super()函数。

# class A:
#     def __init__(self, name):
#         self.name = name
#         print("父类的__init__方法被执行了!")
#
#     def show(self):
#         print("父类的show方法被执行了!")
#
# class B(A):
#     def __init__(self,name,age):
#         super(B,self).__init__(name=name)
#         self.age = age
#
#     def show(self):
#         super(B,self).show()
#
# obj = B('xianxian', 11)
# obj.show()


