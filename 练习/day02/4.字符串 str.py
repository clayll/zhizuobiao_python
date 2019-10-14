#凡是有引号的都是字符串，可单引号，可双引号，还可以三引号
# s1 = '猪猪nb'
# print(s1,type(s1))

#4.1字符串的索引和切片
#从左至右依次: 0, 1, 2, ……

#4.1.1索引即下标，就是字符串组成的元素从第一个开始，初始索引为0，以此类推。
# s1 = 'ABCDEFGHIJK'
# print(s1[0])
# print(s1[3])
# print(s1[5])

#4.1.2 切片
#切片就是通过索引(索引:索引:步长)截取字符串的一段，形成新的字符串
#注意：原则是顾头不顾腚
s1 = 'ABCDEFGHIJK'
# print(s1[0:3])
#从头开始的取0的部分默认可以不写
# print(s1[:3])   #ABC
# print(s1[2:5])  #CDE
# print(s1[:]) #默认到最后
# print(s1[:-1])
#-1 是列表中最后一个元素的索引，但是还是要满足顾头不顾腚的原则，所以取不到K元素
#加上步长
# print(s1[:5:2]) #第一步先切出ABCDE，因为步长2，所以A C E被切出
# print(s1[-1:-5:-2]) #先切出HIJK，然后-2反向步长，K I 被切出
#反向加步长

#4.1.3字符串常用方法
#字符串除了切片，还有其他一些操作
#数 字符串中的元素出现的个数：

# a = 'aaaddccca'
# ret1 = a.count("a",0,5) #可切片
# print(ret1)

# a1 = "dkfjdkfasf54"
# #startswith 判断是否以...开头
# #endswith 判断是否以...结尾
# ret2 = a1.endswith('jdk',0,2)
# print(ret2)#返回是布尔值
# ret3 = a1.startswith('kfj',1,4)
# print(ret3)

#spilt，以什么分割，最后形成一个列表，此列表不含有这个分割的元素。
# ret4 = 'title, Tilte, atre,'.split('t')
# print(ret4) #['', 'i', 'le, Til', 'e, a', 're,']

# ret5 = 'title, Tilte, atre,'.rsplit('t',1)
# print(ret5)
#rsplit是从右边起分割,后面跟的数字，代表切几个

#format格式化占位符的三种玩法
#按位置传入
# res = '{}{}{}'.format('靓靓',18,'male')

#按下标索引传入
# res = '{2}{2}{2}'.format('靓靓',18,'male')

#按关键字传入
# res = '{name}{age}{sex}'.format(sex='male',name='靓靓',age=18)
# print(res)

#strip
# name = '*eddie******'
# print(name.strip('*'))
# print(name.lstrip('*'))
# print(name.rstrip('*'))

#replace替换
# name = 'xianxian say: i have one tesla, my name is xianxian'
# print(name)
# print(name.replace('xianxian','huihui',2))

######is 系列
## .isxxx()全是返回布尔值的
name = 'xinwei123'
# print(name.isalnum()) #al=alphabet,num=number 字符串由字母或数字组成
# print(name.isalpha()) #字符串只由字母组成
# print(name.isdecimal()) #字符串只由十进制组成

a2 = 'dkfjdkfasf54'
#寻找字符串中的元素是否存在
# ret = a2.find('fjdk',1,6)
# print(ret)#返回找到元素的索引，如果找不到返回-1

# ret = a2.index('fjdk',4,6)
# print(ret) #返回找到的元素的索引，找不到就报错

#captalize,swapcase,title
# name = 'eddieZhu'
# print(name.capitalize()) #首字母大写
# print(name.swapcase())#大小写翻转
# msg = 'zhuzhu say hi'
# print(msg.title()) #每个单词的首字母大写

#内同居中，总长度，空白处填充
# a1 = "dkfjdkfasf54"
# ret2 = a1.center(20,'*')
# print(ret2)









