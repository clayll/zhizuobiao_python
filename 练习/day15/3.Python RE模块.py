'''
python中自带re模块，它提供了对正则表达式的支持
re.compile(string[,flag])

re.match(pattern, string[, flags])  从开头开始匹配，返回开始的匹配第一个，不符合就返回None
属性：
string:匹配时使用的文本
re:匹配时使用的Pattern对象
pos:文本中正则表达式开始搜索的索引
endpos:文本中正则表达式结束搜索的索引
lastindex:最后一个被捕获的分组在文本中的索引。如果没有捕获，返回None
lastgroup:最后一个被捕获的分组的别名。 如果这个分组没有别名或者没有被捕获的分组，将为None


re.search(pattern, string[, flags])  查找整个字符串，返回匹配的第一个
re.split(pattern, string[, maxsplit])
re.findall(pattern, string[, flags])
re.finditer(pattern, string[, flags])
re.sub(pattern, repl, string[, count])
re.subn(pattern, repl, string[, count])

'''

# import re
#pattern的概念：一个匹配的模式：re.compile()
# pattern = re.compile(r'hello')

'''
flag参数：匹配模式，取值可以使用按位或运算符’|’表示同时生效，比如re.I | re.M。可选值有：
	（1）re.I(全拼：IGNORECASE): 忽略大小写
 	（2）re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为
 	（3）re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
 	（4）re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
 	（5）re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
	（6）re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
'''
#下面介绍其中方法，flags同样是代表匹配模式。如果在pattern生成时已经指明了flags，那么下面的方法中就不传入这个参数了。

#1. re.match(pattern, string[, flags]) :一次匹配的结果，包含很多关于此次匹配的信息。


# import re
# #将正则表达式编译成pattern对象。注：hello前面r的意思时“原生字符串”
# pattern = re.compile(r'hello')
#
# #使用re.match匹配文本，获得匹配结果，无法匹配则会返回None
# ret1 = re.match(pattern,'hello')#从头到尾完全匹配，匹配成功
# ret2 = re.match(pattern,'helloo world')#匹配完hello之后的o不再匹配。返回匹配成功的信息
# ret3 = re.match(pattern,'helo world')#无法匹配完成，返回None
# ret4 = re.match(pattern,'hello world')#和第二个同理
#
# if ret1:
#     #使用match获得分组信息
#     print(ret1.group())
# else:
#     print('1匹配失败')
#
# if ret2:
#     #使用match获得分组信息
#     print(ret2.group())
# else:
#     print('2匹配失败')
#
# if ret3:
#     #使用match获得分组信息
#     print(ret3.group())
# else:
#     print('3匹配失败')
#
# if ret4:
#     #使用match获得分组信息
#     print(ret4.group())
# else:
#     print('4匹配失败')

#例2

import re
#
# m = re.match(r'(\w+)(\w+)','h1 331')
# # print(m.group())
#
#
# m = re.search(r'(\w+)(\w+)','h1 331')
# # print(m)
#
#
#
m = re.search(r'(\w+)\s(\w+)','h1 331')
print(m.group())
#
# m = re.findall(r'(\w+)','h1 331')
# print(m)


# 正则式中的每个组都有一个序号，它是按定义时从左到右的顺序从 1 开始编号的。其实， re 的正则式还有一个 0 号组，它就是整个正则式本身。
import re
patten = re.compile(r"(?P<name>[a-z]+)\s(?P<age>[\d]+)\s(?P<tel>[\d]+)")
print(patten.groupindex)
print(patten.groups)
s = "Tom 24 88888888  <="
rs = re.search(patten,s)
print(rs)
print(rs.group())


p1 = re.compile(r"(.?)")
s = "1231231"
print(re.match(p1,s))

#span([group])
#返回(start(group),end(group))

#
# print(m.string)
# print(m.re)
# print(m.pos)
# print(m.endpos)
# print(m.lastindex)
# print(m.lastgroup)

#2.re.search(pattern, string[, flags])
#和match的区别在于match()函数只检测re是不是在string开始的位置，search()会扫描整个string查找匹配。
#match()只有在0的位置匹配成功才返回；反之，返回None。
#
# import re
#
# pattern = re.compile(r'world')
#
# search = re.search(pattern,'hello world')
# print(search)
#
# match = re.match(pattern,'hello world')
# print(match)


# if match:
#     print(match.group())



