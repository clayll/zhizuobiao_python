'try..except..'

# a = b
# print(a)
# print('tryexcept太难了!')

# try:
#     a = b
#     print(a)
# except:
#     print('出错了!')
#
# print('tryexcept太难了!')
'''
先执行try代码块，发现了错误
执行except代码块
程序往下执行
'''

# try:
#     print('错误发生之前')
#     a = b
#     print('错误发生之后')
#     print(a)
# except:
#     print('你又出错了')
#
# print('tryexcept太难了!')
#
# '''
# 先执行try,直到发现错误，不再执行异常之后的代码
# 执行except里的内容
# 向下继续
# '''
#

# try:
#     print('错误发生之前')
#     a = b
#     print('错误发生之后')
#     print(a)
# except:
#     print('你又出错了')
#
# print('tryexcept太难了!')

'''
先执行try,直到发现错误，不再执行异常之后的代码
执行except里的内容
向下继续
'''

try:
    print('错误发生之前')
    a = b
    print(a)
except SyntaxError:
    print('SyntaxError')
except SystemExit:
    print('NameError')
except:
    print('我啥都不知道！')

print('我太难了！')

#try except else 当有异常时，else就不会执行了;当没有异常时，执行else
# try:
#     b = 1
#     a = b
#     print(a)
# except SyntaxError:
#     print('SyntaxError')
# except SystemExit:
#     print('NameError')
# except:
#     print('我啥都不知道！')
# else:
#     print("没毛病了")
#
# print('我太难了！')

#try_finally:有错误时，先执行finally语句，再执行try语句，然后再报错


# try:
#     a = b
#     print(a)
# finally:
#     print("我会处理的")
#
# print('我太难了！')

