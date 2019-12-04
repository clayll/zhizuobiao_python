#泰坦尼克号名单分析
#1.泰坦尼克号存货人数分布
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import seaborn as sns
import math
#指定默认字体
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
mp.rcParams['axes.unicode_minus'] = False
sns.set(font='SimHei')  # 解决Seaborn中文显示问题  https://www.lizenghai.com/archives/34192.html


# pd.set_option('display.max_columns', 12)
# df = pd.read_csv('titanic_train.csv')
# print(df.head(2))
#
# print(df.loc[df.Embarked.isna() == True,'Embarked'].index.values)
#
# df1 = df.dropna(axis=0,subset=["Embarked"])
#
# print(df1['Embarked'].unique())
df = pd.read_csv('douban250.csv')
df.loc[(df['movie_country'] == '1964(中国大陆)') | (df['movie_country'] == '2019(中国大陆重映)'),'movie_country'] = '中国大陆'

df.loc[df.movie_type == '1978(中国大陆)','movie_type'] = '动画 奇幻'
df.loc[df.movie_type == '中国大陆','movie_type'] = '动画 奇幻'
print(df.head(1))

print(df.query("movie_type == '1978(中国大陆)' | movie_type ==  '中国大陆' "))
def checkName():
    movieCount = len(df['movie_name'].unique())
    print("数据总共有250条，检查重名的数量%s，所以没有重名" % movieCount)
#a.	重复值检查（检查是否有重名电影）
# checkName()



# b.	查看国家或地区与电影制作的排名情况（空值部分请替换为‘0’，可以考虑先按列计数，替换空值，再按行汇总。）
def countryRank():
    contry = df['movie_country'].str.split(' ').apply(pd.Series)
    contry = contry.apply(pd.Series.value_counts)
    contry.fillna(value=0, inplace=True)
    contry.rename({0: 'a1', 1: 'a2', 2: 'a3', 3: 'a4', 4: 'a5', 5: 'a6'}, inplace=True, axis=1)

# countryRank()

# c.	统计每个区域里相同国家的总数。
def countryTotal():
    contry = df['movie_country'].str.split(' ').apply(pd.Series)
    contry = contry.apply(pd.Series.value_counts)
    contry.fillna(value=0, inplace=True)
    contry.rename({0: 'a1', 1: 'a2', 2: 'a3', 3: 'a4', 4: 'a5', 5: 'a6'}, inplace=True, axis=1)
    print(contry.sum(axis=1).sort_values(ascending=False))

cs = pd.cut(df['movie_num'],bins=12,labels=list("abcdefghijkl"))
print(cs)

countryTotal()
# d.	计算每个国家参与制作的电影总数排名情况
# e.	获取电影类型数量前10的类型及上榜次数最多的导演
def typeRank():
    types = df['movie_type'].str.split(' ').apply(pd.Series)
    types = types.apply(pd.Series.value_counts)
    types.fillna(value=0,inplace=True)

    print(pd.Series(types.sum(axis=1).sort_values(ascending=False),dtype=int) )


typeRank()

# f.	评分和排名的关系
# print(np.corrcoef(df.movie_num ,df.movie_score))
# mp.scatter(df.movie_num ,df.movie_score)
# mp.show()


print(df.describe(include=['O']))
print(df.corr())

# x1 = contry.groupby('a1').sum()
# print(x1)
import math
def plot_distribution(dataset, cols=3, width=20, height=15, hspace=0.2, wspace=0.5):
    mp.style.use('seaborn-whitegrid')
    fig = mp.figure(figsize=(width,height))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=wspace, hspace=hspace)
    rows = math.ceil(float(dataset.shape[1]) / cols)
    for i, column in enumerate(dataset.columns):
        ax = fig.add_subplot(rows, cols, i + 1)
        ax.set_title(column)
        if dataset.dtypes[column] == np.object:
            g = sns.countplot(y=column, data=dataset)
            substrings = [s.get_text()[:18] for s in g.get_yticklabels()]
            g.set(yticklabels=substrings)
            mp.xticks(rotation=25)
        else:
            #直方图，频数
            g = sns.distplot(dataset[column])
            mp.xticks(rotation=25)
    # mp.show()
# plot_distribution(df)

def plot_distribution2(dataset : pd.DataFrame,cols=5,width=20,height=15,wspace=0.2,hspace=0.5):
    mp.style.use('seaborn-whitegrid')
    rows = math.ceil((dataset.shape[1]/cols))
    fig = mp.figure(figsize=(width,height))
    for i,item in enumerate(dataset):
        axe = fig.add_subplot(rows,cols,i+1)

        axe.set_title(item)
        if dataset[item].dtypes == np.object:
            g = sns.countplot(y=item, data=dataset)
            substrings = [s.get_text()[:18] for s in g.get_yticklabels()]
            g.set(yticklabels=substrings)

            mp.xticks(rotation=25)
        else:
            g = sns.distplot(dataset[item])
            mp.xticks(rotation=25)
    mp.show()



print(type(df.columns))
print([i for i in df.columns])
print(math.ceil(float(df.shape[1]) / 3))
# plot_distribution2(dataset=df.loc[:,['movie_country','movie_type']],height=100,cols=1)
# mp.bar(['测试1','测试2','测试3'],[1,5,7])
s = sns.regplot(x='movie_score',y='movie_num',data=df)

mp.show()
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