import numpy as np
import pandas as pd
import xlrd
import xlwt


# df = pd.read_excel('data.xlsx',sheet_name='sales1')#sheet_name要读取的表单

# print(pd.pivot_table(df,index=['Manager','Rep'],values=['Money','Quantity'],aggfunc=[np.sum]))
#
# x = pd.pivot_table(df,index=['Manager','Rep'],columns=['Product'],values=['Money','Quantity'],aggfunc=[np.sum])

# print(x.fillna(0))


df = pd.read_excel('data.xlsx',sheet_name='sales2')

# print(df['Q1'].std())#max()/min()/mean()/std()

x = df.loc[:,'Q1':'Q4'].T
# print(x.std())
# print(x)
x.std()
# df['STD'] = x.std() #手工添加列

df['STD'] = np.around(x.std(),decimals=2) #统计每个员工四个季度的标准差

print(df)


#存储文件

# df.to_csv('std_sales.csv')
df.to_excel('std_sales.xls')
print(df)













