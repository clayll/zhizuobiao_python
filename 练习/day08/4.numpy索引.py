#numpy中的元素索引：

#数组[索引]
#数组[行索引][列索引]
#数组[页索引][行索引][列索引]

#nmupy索引和python中的下标索引方法相似

import numpy as np

a = np.array([[[1, 2],[3, 4]],[[5, 6],[7, 8]]])

# print(a)
# print('*' * 120)
# print(a[0])
# print('*' * 120)
# print(a[0][0])
# print('*' * 120)
# print(a[0][0][0])


# for i in range(a.shape[0]):   #逐页
#     for j in range(a.shape[1]): #逐行
#         for k in range(a.shape[2]): #逐列
#             print(a[i][j][k])
#             # print(a[i, j, k])

