import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
pd.options.display.max_rows=None
pd.options.display.max_columns=None


labels = ['UserID','Gender','Age','Occupation','Zip-code']
users = pd.read_csv('users.dat',sep='::',header=None,names=labels,engine='python')
# print(users.shape)



labels2 = ['MovieID','Title','Genres']

movie = pd.read_csv('movies.dat',sep='::',header=None,names=labels2,engine='python')
# print(movie.head())
# print(movie.shape)

labels3 = ['UserID','MovieID','Rating','Time']
ratings = pd.read_csv('ratings.dat',sep='::',header=None,names=labels3,engine='python')
# print(ratings.head())
# print(movie.shape)

df1 = pd.merge(left= movie, right=ratings)
movie_data = pd.merge(df1,users,how='outer')

#平均分较高电影
movie_rate_mean = pd.pivot_table(movie_data,values=['Rating'],index=['Title'],aggfunc='mean')

# print(movie_rate_mean.head())

movie_rate_mean.sort_values(by='Rating',ascending=False,inplace=True)
# print(movie_rate_mean.head(20))

#查看评分最低的电影
# print(movie_rate_mean[-20:])


#不同性别观众对电影的评分
movie_gender_rating = pd.pivot_table(movie_data,values=['Rating'],index=['Title','Gender'],aggfunc='mean')
# print(movie_gender_rating.head(10))

movie_gender_rating2 = pd.pivot_table(movie_data,values='Rating',index=['Title'],columns=['Gender'],aggfunc='mean')
# print(movie_gender_rating2.head(10))


#不同性别争议最大影片
#查看列索引
# print(movie_gender_rating2.columns)

movie_gender_rating2['diff'] = movie_gender_rating2.F - movie_gender_rating2.M
# print(movie_gender_rating2.head(10))
movie_gender_rating2.sort_values(by='diff',ascending=False,inplace=True)
# print(movie_gender_rating2.head(10))

# print(movie_gender_rating2[:10])

# print(movie_gender_rating2[-10:])

m = movie_gender_rating2.dropna()[-10:]
# print(m)
f = movie_gender_rating2.dropna()[:10]
#将男女最爱电影合一张表

#.concat()合并操作
diff = pd.concat([f,m])
# print(diff)

diff.plot(y='diff',kind='barh',figsize=(16,9))
# mp.show()


#评论次数最多热门的电影
rating_count =  movie_data.groupby(['Title']).size()
# print(rating_count.sort_values(ascending=False))

#查看不同年龄段争议最大电影
# movie_data['Age'].plot(kind='bar')
# mp.show()
