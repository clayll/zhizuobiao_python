#数据类型 可以分为可变和不可变
#不可变(可哈希)的数据类型:int, str, bool, tuple
#可变(不可哈希)的数据类型: list, dict, set

#字典
# D = {}
# print(type(D))

#字典分为键和值,通过键值对形式进行储存
#键Key: 不可变(可哈希)的数据类型，并且键是唯一的，不重复的。
#值Value；任意数据(int,str, bool,tuple,dict,list,set)

#1.创建字典的几种方式:
#方式1:
# dic = dict((('one',1),('two',2),('three',3)))
# print(dic)

#方式2:
# dic = dict(one=1,two=2,three=3)
# print(dic)

#方式3
# dic = dict({'one': 1, 'two': 2, 'three': 3})
# print(dic)

#方式4
# dic = dict(zip(['one','two','three'],[1, 2, 3]))
# print(dic)

#方式5 字典推导式
# dic = {k : v for k, v in [('one',1),('two',2),('three',3)]}
# print(dic)

#方式6 利用fromkey
# dic = dict.fromkeys('abcd',"python")
# print(dic)

#2. 验证字典的合法性
#合法的字典
# dic = {123: 456, True:999, "id":1,"name":'zhuzhu',"age":18,"stu":['a','b'],(1,2,3):"藤椒鸡"}
# print(dic)


#可变类型不能做字典的键
# dic = {[1,2,3]:456} #错的。。
# print(dic)

# dic = {{1:2}:"哈哈哈"}
# print(dic)

# dic = {{1, 2, 3}:"周杰伦"}
# print(dic)

#3.字典的常用操作
#增:
#通过键值对直接增加
# dic = {'name':'zhuzhu','age': 18}
# dic['weight'] = 82  #没有weight这个键，就直接增加键值对
# print(dic)

# dic['name'] = 'xinwei'
# print(dic) #如果已有键，譬如已有name这个键，就成了字典的改值


#setdefault
# dic = {'name':'zhuzhu','age': 18}
# # dic.setdefault('height',188)
# # print(dic)
#
# dic.setdefault('name','xinwei') #如果已有此键则不变
# print(dic)
#它有返回值
# dic = {'name':'zhuzhu','age': 18}
# ret = dic.setdefault('age')
# print(ret)

#删
#pop 通过key删除字典的键值对，有返回值，可设置返回值
# dic = {'name':'zhuzhu','age': 18}
# ret = dic.pop('name')
# print(ret) #zhuzhu
# ret1 = dic.pop('n',None) #设置返回值
# print(ret1,dic)

#popitem 3.6之后为删除最后一个，有返回值
# dic = {'name':'zhuzhu','age': 18}
# ret = dic.popitem()
# print(ret,dic)


#clear清空字典
# dic = {'name':'zhuzhu','age': 18}
# dic.clear()
# print(dic)

#del
#通过键删除键值对
# dic = {'name':'zhuzhu','age': 18}
# del dic['name']
# print(dic)

#del 删除整个字典
# del dic
# print(dic)

#改
#通过键值对直接改
# dic = {'name':'zhuzhu','age': 18}
# dic['name'] = 'barry'
# print(dic)

#update
# dic.update(sex='男',height=180)
# print(dic)

# dic.update([(1, 'a'),(2, 'b'), (3, 'c'), (4, 'd')])
# print(dic)

# dic1 = {"name":'wang', 'age':18, 'sex':'male'}
# dic2 = {"name":"barry", "weight":130}
# dic1.update(dic2)
#
# print(dic1)
# print(dic2)

#查
#通过键查询
# dic = {'name':'zhuzhu','age': 18}
# print(dic['name'])

#get
# v = dic.get('name')
# print(v)
# v = dic.get('name1')
# print(v) #None
# v = dic.get('name2','查无此键')
# print(v)


#keys()
# dic = {'name':'zhuzhu','age': 18}
# print(dic.keys())#dict_keys(['name', 'age'])

#values():
# dic = {'name':'zhuzhu','age': 18}
# print(dic.values()) #dict_values(['zhuzhu', 18])

#items()
# dic = {'name':'zhuzhu','age': 18}
# print(dic.items())#dict_items([('name', 'zhuzhu'), ('age', 18)])

#其他操作
# dic = {'name':'zhuzhu','age': 18}
# key_list = dic.keys()
# print(key_list)

#它可以循环打印
# dic = {'圣剑':'毛','哈哈':'见见','大圣剑':'概论'}
#
# for i in dic:
#     print(i)
#
# value_list = dic.values()
# # print(value_list)

# dic = {'圣剑':'毛','哈哈':'见见','大圣剑':'概论'}
# for i in dic.items():
#     print(i)


#拆包，也叫分别赋值

# a, b = 1, 2
# print(a, b)


# a, b = ('你好','世界') #这个专业名词就叫做元组的拆包
# print(a, b)
#
#
# a, b = ['你好','小飞龙']
# print(a, b)

# a, b = {'周杰伦':'龙卷风','kunkun':'真好'}
# print(a, b)


# dic = {'圣剑':'毛','哈哈':'见见','大圣剑':'概论'}
#
# for k,v in dic.items():
#     print('这是键',k)
#     print('这是值',v)

#回家作业
dic = {
    'name':'汪峰',
    'age':48,
    'wife':[{'name':'国际章','age':38}],
    'children':{'first_girl':'小苹果', 'sencond_girl':'小一','third_girl':'顶顶'}
}
#1.获取汪峰的名字
#2.获取这个字典{'name':'国际章','age':38}
#3.获取汪峰妻子的名字
#4.获取汪峰的第三个孩子的名字


