import numpy as np
import pandas as pd
cols = ['emp_id','emp_name','Q1','Q2','Q3','Q4']
data = [['emp001','tom',80,78,35,87],
        ['emp002','jerry',98,90,65],
        ['emp003','jim',78,34,29,81],
        ['emp004','peter',34,62,87,61]]
df = pd.DataFrame(data,columns=cols)
df['SUM'] = df['Q1'] + df['Q2'] + df['Q3'] + df['Q4']
df['AVG'] = df['SUM'] / 4


#数据清理：isnull/dropna/fillna/replace

# print(df.isnull())    #判断数据是否为NaN

# df.dropna(axis=0,inplace=True)    #删除NaN所在行
# df.dropna(axis=1,inplace=True)      #删除NaN所在列

df.fillna(0,inplace=True)#把NaN填充为0

df.replace(0,60,inplace=True)#替换

# print(df)

