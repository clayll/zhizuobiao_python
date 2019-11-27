#泰坦尼克号名单分析
#1.泰坦尼克号存货人数分布
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['font.serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus']=False


pd.set_option('display.max_columns', 12)
# df = pd.read_csv('titanic_train.csv')
#
# print(df.head(2))
#
# print(df.loc[df.Embarked.isna() == True,'Embarked'].index.values)
#
# df1 = df.dropna(axis=0,subset=["Embarked"])
#
# print(df1['Embarked'].unique())
df = pd.read_csv('douban250.csv')
print(df.head(2))
def checkName():
    movieCount = len(df['movie_name'].unique())
    print("数据总共有250条，检查重名的数量%s，所以没有重名" % movieCount)
#a.	重复值检查（检查是否有重名电影）
checkName()

def countryRank():
    print(len(df[df['movie_country'].isnull()==True]))
    print(len(df['movie_country'].unique()))
    df1 = df.groupby(by='movie_country').size()
    print(df1)
countryRank()
# b.	查看国家或地区与电影制作的排名情况（空值部分请替换为‘0’，可以考虑先按列计数，替换空值，再按行汇总。）
# c.	统计每个区域里相同国家的总数。
# d.	计算每个国家参与职做的电影总数排名情况
# e.	获取电影类型数量前10的类型及上榜次数最多的导演
# f.	评分和排名的关系a.	重复值检查（检查是否有重名电影）
def myToInt(item):
    print(item,type(item))
    if isinstance(item,str):
        return 1
    else:
        return item



contry = df['movie_country'].str.split(' ').apply(pd.Series)
contry = contry.apply(pd.Series.value_counts)

contry.fillna(value=0,inplace=True)

contry.rename({0:'a1',1:'a2',2:'a3',3:'a4',4:'a5',5:'a6'},inplace=True,axis=1)


print(contry)
# x1 = contry.groupby('a1').sum()
# print(x1)




# s1 = df['movie_country'].str.split(' ')
#
#
#
# s2 = pd.Series(data= [['中国大陆', '中国香港'],['英国' ,'美国' ,'法国']],index=[2,3])
# print(s2)

# print(s1)

# data = [[1,1,1,1,0]]
# df2 = pd.DataFrame(data=data,index=['中国台湾-中国大陆-美国-中国香港'],columns=['中国台湾', '中国大陆', '美国', '中国香港','日本'])
# print(df2)