import pandas as pd
from matplotlib import pyplot as plt
from pylab import mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

pd.set_option('display.max_columns', 12)

class itanic():

    # 处理船舱等级映射中文
    def __toPclassMap(self,row):
        pclass = row['Pclass']
        # survived = row['Survived']
        if pclass == 1:
            return "一等舱"
        if pclass == 2:
            return "二等舱"
        if pclass == 3:
            return "三等舱"


    # 清洗生存添加说明
    def __toSurvivedMap(self,row):
        survived = row['Survived']
        if survived == 0:
            return "死亡"
        if survived == 1:
            return "生存"

        # 处理船舱等级映射中文

    def __toEmbarkedMap(self, row):
        '''
         # Q-代表爱尔兰Queenstown港，
        # C-代表法国瑟堡港Cestbourg,
        # S-代表英国南安普顿港Southampton）
        :param row:
        :return:
        '''
        embarked = row['Embarked']
        # survived = row['Survived']
        if embarked == 'Q':
            return "爱尔兰Queenstown港"
        if embarked == 'C':
            return "法国瑟堡港Cestbourg"
        if embarked == 'S':
            return "英国南安普顿港Southampton"



    def __init__(self):
        self.df = pd.read_csv("titanic_train.csv")
        # apply 的方式转换
        self.df['Pclass_map'] = self.df.apply(self.__toPclassMap,axis=1)
        self.df['Survived_map'] = self.df['Survived'].map(lambda x:'生存' if x ==1 else '死亡')
        self.df['Sex_map'] = self.df['Sex'].map(lambda x: '男性' if x == 'male' else '女性')
        self.df['Embarked_map'] = self.df.apply(self.__toEmbarkedMap,axis=1)
        print(self.df.head(2))



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
        df3= self.df.groupby(['Pclass','Survived']).size()

        print(df3)

        labels =list(map(lambda x: '一等舱' if x[0] == 1 else '二等舱' if x[0] == 2 else '三等舱', df3.index.values[::2]))
        y1 = list(map(lambda x:x , df3.values[::2]))
        y2 = list(map(lambda x:x , df3.values[1::2]))


        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, y1, width, label='生存' if df3.index.values[0][1] ==1 else '死亡')
        rects2 = ax.bar(x + width / 2, y2, width, label='生存' if df3.index.values[1][1] ==1 else '死亡')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('数量')
        ax.set_title('不同舱位等级的获救情况')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()

        plt.show()


    def q4(self):
        '''
        # 4.	不同港口的登船人数分布（Embarked）：
        # （泰坦尼克号沉没事件中，该船共停靠过三个港口的注释：
        # Q-代表爱尔兰Queenstown港，
        # C-代表法国瑟堡港Cestbourg,
        # S-代表英国南安普顿港Southampton）
        # 请用Pandas分析，并用matplotlib图例显示，并做出分析。
        :return:
        '''

        df4 = self.df.groupby('Embarked_map').size()
        labels = df4.index.values
        y = df4.values
        width = 0.35
        x = np.arange(len(df4))
        plt.xticks(x,labels=labels)
        plt.bar(x,y,width=width)
        plt.show()
        print(df4)



    def q5(self):
        '''
        # 5．不同性别乘客获救情况分布
        # 	请用Pandas分析，并用matplotlib图例显示，并做出分析。
        :return:
        '''
        df5 = self.df.groupby(['Sex','Survived']).size()
        print(df5)
        labels = list(map(lambda x: '男' if x[0] == 'male' else '女' , df5.index.values[::2]))
        y1 = list(map(lambda x: x, df5.values[::2]))
        y2 = list(map(lambda x: x, df5.values[1::2]))

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, y1, width, label='生存' if df5.index.values[0][1] == 1 else '死亡')
        rects2 = ax.bar(x + width / 2, y2, width, label='生存' if df5.index.values[1][1] == 1 else '死亡')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('数量')
        ax.set_title('不同性别乘客获救情况分布')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()

        plt.show()

i = itanic()
i.q1()
i.q2()
i.q3()
i.q4()
i.q5()


