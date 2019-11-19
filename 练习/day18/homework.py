import pandas as pd
import numpy as  np
#
# s = pd.Series((1,2,3),index=("a","b","c"))
# s2 = pd.Series((4,5,6),index=("a","b","c"))
# df = pd.DataFrame()
# df['a'] = s
# df['b'] = s2
# df.insert(0,'z',(4,56,7))
# print(df)
# # df.drop('c',axis=1,inplace=True)
# # print(df)
# df.columns = ["A","B","C"]
#
# df.rename(index = {"a":1,"b":2,"c":3},inplace=True)
# print(df)



data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 1.	创建索引为labels的数据框df
df = pd.DataFrame(data=data,index=labels)
print(df)
#
# 2.	返回df的前三行
q2 = df.iloc[:3]
# print(q2)
# 3.	返回df的最后两行
q3 = df.tail(2)
# print(q3)
# 4.	只选择 'animal' 和'age' 列
# q4 = df.loc[:,['animal','age']]
q4 = df[['animal','age']]
# print(q4)

#
# 5.	选择['animal', 'age']的 [3, 4, 8]行
q5 = df.loc[['c','d','i'],['animal','age']]
# print(q5)
#
# 6.	选择visits大于 2的数据
q6 = df[df.visits>2]
q6 = df.query('visits>2')
# print(q6)
#
# 7.	选择 animal 是cat和age小于3.
q7 = df.query("animal=='cat' and age < 3 ")

# print(q7)
# 8.	选择 age is between 2 and 4 (inclusive)的行
q8 = df.query('age <=4 and age>=2')
# print(q8)
#
# 9.	将age里的'f'改成1.5.
q9 = df.loc['f','age'] = 1.5
# print(df)
#
# 10.	计算visits的和：
q10 = sum(df.visits)
print(q10)
