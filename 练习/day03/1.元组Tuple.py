#元组
#因为list列表可变容器，有不安全的情况。所以元组产生了。

#1.元组的索引切片
# tu1 = ('a','b','fengfeng', 3, 666)
# print(tu1,type(tu1))
# print(tu1[0])
# print(tu1[-1])
# print(tu1[1:3])
# print(tu1[:-1])
# print(tu1[::2])
# print(tu1[::-1]) #步长为-1就是反转

#2.元组的其他一些用法
#2.1可以利用for循环查询

# tu1 = ('a','b','fengfeng', 3, 666)
# for i in tu1:
#     print(i)

#2.2 index:通过元素查找索引(可切片),找到第一个元素就返回，找不到即报错。

# tu = ('fengfeng',[1, 2, 3],'fengjuan','qianqian')
# print(tu.index('qianqian'))


#2.3 count 获取某元素在元组中出现的次数
# tu = ('fengfeng','zhuzhu','zhuzhu','fengjuan','zhuzhu','zhuzhu')
# print(tu.count('zhuzhu'))

#2.4 len
# tu1 = (1, 2, 3, 4, 84, 5, 2, 8, 9, 11, 2)
# print(len(tu1))

# tu1 = (1,)
# print(tu1)













