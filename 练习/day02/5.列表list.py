# L = []
# print(type(L))

#5.1 列表的创建（三种方式）
#方式一:(常用)
# l1 = [1, 2, '猪猪']

#方式二: (不常用)
# l1 = list() #空列表
# l1 = list('123')
# print(l1) #返回：['1', '2', '3'] ; list('x')中'x'为可迭代对象
# l1 = list('abc')
# print(l1)

#方式三：列表推导式(后面会讲到)
# l1 = [ i for i in range(1, 5)]
# print(l1) #[1, 2, 3, 4]

#5.2 列表的切片索引 (同字符串切片索引)
l1 = ['a','b','慧慧', 3, 666]
print(l1[0]) #
print(l1[-1]) #666
print(l1[1:3]) #['b', '慧慧']
print(l1[:-1]) #['a', 'b', '慧慧', 3]
print(l1[::2]) #['a', '慧慧', 666]
print(l1[::-1])#[666, 3, '慧慧', 'b', 'a'],[::-1]只是做翻转


#通过li列表可以切出新的列表
# li = [1, 3, 2, 'a', 4, 'b', 5, 'c']
# l1 = li[:3]
# print(l1) #[1, 3, 2]
#
#
# #5.3列表的增删改查
# #增
# #append 追加，给列表最后面追加一个元素
# # l = [1, 2, 'a']
# # l.append(999)
# # print(l)
#
# #insert 插入，在列表任意位置插入元素
# # l = [1, 2, 'a']
# # l.insert(2,'猪猪')
# # print(l)
#
# #extend 迭代着追加，在列表的最后面迭代着追加一组数据
# l = [1, 2, 'a']
# # l.extend('bbb a')
# l.extend('345')
# print(l)

#删
#pop 通过索引删除列表中对应的元素，该方法有返回值，返回值为删除的元素
# l = ['zhuzhu','huihui','xianxian','liangliang']
# ret = l.pop(1) #获取返回值
# print(ret,l)

# remove 通过元素删除列表中的该元素
# l = ['zhuzhu','huihui','xianxian','liangliang']
# l.remove('zhuzhu')
# print(l) #['huihui', 'xianxian', 'liangliang']

#clear 清空列表
# l = ['zhuzhu','huihui','xianxian','liangliang']
# l.clear()
# print(l) #[]

#del
#按照索引删除该元素
# l = ['zhuzhu','huihui','xianxian','liangliang']
# del l[2]
# print(l) #['zhuzhu', 'huihui', 'liangliang']

#切片删除该元素
# l = ['zhuzhu','huihui','xianxian','liangliang']
# del l[1:]
# print(l)

#切片（步长）删除该元素
l = ['zhuzhu','huihui','xianxian','liangliang']
del l[::2]
print(l) #['huihui', 'liangliang']

#改
#按照索引改值
# l = ['zhuzhu','huihui','xianxian','liangliang']
# l[0] = 'fengjuan'
# print(l) #['fengjuan', 'huihui', 'xianxian', 'liangliang']

#按照切片改值(迭代着增加)
# l = ['zhuzhu','huihui','xianxian','liangliang']
# l[1:3] = 'abcdefg'
# print(l)#['zhuzhu', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'liangliang']

#按照切片（步长）改值 (必须一一对应)

l = ['zhuzhu','huihui','xianxian','liangliang']
l[::2] = '男女'
print(l)

#查
#切片取查，或者循环去查

#列表其他操作
#count(数) (方法统计某个元素在列表中出现的次数)
#index
#sort
#reverse
#列表可以相加与整数相乘
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l1 + l2) #[1, 2, 3, 4, 5, 6]
# print(l1*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#列表的嵌套
# l1 = [1, 2, 3, 4, [5, 6, 7, 8]]
# print(l1)

#5.4深拷贝和浅拷贝
#浅拷贝 , 只拷贝一层，只拷贝外层，原列表内层嵌套列表发生改变，浅拷贝的对象也会改变
import copy

l1 = [1, 2, 3, 4, [5, 6, 7, 8]]

l2 = copy.copy(l1)

l1[1] = 10
# l1[4][0] = 9

print(l1)
print(l2)

#深拷贝,完全的拷贝，内外层都拷贝
# l1 = [1, 2, 3, 4, [5, 6, 7, 8]]
# l2 = copy.deepcopy(l1)
#
# l1[4][0] = 9
#
# print(l1)
# print(l2)



#5.5列表其他操作
# count（数）（方法统计某个元素在列表中出现的次数）。
a = ["q","w","q","r","t","y"]
print(a.count("q"))
# index（方法用于从列表中找出某个值第一个匹配项的索引位置）
a = ["q","w","r","t","y"]
print(a.index("r"))


# 排序：
# sort （方法用于在原位置对列表进行排序）。
#  reverse （方法将列表中的元素反向存放）。
a = [2,1,3,4,5]
a.sort()# 没有返回值，所以只能打印a
print(a)
a.reverse()#也没有返回值，所以只能打印a
print(a)
del(a[2])
print(a[:])




