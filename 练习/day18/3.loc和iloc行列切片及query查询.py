import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(10,30).reshape(4,5),columns=['A','B','C','D','E'])

# print(df['A'])  #取得A列

# print(df[['A','C','E']])    #取得指定的列

# print(df.loc[:,'A':'B'])    #loc是按照名称切片

# print(df.iloc[:,-2:])   #iloc是按照位置切片

df.index = ['p1','p2','p3','p4']
# print(df)
# print(df.loc['p1':'p2'])
# print(df.iloc[:2])
# print(df.head(1)) #查询前几行
# print(df.tail(1))#查询后几行

#query
products = pd.DataFrame({'p_id':['p001','p002','p003','p004'],
                         'price':[3000,2000,50,500],
                         'region':['us','cn','us','cn']})

# print(products.query('price>1000 and price<3000'))
m = 1000
n = 2500

#加query查询条件若为变量，前须加@
# print(products.query('price>@m and price<@n'))#查询条件
# print(products.query(("region =='cn'")))
print(products[products.price<1000])    #另一种写法




