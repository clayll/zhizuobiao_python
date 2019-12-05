#泰坦尼克号名单分析
#1.泰坦尼克号存货人数分布
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import matplotlib
import seaborn as sns
import math
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
#指定默认字体
# mp.rcParams['font.sans-serif'] = ['FangSong']
# mp.rcParams['font.family']='FangSong'
# # myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')
#
# #解决负号'-'显示为方块的问题
# mp.rcParams['axes.unicode_minus'] = False
# sns.set(font='FangSong')  # 解决Seaborn中文显示问题  https://www.lizenghai.com/archives/34192.html
print(matplotlib.matplotlib_fname())

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
    contry = contry.sum(axis=1)
    contry = pd.DataFrame({'国家名称':contry.index,'国家数量':contry.values})

    print(contry)
    sns.barplot(x='国家数量',y='国家名称',data=contry)
    mp.show()

# countryRank()

# c.	统计每个区域里相同国家的总数。
def countryTotal():
    contry = df['movie_country'].str.split(' ').apply(pd.Series)
    contry = contry.apply(pd.Series.value_counts)
    contry.fillna(value=0, inplace=True)
    contry.rename({0: 'a1', 1: 'a2', 2: 'a3', 3: 'a4', 4: 'a5', 5: 'a6'}, inplace=True, axis=1)
    print(contry.sum(axis=1).sort_values(ascending=False))
    sns.countplot(data=contry)
    mp.show()

# cs = pd.cut(df['movie_num'],bins=12,labels=list("abcdefghijkl"))
# print(cs)

# countryTotal()
# d.	计算每个国家参与制作的电影总数排名情况
# e.	获取电影类型数量前10的类型及上榜次数最多的导演
def typeRank():
    types = df['movie_type'].str.split(' ').apply(pd.Series)
    types = types.apply(pd.Series.value_counts)
    types.fillna(value=0,inplace=True)
    # 获取前10的类型
    top10Types = pd.Series(types.sum(axis=1).sort_values(ascending=False),dtype=int).head(10)
    top10index = top10Types.index.tolist()
    def caculateTypeNum(item):
        list = item['movie_type'].split(' ')
        count = 0
        for i in list:
            if i in top10index:
                count = count+1
        item['actorTop'] = count
        return item
    df['actorTop'] = 0

    result = df.apply(caculateTypeNum,axis=1)
    resuntgb = result.groupby(by='movie_director')[['actorTop']].sum()

    resuntgb = resuntgb.sort_values(by='actorTop', ascending=False).head(10)
    resuntgb = pd.DataFrame({"导演":resuntgb.index,"类型数量":resuntgb.values})
    sns.barplot(x='类型数量',y='导演',data=resuntgb)



# typeRank()

# f.	评分和排名的关系
# print(np.corrcoef(df.movie_num ,df.movie_score))
# mp.scatter(df.movie_num ,df.movie_score)
# mp.show()


# print(df.describe(include=['O']))
# print(df.corr())

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



print([i for i in df.columns])

s_mask = np.array(Image.open("stormtrooper_mask.png"))
stopwords = set(STOPWORDS)
stopwords.add("said")

# wc = WordCloud(background_color="white", max_words=2000, mask=s_mask,
#                stopwords=stopwords, contour_width=3, contour_color='steelblue')
# mytext1 = ' '.join(df['movie_type'].tolist())
mytext = ' '.join(df['movie_director'].tolist())
wc1 = WordCloud(
    background_color='white',  # 背景色
    width=2000,  # 宽度
    height=1000,  # 高度
    font_path='simhei.TTF',  # 字体文件，此处与py文件放在同一目录
mask=s_mask, stopwords=stopwords,
    margin=1  # 词语边缘距离
)
wc2 = wc1.generate(mytext)  # 绘制词云
mp.rcParams['figure.dpi'] = 600  # 修改dpi
mp.rcParams['savefig.dpi']=600   # 修改dpi
mp.axis('off')
mp.imshow(wc2)

# plt.savefig('{}.jpg'.format(filename))
mp.show()



# plot_distribution2(dataset=df.loc[:,['movie_year','movie_country','movie_type','movie_score']],height=30,cols=2)
# mp.bar(['测试1','测试2','测试3'],[1,5,7])
# s = sns.regplot(x='movie_score',y='movie_num',data=df)
# 相关系数热力图
# fig = mp.figure(figsize=(10,6))
# fig.add_subplot(1,2,1)
# sns.heatmap(data=df.corr(),cmap="YlOrBr_r")
# fig.add_subplot(1,2,2)
# sns.relplot(x='movie_score',y='movie_num',data=df)
# mp.show()
# s1 = df['movie_country'].str.split(' ')

#
#
# s2 = pd.Series(data= [['中国大陆', '中国香港'],['英国' ,'美国' ,'法国']],index=[2,3])
# print(s2)

# print(s1)

# data = [[1,1,1,1,0]]
# df2 = pd.DataFrame(data=data,index=['中国台湾-中国大陆-美国-中国香港'],columns=['中国台湾', '中国大陆', '美国', '中国香港','日本'])
# print(df2)
