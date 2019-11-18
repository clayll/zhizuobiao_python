import pandas as pd

#1.Series
#它是一维的，带索引的数组，支持多种数据类型。可以使用列表进行转换。



# s = pd.Series([3,-5,7,4],index=['a','b','c','d'])
# print(s)
#
# #可重新指定索引
# s.index = ['A','B','C','D']
# print(s)

#2.DataFrame
#一种二维的，类似于Excel表格的数据结构。可以为其指定列名、索引名
#将字典结构转换为DataFrame:

#默认写法：
#
# data  = {
#     'Coutry':['China','Japan','Korea'],
#     'Captial':['Beijing','Tokyo','Seoul'],
#     'Population':[12,9,6]
# }
# df = pd.DataFrame(data)
# print(df)
#

#自定义列的顺序
# data  = {
#     'Coutry':['China','Japan','Korea'],
#     'Captial':['Beijing','Tokyo','Seoul'],
#     'Population':[12,9,6]
# }
# df = pd.DataFrame(data, columns=['Coutry','Captial','Population'])
# print(df)

#读取DataFrame中的数据
#通过类似字典键索引的方式

# data  = {
#     'Country':['China','Japan','Korea'],
#     'Captial':['Beijing','Tokyo','Seoul'],
#     'Population':[12,9,6]
# }
# df = pd.DataFrame(data, columns=['Country','Captial','Population'])
# country = df['Captial']
# print(country)


#通过属性的方式
# country = df.Country
# print(country)


#DataFrame增加列
data  = {
    '地区':['北京','上海','广州','深圳','重庆'],
    '年份':['2000','2000','2002','2001','2002'],
    '人口':[1.5,1.7,3.6,2.4,2.9]
}
df = pd.DataFrame(data,columns=data.keys())
# print(df)
# df['财务'] = 17
# print(df)#给财务列赋值一组值
# df['财务'] = range(5)
# print(df)

# df['地区_上海'] = df.地区 == '上海'
#
# print(df)

#DF删除列

# del df['地区_上海']
# print(df)


#DF转置
# print(df.T)

#DF取值:
print(df.values)