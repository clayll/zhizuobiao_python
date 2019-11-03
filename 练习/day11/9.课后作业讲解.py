# 1.表达式eval("4 * 2 + 5 % 2 + 4/3")的结果是_______。

# print(eval("4 * 2 + 5 % 2 + 4/3"))
'''
eval()函数用来执行一个字符串表达式，并且返回表达式的值
语法:eval(expression,globals,locals)
expression 表达式
globals 变量作用域，全局命名空间。如果被提供，则必须是一个字典对象
locals 变量作用域，局部命名空间。如果被提供，可以是任何映射对象
返回值：返回表达式计算结果
'''
#
# x =10
# a = eval('3 + x')
# print(a)
#
# b = eval('pow(2,2)')
# print(b)

# n = 81
# print(eval("n + 4"))


#2.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。
# 请问第五个人多大？(递归算法计算)
'''
递归：
在一个函数里调用自己。
'''

# def age(n):
#     if n == 1:
#         return 10
#     else:
#         return 2 + age(n - 1)
#
# print(age(5))

#4:  2
# 3: 2 +2
#2:  2 + 2 + 2
# 1： 2 + 2 + 2 +2 +10 =18

#3.闭包：
#内部函数引用外部函数的变量，再从内部函数返回一个值到全局

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print (l)
# f(2)
# f(3,[3,2,1])
#
# f(3)




#实现斐波那契数列
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
# def inputdigit():
#     num = int(input('请输入数字:'))
#     for i in range(1, num+1):
#         print(fibo(i), end=' ')
#     return num
#
# while True:
#     if inputdigit() == 0:
#         print('退出')
#         break

def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

for i in range(5):
    print(fibo(i),end=' ')



# num = int(input("请输入数字:"))
#
# for i in range(1,num+1):
#     print(fibo(i), end=' ')






