import pandas as pd
from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

pd.set_option('display.max_columns', 12)

class itanic():

    def __toLable(self,row):
        pclass = row['Pclass']
        survived = row['Survived']
        if pclass == 1:
            return "一等舱"
        if pclass == 2:
            return "二等舱"
        if pclass == 3:
            return "三等舱"
        if survived == 0:
            return "死亡"
        if survived == 1:
            return "生存"

    def __init__(self):
        self.df = pd.read_csv("titanic_train.csv")

        print(self.df.head(1))



    def q1(self):
        '''
        # 1.	泰坦尼克号存活人数分布：
        # 请用Pandas分析，并用matplotlib图例显示，并做出分析。
        :return:
        '''
        df1 = self.df.groupby('Survived').size()
        print(df1.head(2))
        plt.bar(df1.index.values, df1.values)
        plt.xticks(df1.index.values,labels=['生存','死亡'])
        plt.show()

    def q2(self):
        '''
        # 2.	不同舱位等级的人数分布。
        # 请用Pandas分析，并用matplotlib图例显示，并做出分析。
        :return:
        '''
        df2 = self.df.groupby('Pclass').size()
        plt.bar(df2.index.values, df2.values)
        plt.show()

    def q3(self):
        '''
        3.	不同舱位等级的获救情况
        请用Pandas分析，并用matplotlib图例显示，并做出分析。
        :return:
        '''
        df3= self.df.apply(self.__toLable)
        # df3 = self.df.groupby(['Pclass','Survived']).apply(self.__toLable).size()



        print(df3)






i = itanic()
i.q3()



# 3.	不同舱位等级的获救情况
# 请用Pandas分析，并用matplotlib图例显示，并做出分析。
#
# 4.	不同港口的登船人数分布（Embarked）：
# （泰坦尼克号沉没事件中，该船共停靠过三个港口的注释：
# Q-代表爱尔兰Queenstown港，
# C-代表法国瑟堡港Cestbourg,
# S-代表英国南安普顿港Southampton）
# 请用Pandas分析，并用matplotlib图例显示，并做出分析。
#
# 5．不同性别乘客获救情况分布
# 	请用Pandas分析，并用matplotlib图例显示，并做出分析。
