# 1.	简答题:(1分):
# 介绍下try..except..except..[else…][finally]..的用法和作用？
# 正常执行的程序在try下面的语句块，在执行过程中如果发生了异常，从第一个except处开始查找，如果找到了对应的exception类型则进入其提供的excep中进行处理，
# 如果没有找到则直接进入except块处进行处理。except块是可选项，如果没有提供，该exception将会被提交给python进行默认处理，处理方式则是终止应用程序并打印提示信息；
# 如果在执行块中执行过程中没有发生任何异常，则在执行完后会进入else执行块中执行。
# 无论是否发生了异常，只要提供了finally语句，以上try/except/else/finally代码块执行的最后一步总是执行finally所对应的代码块。
# 2. 编程题(4分)
# 模拟斗地主发牌, 扑克牌共54张
# 三个人一起玩,每个人发17张,底牌三张
# 牌的种类:
# 黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665'), 红桃('\u2666')
# 数字:
# A2~10JQK
# 大小王
# #   要求,输入回车,打印第1个人的17张牌
# #   再回车,打印第2个人的17张牌
# #   再回车,打印第3个人的17张牌
# #   再回车,打印三张底牌

# 拍属性
class Card():
    def __init__(self,cardColor,cardName,cardNo):
        # 花色
        self.cardColor =  cardColor
        # 派名
        self.cardName= cardName
        # 排顺序
        self.cardNo = cardNo

    def __str__(self):
        if(self.cardName == '大王' or self.cardName == '小王'):
            return self.cardName
        else:
            return self.cardColor +self.cardName

    def getName(self):
        if (self.cardName == '大王' or self.cardName == '小王'):
            return self.cardName
        else:
            return self.cardColor + self.cardName

# 扑克牌类
class Poker():
    def __init__(self):
        self.cardList = self.__generatePorker()

    def __generatePorker(self):
        colors = ["黑桃", "梅花", "方块", "红桃"]
        names =["A"] + [str(i+2) for i in range(9)]+(list("JQK"))

        cardList= []
        number = 1
        for color in colors:
            for name in names:
                cardList.append(Card(color,name,number))
                number = number+1

        cardList.append(Card('小王', '小王', number))
        cardList.append(Card('大王', '大王', number+1))
        return cardList

# 斗地主类
import random
class doudizhu():
    def __init__(self,poker : Poker):
        # 3个玩家和3张底牌
        self.person1,self.person2,self.person3,self.left3 = [],[],[],[]

        self.poker = poker
        self.cardNoByPerson = 17
        self.leftCardNo = 3

    # 发牌
    def licensing(self):
        # 洗牌
        cardList = self.poker.cardList
        random.shuffle(cardList)

        self.person1 = cardList[0:17]
        self.person2 = cardList[17:34]

        self.person3 = cardList[34:51]

        self.left3 = cardList[51:]
        self.__showAll()



    # 显示牌信息
    def __showCards(self,label,list):
        print(label+"牌为："+",".join([i.getName() for i in list]))

    # 显示所有牌信息
    def __showAll(self):
        all = {"玩家1":self.person1,"玩家2":self.person2,"玩家3":self.person3,"底牌":self.left3}
        for key,item in all.items():
            a = self.__getInput()
            if a == True:
                self.__showCards(key, item)


    def __getInput(self):
        while True:
            a = input("请输入回车依次查看信息：")
            if a == '':
                return True
            else:
                print("输入错误！")

s = Poker()
d = doudizhu(s)
# d.licensing()
# 3.编写代码实现下列需求（5分）
# 爬取51job上的职位信息，并写入到文本和excel文件中

import requests
from bs4 import BeautifulSoup
import csv
import time

class job51Spider():

    def __init__(self,kw):
        self.filename = kw
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
        self.url_list = []
        # 抓取页数
        self.dataCount=50



    def init_allUrl(self):
        self.start_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        # self.baseurl ='https://news.online.sh.cn/news/gb/node/'
        # self.baseurlA = 'https://news.online.sh.cn/news/gb/'

        self.url_list.append(self.start_url)

    def  parse_url(self,url):

        response = requests.get(url, headers=self.headers)
        response.encoding = "gbk"
        return response.text

    def get_url_content(self, content):

        """遍历所有的页面"""

        soup = BeautifulSoup(content, 'html.parser')
        resultList= soup.find(id="resultList")
        div_list = resultList.find_all("div",'el')[1:]


        content_list = []
        # 遍历内容
        for mydiv in div_list:
            item = {}

            t1 = mydiv.find(name='p',class_='t1')
            a = t1.find('a')
            href = a.get("href")
            title = self.__replceblank(a.text)
            companyName = mydiv.find(name='span',class_='t2').text
            datetime = mydiv.find(name='span',class_='t5').text
            city = mydiv.find(name='span',class_='t3').text
            salary=mydiv.find(name='span',class_='t4').text

            item = dict({"链接": href, "标题": title,"公司名称":companyName,"城市":city,"薪资":salary,"发布日期":datetime})
            print(item)
            # time.sleep(random.random() * 0.5)s
            content_list.append(item)



        # 抽取下一页
        next_page = soup.find(name= 'a',text="下一页")
        next_url = ""


        if next_page:
            next_url =next_page.get("href")

        # 数据限制

        return content_list,next_url




    def save_content_list(self,content_list):
        f = open(self.filename + ".csv", mode="a", encoding="utf-8")
        writer = csv.writer(f)
        flag = True
        for item in content_list:
            print(item)
            keys = list(item.keys())
            if flag:
                writer.writerow(keys)  # 将属性列表写入csv中
                flag = False

            #读取json数据的每一行，将values数据一次一行的写入csv中
            writer.writerow(list(item.values()))
    def  save_content_list_txt(self,content_list):
        f = open(self.filename + ".txt", mode="a", encoding="utf-8")


        for item in content_list:
            #读取json数据的每一行，将values数据一次一行的写入csv中
            f.write("\t".join(item.values())+"\r\n")

    # 特殊处理空格/
    def __replceblank(self,url):
        url =  url.replace("\r\n","")
        return url.replace(" ", "")




    def run(self):
        # t1 = time.time()
        # 1 整个页面的标题以及对应标题的URL
        self.init_allUrl()
        next_url = self.start_url
        content_list = []
        while next_url:
            # 2 根据url去请求列表页面
            html = self.parse_url(next_url)
            # 2.1请求详情页面的地址
            content,next_url = self.get_url_content(html)
            if len(content)>0:
                content_list.extend(content)
             #     数据限制
            if len(content_list) > self.dataCount:
                break



        # 3.做数据保存
        self.save_content_list(content_list)
        self.save_content_list_txt(content_list)


        # print(time.time()-t1)
n= job51Spider("数据分析")
n.run()
