#集合set(用的少)
#集合是无序的，不重复的数据集合。
#它里面元素可以是不可变类型，但是它本身却是可变类型。

#作用：1.去重 2.关系测试，测试两组数据之间的交集，差集和并集等关系

#1.集合的创建
# set1 = set([1, 2, 'barry'])
# print(set1)

#2.集合的增
# set1 = {'xianxian','liangliang','panpan','yuyu'}
# set1.add('女神')
# print(set1)

#update 迭代着增加
# set1.update('A')
# print(set1)

# set1.update('仓老师')
# print(set1)

# set1.update([1, 2, 3])
# print(set1)

#3.集合的删
set1 = {'xianxian','liangliang','panpan','yuyu'}

# set1.remove('yuyu')
# print(set1)#删除一个元素

# set1.pop()#随机删除一个元素
# print(set1)

# set1.clear() #清空集合
# print(set1)

# del set1 #删除集合
# print(set1)


#集合的其他操作:
#交集 (& 或者 intersection)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1 & set2)  #{4, 5}
print(set1.intersection(set2)) #{4, 5}

#并集  (| 或者 union)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 | set2) #{1, 2, 3, 4, 5, 6, 7, 8}
print(set2.union(set1))#{1, 2, 3, 4, 5, 6, 7, 8}

#差集   (- 或者 difference)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# print(  set1 - set2 ) #{1, 2, 3}
# print( set1.difference(set2) )#{1, 2, 3}

#反交集 (^ 或者 symmetric_difference)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# print( set1 ^ set2 )#{1, 2, 3, 6, 7, 8}
# print(set1.symmetric_difference(set2)) #{1, 2, 3, 6, 7, 8}

#子集和超集

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}

print(set1 < set2)
print(set1.issubset(set2))  #说明set1 是set2的子集


print(set2 > set1)
print(set2.issuperset(set1)) #说明set2 是 set1 的超集


#frozenset 不可变集合，让集合变成不可变类型

s = frozenset('barry')
print(s, type(s))
