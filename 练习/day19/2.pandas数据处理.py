#数据处理  reindex、Sort和Groupby
import numpy as np
import pandas as pd
cols = ['emp_id','emp_name','Q1','Q2','Q3','Q4']
data = [['emp001','tom',80,78,35,87],
        ['emp002','jerry',98,90,65,83],
        ['emp003','jim',78,34,29,81],
        ['emp004','peter',34,62,87,61]]
df = pd.DataFrame(data,columns=cols)
df['SUM'] = df['Q1'] + df['Q2'] + df['Q3'] + df['Q4']
df['AVG'] = df['SUM'] / 4

x = df.pivot(index='emp_id',columns='emp_name',values="Q1")
print(x)

#reindex可以指定查看索引及其顺序
# t = df.reindex([3, 1, 0],axis=0)

t = df.reindex(['emp_name','AVG','SUM'],axis=1)
# print(t)
#排序
# df.sort_values('Q4',ascending=False,inplace=True)
# df.sort_values(['AVG','Q4'],ascending=[True,False],inplace=True)#可以对多列进行排序，可以自定义升降序

# df.sort_index(inplace=True)#对索引进行排序



df = pd.read_csv('cloth.csv',sep=',')
print(df)
gp= df.groupby('name')

# gp = df.groupby('name')

#gp.sum()得到每个分组数值列的合计
# print(gp.sum().sort_values('cost',ascending=False))



# gp = df.groupby(['brand','name'])
# print(gp.sum())

# gp = df.groupby('brand')
# print(gp.size())#得到分组的记录条数

#




