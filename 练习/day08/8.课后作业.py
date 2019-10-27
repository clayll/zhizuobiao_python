#课后作业：
#要求同学们写出 这个结果如何得出的：

import numpy as np
a = np.array([[1,2],
              [0,1]])

b = np.array([[2,0],
              [3,4]])

#1.两个矩阵得乘积：
'''
答案是:[[8 8]
        [3 4]]

c = a.dot(b) 或者 a @b
'''


c = a @ b
print(c)














