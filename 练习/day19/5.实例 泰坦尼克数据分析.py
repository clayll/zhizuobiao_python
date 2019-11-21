import pandas as pd
import numpy as np

titanic_survival = pd.read_csv('titanic_train.csv')

# print(titanic_survival.head())
age = titanic_survival['Age']
# print(age.iloc[0:10])
age_is_null = pd.isnull(age)#迭代判断值是否为空，结果可以一个索引
#获取值为空的数据集
age_null_true = age[age_is_null]
# print(len(age_null_true))#判断一共有多少个空数据

#求平均值，应用不为空的数据集
good_ages = age[age_is_null == False]   #获取值不为空的数据集
# print(good_ages)
# correct_mean_age = sum(good_ages) / len(good_ages)  #求平均
# print(correct_mean_age)
#使用pandas内置的求平均值函数，自动去除空数据
correct_mean_age = age.mean()   #pandas内置求平均，将空值舍弃

#pivot_table透视表方法默认求平均值，如果需求是求平均aggfunc参数不写
#对index相同的分别求平均值
passger_survial = titanic_survival.pivot_table(index='Pclass',values='Survived',aggfunc=np.mean)
# print(passger_survial)

#分组对多列求和
# port_stats = titanic_survival.pivot_table(index="Embarked",values=['Fare','Survived'],aggfunc=np.sum)
# print(port_stats)

#丢弃空值数据
drop_na_columns = titanic_survival.dropna(axis=1)
# print(drop_na_columns)
new_titanic_survival = titanic_survival.dropna(axis=0,subset=['Age','Sex'])
#axis=0 以行做依据, 需要指定判断行的字段，数据为空，则DataFrame中丢弃
#print(new_titanic_survival)

#具体定位到某行某列
row_index_83_age = titanic_survival.loc[83,'Age']
# print(row_index_83_age)
row_index_766_pclass = titanic_survival.loc[766,'Pclass']
# print(row_index_766_pclass)

new_titanic_survival = titanic_survival.sort_values('Age',ascending=False)
# print(new_titanic_survival[0:10])
#重置每行的索引值
titanic_reindexed = new_titanic_survival.reset_index(drop=True)
# print(titanic_reindexed[0:20])

#自定义函数，对每行或每列逐个使用
def null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)
#通过自定义函数统计每列为空的个数

column_null_count = titanic_survival.apply(null_count,axis=0)
print(column_null_count)

#通过自定义函数，替换每行的Pclass值，
def which_class(row):
    pclass = row['Pclass']
    if pclass == 1:
        return 'First Class'
    elif pclass == 2:
        return 'Second Class'
    elif pclass == 3:
        return 'Third Class'
    else:
        return 'Unknown'

classes = titanic_survival.apply(which_class,axis=1)
print(classes)