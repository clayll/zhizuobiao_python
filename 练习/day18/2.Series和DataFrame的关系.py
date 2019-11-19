import numpy as np
import pandas as pd
#Series和DataFrame的关系
s_1 = pd.Series([3,4,5])
s_2 = pd.Series([8,8,8])
df = pd.DataFrame()
df['a'] = s_1   #把Series当作行加入
df['b'] = s_2
s_3 = pd.Series({'a':9,'b':9})#注意索引匹配
#ignore_index忽略索引
df = df.append(s_3,ignore_index=True)   #把Series当作行加入
print(df)


#DataFrame增删改查操作
#增
pf = pd.DataFrame(np.arange(10,30).reshape(4,5),columns=['a','b','c','d','e'])
pf['f'] = [77,88,99,11] #增加或修改一列
pf.insert(2,'n',[66,66,66,66])#pf.insert(索引位置,'列名',[列元素信息])
#在指定的位置插入一列。

#删除列
pf.pop('n')
pf.drop('f',axis=1,inplace=True)


#修改列的名称
pf.columns = ['A','B','C','D','E']
pf.rename(columns={'E':'f','D':'x'},inplace=True)#列的改名


#修改行的索引
pf.rename(index={2:'y'},inplace=True)
print(pf)


