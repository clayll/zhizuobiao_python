#lst形参； 接受参数
# def my_len(lst):
#     print(lst)
#     count = 0
#     for i in lst:
#         count += 1
#     return count

# my_len([2,100,99])# 参数；传参数/传参
# l = [1, 2, 3, 4]
# len_count = my_len(l)
# print(len_count)
#
# len_count2 = my_len('靓靓 is handsome')
# print(len_count2)

#例:
#写一个函数：接收参数一个列表或者字符串。
#如果这个列表或者字符串长度大于2，返回True，否则返回False。
# def func(s_l):
#     if len(s_l) > 2:
#         return True
#     else:
#         return False
#
# print(func([1, 2, 3, 4]))
# print(func('123456'))


#1、参数
#形参和实参
#简单地传递一个参数
#传参数可以传任意的数据类型，并且传什么，接收什么！

#在传参数的角度上看问题：一共有两种传参方式
    #第一种：按照位置传参
    #第二种：按照关键字传参

#传一个参数：
# def f(para):
#     print(para)
#
# f(para = 1)

#传多个参数
# def f2(arg1, arg2):
#     print(arg1)
#     print(arg2)
#
# # f2(1,'abc')   #按位置传参，必须按顺序
# # f2(arg2='abc',arg1=1) #按关键字传参，无需按照顺序
# f2([1, 2, 3],arg2='abc')

#按照关键字传参和按照位置传参是可以混用的。
#但是 首先传位置传参，再传关键词传参。切记！


#2、形参
#2.1、位置参数
#数量必须与实参数量一致

# def classmate(name,gender):
#     print('姓名:%s, 性别:%s'%(name, gender))

# def classmate(name,gender='男'):
#     print('姓名:%s, 性别:%s'%(name, gender))
#
# classmate('靓靓')
# classmate('欣慰','女')
# classmate('慧芳')
# classmate('猪猪')

#2.2默认参数：
#默认参数 是可以不传参数
#在不传参数的情况下，可以使用默认值；如果传了，就会使用传的值

#魔性的用法:
#注：默认参数尽量避免使用可变数据类型
# lst = []
# def func(l = lst):
#     l.append(l)
#     print(l)
#
# func([])
# func([])
# func([])
# func([])

#2.3动态参数
# def func(*args):#在参数前面加个*,这个参数就变成了动态参数
#     print(args)#使用时，所有接收过来的参数被组织成一个元组的形式。
#
# func(2, 4,[1,2,3,4],(4,5,6,7),'arg1')

# def func(a,b,c,*args,key='key'):
#     print(a, b, c)
#     print(key)
#     print(args)
#
# func(2,4,4,5,'asf',[1,3],key='zhoujielun')
# print()


# def func(a,key='key',*args,**kwargs):
#     print(kwargs)
# func(a=1, b=2, c=3)

# def func(a,*args,key='jayzhou',**kwargs):
#     print('a:',a)
#     print('args:',args)
#     print('key:',key)
#     print('kwargs:',kwargs)
#
# # func(5)
# # func(5,6,7)
# func(5,6,7,b='hahahha',c='heiheihei')


# def my_sum(*args):
#     sum_2 = 0
#     for i in args:
#         sum_2 += i
#     return sum_2
#
# ret = my_sum(1, 24, 5, 7)
# print(ret)
# ret2 = my_sum(24, 5, 7)
# print(ret2)

# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func(1,2,3,4,key='5')

# def my_sum(*args):  #聚合
#     sum_2 = 0
#     for i in args:
#         sum_2 += i
#     return sum_2
#
# l = [1, 24, 5, 7]
# # ret = my_sum(l[0],l[1],l[2],l[3])
# ret = my_sum(*l) #按顺序打散
# print(ret)

def func(**kwargs):
    print(kwargs)

# func(b=2, a=1)
dic = {'b': 2, 'a': 1}
func(**dic)
# print(**dic)

#总结:
#动态参数
#*args: 接收所有按照位置传递的参数，接收到的是参数组成的元组
#**kwargs:接收所有按照关键字传递的蚕食，接收到是参数组成的字典

#所有的参数的顺序：位置参数，*args,默认参数，**kwargs

#魔性的用法：
#在调用函数时，可以打散 *l, **dic




