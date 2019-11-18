#回家作业
#题1.(2分)
express = r'1 - 2 * ((60 - 30 + (-40/5) * (9-3.33 + 198/4*2998 +10*568/14))-(-4*3)/(16-3*2))'
#正则表达式
#0.去掉表达式中的所有空格
import re
p11 = re.compile("\s+")
express1 = re.sub(p11,"",express)
print(express1)

# 这道题感觉算法有点复杂，等老师评讲
#1.从表达式中匹配出所有的()里面不再有小括号的表达式
p12 = re.compile(r"([-]?\d+[\/|\*|-]+\d*?[\/|\*]?\d*)+")


# 匹配乘除法,处理括号内的长算式,以分组将算式进行最小分割,只包括最小的乘除计算,
rs = re.findall(p12,express1)
print(rs)

# 题2.从表达式9-2*5/3 + 7/3*99/4*2998+10*568/14中匹配出第一个乘法或者除法(2分)

# 乘法
express2 = "9-2*5/3 + 7/3*99/4*2998+10*568/14"
p21 = re.compile(r"\d+(\*|\/)\d+")
rs = re.search(p21,express2)
print(rs)
# 除法
p22 = re.compile(r"\d+(\/)\d+")
rs = re.search(p22,express2)
print(rs)
# 题3：（6分）
#爬取猫眼榜单100大电影信息: https://maoyan.com/board/4

import requests
from bs4 import BeautifulSoup
import csv
import re

class maoyanSpider():

    def __init__(self,kw):
        self.filename = kw
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
        # self.url_list = []


    def init_allUrl(self):
        self.start_url = "https://maoyan.com/board/4"
        self.baseurl ='https://maoyan.com/board/4'
        self.baseurlA = 'https://maoyan.com'

        # self.url_list.append(self.start_url)

    def  parse_url(self,url):

        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        return response.text

    def get_url_content(self, content):

        """遍历所有的页面"""

        soup = BeautifulSoup(content, 'html.parser')
        div_list = soup.find_all(name = 'dd')


        content_list = []
        # 遍历内容
        for mydiv in div_list:
            item = {}

            a = mydiv.find(name='a')
            href = self.baseurlA+a.get("href")
            title = a.get("title")
            imgSrc = a.find(name='img',class_="board-img")
            if imgSrc:
                imgSrc = imgSrc.get("data-src")
            datetime = mydiv.find(name="p",class_="releasetime")
            if datetime:
                datetime = self.__replceTime(datetime.text)
            actors = mydiv.find(name="p",class_="star")
            if actors:
                actors = self.__replceBlank(actors.text)
            item = dict({"链接": href, "标题": title,"发布日期":datetime,"图片链接":imgSrc,"主演":actors})

            # time.sleep(random.random() * 5)
            print(item)
            content_list.append(item)


        # 抽取下一页
        next_page = soup.find(name= 'a',text="下一页")
        next_url = ""
        if next_page:
            next_url =self.baseurl + next_page.get("href")
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

    # 特殊空格换行符/
    def __replceBlank(self,content):
        p = re.compile(r"//n|\s")
        return re.sub(p,"",content)

    # 特殊处理上映时间
    def __replceTime(self, content):
        p = re.compile(r"\d+-\d+-\d+")
        rs = re.search(p, content)
        if rs:
            return rs.group()
        return ""

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


        # 3.做数据保存
        self.save_content_list(content_list)



        # print(time.time()-t1)
n= maoyanSpider("猫眼电影")
# n.run()



def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'
for i in fib(6):
    print(i)

import time


def consumer(name):
    print("%s 准备学习啦!" % name)
    while True:
        lesson = yield

        print("开始[%s]了,[%s]老师来讲课了!" % (lesson, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("同学们开始上课 了!")
    for i in range(10):
        time.sleep(1)
        print("到了两个同学!")
        c.send(i)
        c2.send(i)

