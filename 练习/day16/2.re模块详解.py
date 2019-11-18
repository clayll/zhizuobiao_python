import re
'''
re.findall()
re.finditer()
re.search()
re.match()
re.split()
re.sub()
re.subn()
'''
#1.re.findall()
# ret = re.findall(r'\d',r'liangliang666 zhuzhu huihui')#返回所有满足匹配条件的结果，放在列表里
# print(ret)

#2.re.search()
#search从左至右依次找，找到一个就回来，需要使用group()获取返回值
#如果re.search找不到，就返回None，使用group()会报错
# ret = re.search('a','eva apple abc')
# # print(ret)
# if ret:
#     print(ret.group())


#3.re.match
#match从头开始匹配，匹配上了需要使用group来获取返回值
#匹配不上就返回None，使用group会报错
# ret = re.match('a','bva apple abc')
# print(ret.group())


#4.re.split
# c = 'a,b'.split(',')
# print(c)

#以下面例子为例：先按'a'分割得到'' +  'bcd'; 再对''+'bcd'分别按'b'分割
# ret = re.split('[ab]','abcd')
# print(ret)#['', '', 'cd']

#5.re.sub
#以下面例子为例:'\d'(pattern)去字符串里匹配数字,'H'代表要替换的内容,数字3，代表替换3个
#re.sub(pattern,要替换的内容,string, 替换几个)
# ret = re.sub('\d','H','liangliang6huihui9zhuzhu8',2)
# print(ret)

#6.re.subn
#将数字全部替换成'H'，返回元组(替换的内容,替换了几次)
# ret = re.subn('\d','H','liangliang6huihui9zhuzhu8')
# print(ret) #('liangliangHhuihuiHzhuzhuH', 3)

#7.re.finditer
ret = re.finditer('\d','da3sy4784a')
#re.finditer返回一个存放匹配结果的迭代器对象
# print(ret)
# for i in ret:
#     print(i.group())
print(next(ret).group())#查看第一个结果
print(next(ret).group())#查看第二个结果
# print(next(ret).group())  ：
# print(next(ret).group())  ：
# print(next(ret).group()) ：
# print(next(ret).group()) ：
#列表推导式写法
# print([i.group() for i in ret])#查看剩余的结果，放在列表中

#findall
#search
#match
#sub/subn
#compile
#finditer


#回家作业
#1.
express = '1 - 2 * ((60 - 30 + (-40/5) * (9-3.33 + 198/4*2998 +10*568/14))-(-4*3)/(16-3*2))'
#正则表达式
#0.去掉表达式中的所有空格
#1.从表达式中匹配出所有的()里面不再有小括号的表达式

#2.从表达式9-2*5/3 + 7/3*99/4*2998+10*568/14中匹配出第一个乘法或者除法




