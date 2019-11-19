#正则表达式匹配中,(.)和(.?)匹配区别
#(.)是贪婪匹配 尽可能多的往后匹配
#(.?)非贪婪匹配 尽可能少匹配

# import re
# #2. 正则匹配，匹配日期2018-03-20			（2分）
# url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
# ret = re.findall(r'dateRange=(.*?)%7C(.*?)&',url)
# print(ret)

# (.*?)

#举例说明 zip()函数用法
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [4, 5, 6, 7, 8]
#
# zipped = list(zip(a, b))  #zip函数打包成元组
#
# print(zipped)
# for i in zipped:
#     print(i)

# zipped2 = list(zip(a, c))
# print(zipped2)  #元素个数与最短的列表一致
# print(list(zip(*zipped)))   #与zip相反，*zipped可以理解为解压，返回二维矩阵

#4.生成0-100的随机数
# import random
# for i in range(0, 100):
#     n = random.randint(0, 100)
#     print(n)

#*args **kwargs
# def func1(a,*args):
#     print("a",a)
#     for x in args:
#         print("arg:",x)
#
# func1(2,3,5,4)

# def func1(a,**kwargs):
#     print("a",a)
#     for key in kwargs:
#         print("%s:%s"%(key,kwargs[key]))
#
# func1(b=2,a=1)

# 2. 编程题(4分)
# 模拟斗地主发牌, 扑克牌共54张
# 三个人一起玩,每个人发17张,底牌三张
# 牌的种类:
# 黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665'), 红桃('\u2666')
# 数字:
# A2~10JQK
# 大小王
#   要求,输入回车,打印第1个人的17张牌
#   再回车,打印第2个人的17张牌
#   再回车,打印第3个人的17张牌
#   再回车,打印三张底牌

# from random import shuffle
#
# #扑克的花色
# kinds = ['\u2660','\u2663','\u2665','\u2666']
# numbers = ['A'] + [ str(x) for x in range(2,11)] + ['J','Q','K']
# jokers = ['大王','小王']
#
# pocker = [ x + y for x in kinds for y in numbers]
# pocker += jokers
#
# #洗牌
# shuffle(pocker)
#
# #发牌
# input('打印第一人的牌:')
# print(pocker[:17])
# input('打印第二人的牌:')
# print(pocker[17:34])
# input('打印第三人的牌:')
# print(pocker[34:51])
# input('打印底牌:')
# print(pocker[51:])

#回家作业
#题1.(2分)
express = '1 - 2 * ((60 - 30 + (-40/5) * (9-3.33 + 198/4*2998 +10*568/14))-(-4*3)/(16-3*2))'
#正则表达式
#0.去掉表达式中的所有空格
#1.从表达式中匹配出所有的()里面小括号的内容表达式
import re
# pattern = re.compile(r' ')
# print(pattern.sub('',express))
# pattern = re.compile(r'[()]')
# print(pattern.sub('',express))

# a = re.findall(r'\((.*?)\)',express)
# a = re.findall(r'(?<=\()[^()]*(?=\))',express)
# print(a)


#题2.从表达式9-2*5/3 + 7/3*99/4*2998+10*568/14中匹配出第一个乘法或者除法(2分)

# a = '9-2*5/3 + 7/3*99/4*2998+10*568/14'
#
# ret1 = re.search(r"\d+(\*|\/)\d+",a)
# print(ret1.group())
# ret2 = re.search(r"\d+(\/)\d+",a)
# print(ret2.group())

# str = u'周杰伦演唱(龙泉)、(龙卷风)、(霍元甲)'
# print(re.findall('\((.*?)\)',str))


