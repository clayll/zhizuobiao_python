#正则是一种处理文字的规则
#re模块 -python使用正则 import re
# 它只是我们使用python去操作一些问题的工具而已。

#18939905107
#是数字
#11位
#以13|15|17|18|16|14 卡头

# num = input("phone_number:")
# if num.isdigit() and len(num) == 11 and num.startswith('13') or\
#         num.startswith('14') or \
#         num.startswith('15') or \
#         num.startswith('17') or \
#         num.startswith('18'):
#     print('这是一个格式正确的电话号码')
# else:
#     print('您的输入有误!')

import re
num = input("please input your phone number:")
if re.match('^(13|15|17|18|16|14)[0-9]{9}$',num):
    print('这是一个合法的手机号')
else:
    print('这是不合法的手机号码')

'''
需要大家记一下：两大类
[字符组] ：表示在一个字符的位置可以出现的所有情况的集合就是一个字符组

#1.表示数字的字符组
[13456782]
[0123456789]
简写的写法：必须由小到大
[0-9]
[2-8]

#2.表示字母的字符组
[abcd]
简写的写法：
[a-z]
[A-Z]

#表示匹配任意字符 :[\w\W][\d\D][\s\S]

#正则匹配： 字符  量词 非贪婪标志
    #字符: 字符、字符组、元字符 表示一个字符位置上出现的内容

#身份证号：
#15： 首位不能为零，由数字组成
#18：首位不能为零，前17位是数字，最后一位可以是数字或者X。
'''

