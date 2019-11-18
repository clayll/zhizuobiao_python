'''
"." 在普通模式，它匹配除换行符外的任意一个字符。

"^" 表示匹配一个字符串的开始。
"$" 匹配一个字符串的结尾或者字串最后面的换行符。

'''

import re
# a = re.findall('(foo.$)','foo1\nfoo2\n')
# print(a) #['foo2']

# a = re.findall('($)','foo\n')
# print(a)#['', '']
#如果用一个$去搜索'foo\n'，直接找到两个空的匹配：一个是最后最后的换行符，另一个是字符串的结尾


'''
"*" 指定将前面的RE重复0次或者任意多次，而且总是试图尽量多地匹配
"+" 指定将前面的RE重复1次或者任意多次，而且总是试图尽量多地匹配
"?" 指定将前面的RE重复0次或者1次。如果有的话，也尽量匹配1次。
*?  +?  ??
*，+，？都是贪婪的。
可以在后面加个问号，将RE策略改为非贪婪，只匹配尽量少的RE
'''
# b = re.findall('<.*>','<H1>title</H1>')
# print(b)#['<H1>title</H1>']

# b = re.findall('<.*?>','<H1>title</H1>')
# print(b)

'''
{m} 是一个数字，指定将前面的RE重复m次
{m,n} m,n都是数字，指定将前面的RE重复m到n次。
例如：a{3,5}：匹配3到5个连续的a。
注：如果省略m，将匹配到0到n个前面RE；
如果省略n，将匹配n到无穷多个前面的RE。
{m,n}?  非贪婪
'\' 转义特殊字符
'[]' 用于指定一个字符的集合[a-zA-Z0-9]
'|' 管道符号,A和B是任意的RE
'(...)' 匹配括号里的RE匹配的内容，并指定组的开始和结束位置。
'(?...)' 这是一个表达式的扩展字符。'?'后的第一个字母决定了整个表达式的语法和含义。
例：?P<year>
'(?P<name>)' 和圆括号类似，但是子串匹配的内容将可以用命名的name参数来提取。、
\w 等价于[a-zA-Z0-9]
(?P=name) 匹配之前以name命名的组里的内容
'''
m = re.match('(?P<var>\w*)','abc=123')
# print(m.group('var'))
print(m.group(0))

#组的name必须是有效的python标识符，而且在本表达式内不重名。命名了的组和普通组一样，也可以用数字来提取。
#也就是说名字是个额外的属性。








