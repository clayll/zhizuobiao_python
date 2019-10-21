#1. 函数range(1,1,1)的值是_______。
# print(list(range(1,1,1))) #[]

#math模块
#  写一个程序利用海伦公式计算三角形的面积。要求：
# 1）三角形的三条边从键盘录入
# 2）要求做边的非法判断（两边之和大于第三边）
# 3）输出最后的面积
# import math
# a, b, c = map(float, input('请输入三边的长度,以空格分隔:').split())
#
# if a + b < c or a + c < b or b + c< a:
#     print('输入的边无法构成三角形，请重新输入')
# else:
#     s =  (a + b + c)/2
#     # S = (s*(s-a)*(s-b)*(s-c))**0.5
#     S = math.sqrt(s*(s-a)*(s-b)*(s-c))
#     print('面积为:%1.3f'%S)

#4.列表推导式把单词大写变成小写
# s = input('请输入单词:')
#
# L = [i.lower() for i in s]
# print(L) #['a', 'p', 'p', 'l', 'e']

# year = int(input("请输入一个年份:"))
# if year == 0:
#     print('您输入的不是年份')
# else:
#     newyear11 = year
#     i10 = [newyear11 + 1,newyear11 + 2,newyear11 + 3,newyear11 + 4]
#     if i10.count(0) == 1:
#         i10.remove(0)
#         i1 = i10
#     else:
#         i1 = i10
#     for newyear1 in i1:
#         if newyear1 % 4 == 0 and newyear1 % 100 != 0 or newyear1 % 400 == 0:
#             break
#
#     newyear22 = year
#     i20 = [newyear22 - 1,newyear22 - 2,newyear22 - 3,newyear22 - 4]
#     if i20.count(0) == 1:
#         i20.remove(0)
#         i2 = i20
#     else:
#         i2 = i20
#     for newyear2 in i2:
#         if newyear2 % 4 == 0 and newyear2 % 100 != 0 or newyear2 % 400 == 0:
#             break
#
#     z1 = newyear1 - year
#     z2 = year - newyear2
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("{}年是闰年".format(year))
#     elif abs(z1) > abs(z2):
#         print('%d年不是闰年，离%d年最近的闰年是%d年' % (year, year, newyear2))
#     elif abs(z1) < abs(z2):
#         print('%d年不是闰年，离%d年最近的闰年是%d年' % (year, year, newyear1))
#     else:
#         print('%d年不是闰年，离%d年最近的闰年是%d年和%d年' % (year, year, newyear1, newyear2))
#
