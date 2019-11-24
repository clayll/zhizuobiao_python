#泰坦尼克号名单分析
#1.泰坦尼克号存货人数分布
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['font.serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus']=False


#1.数据清洗
data = pd.read_csv('titanic_train.csv')
# print(data.info())
data.drop(['PassengerId','Name','Ticket','Cabin'],axis=1,inplace=True)
# print(data.info())
# print(data.isnull().sum())
data.Age = data.Age.fillna(data.Age.mean())
data.dropna(subset=['Embarked'],how='any',axis=0,inplace=True)
# print(data.isnull().sum())

#数据规整
# print(data.Sex.unique())
data.loc[data['Sex']=='male','Sex']=0
data.loc[data['Sex']=='female','Sex']=1

# print(data.Embarked.unique())
data.loc[data['Embarked']=='S','Embarked'] = 0
data.loc[data['Embarked']=='C','Embarked'] = 1
data.loc[data['Embarked']=='Q','Embarked'] = 2

pd.options.display.max_rows=None
pd.options.display.max_columns=None
print(data.describe())



#数据分析
'''
1.泰坦尼克号存活人数分布
2.不同舱位等级的人数分布
3.不同舱位等级的获救人数
4.不同港口的登船人数分布
5.不同性别乘客获救情况分布
'''
#大概存活130人左右，占总比例1/3左右
# fig,axes = mp.subplots(2,3,figsize=(20,30))
# mp.subplot(2,3,1)
# data['Survived'].value_counts().plot(kind='bar',alpha=0.75,color=['dodgerblue','orangered'])
# mp.title('存活人数')

#3等舱人数最多，符合当时历史收入情况
# mp.subplot(2,3,2)
# data['Pclass'].value_counts().plot(kind='bar',alpha=0.75,color=['dodgerblue','orangered','limegreen'])
# mp.title('不同船舱人数')
#

#舱位等级越高，获救比例越高。
# survive_0 = data['Pclass'][data['Survived']==0].value_counts()
# survive_1 = data['Pclass'][data['Survived']==1].value_counts()
# data2 = pd.DataFrame({'获救':survive_1,'未获救':survive_0})
# data2.plot(kind='bar',stacked=True)
# mp.title('不同舱位等级获救比例')
# mp.show()


# survive_0 = data['Embarked'][data['Survived']==0].value_counts()
# survive_1 = data['Embarked'][data['Survived']==1].value_counts()
# data2 = pd.DataFrame({'获救':survive_1,'未获救':survive_0})
# data2.plot(kind='bar',stacked=True)
# mp.title('不同港口获救比例')

#当时绅士精神，把存活机会留给了女士
survive_0 = data['Survived'][data['Sex']==0].value_counts()
survive_1 = data['Survived'][data['Sex']==1].value_counts()
data2 = pd.DataFrame({'获救':survive_1,'未获救':survive_0})
data2.plot(kind='bar',stacked=True)
mp.title('不同性别获救比例')

mp.show()






