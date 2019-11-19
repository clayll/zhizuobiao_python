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

#查询平均业绩小于60的员工
# print(df.query('AVG<60'))
# print(df[df.AVG < 60])
# df.loc[df.AVG<60,'emp_name'] += '*'
# df.query('AVG<60').emp_name += '*'
# x = df.query('AVG<60')
# df.loc[x.index,'emp_name'] += '*'#在业绩小于60的员工后加*
#
# df.drop(x.index,axis=0,inplace=True)#删除业绩小于60的员工

df.loc[df.emp_name=='jim','Q2'] = 90    #修改姓名为jim的第二季度的业绩
print(df)
