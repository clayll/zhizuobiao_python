#泰坦尼克号名单分析
#1.泰坦尼克号存货人数分布
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['font.serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus']=False


pd.set_option('display.max_columns', 12)
df = pd.read_csv('titanic_train.csv')

print(df.head(2))

print(df.loc[df.Embarked.isna() == True,'Embarked'].index.values)

df1 = df.dropna(axis=0,subset=["Embarked"])

print(df1['Embarked'].unique())