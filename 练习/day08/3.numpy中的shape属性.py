import numpy as np

#shape属性：
#shape属性的值是一个元组类型，一个元组内包含多个元素，分别是从高到底表示每个维度的数。
#页 行 列
#numpy中三维的优先级:
#页：最高级
#行：次之
#列：最低


#arange和array都可以创建数组，有时可以混用。

#用shape属性可以看到维度。
#numpy中多使用二维数组，三维很少见。
# print(i.shape) #(2, 3, 4)  生成了三维数组，2页，3行，4列


i = np.array([
    [np.arange(1,5),np.arange(5,9),np.arange(9,13)],
    [np.arange(13, 17), np.arange(17, 21), np.arange(21, 25)]
])
print(i)
print(i.shape) #(2, 3, 4)  生成了三维数组，2页，3行，4列

