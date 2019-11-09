
# 1. Python中用___readline()______函数读取文件一行内容，用____readlines()_______函数读取文件全部内容。（1分）
def q1():
    with open("c:\\log.txt",encoding="utf-8") as f:
        x = f.readlines()
        print(x)

# 2 现有两元组(('a'),('b')),(('c'),('d')), 请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]（3分）
def q2():
    def gen(*args):
        list = []
        for arg in args:
            list.append(dict((arg,)))

        return list

    l1 = gen((('a'),('b')),(('c'),('d')))
    print(l1)


# .编程题（6分）：
# 1.	请编写代码爬取以下国内新闻内容（包括新闻标题+新闻标题的超链接地址+内容）
# 2.	写代码将爬取下来的内容保存到txt文档中。
# 提示：请使用BeautifulSoup的方法来爬取。
# 网页地址：https://news.online.sh.cn/news/gb/node/creport.htm
import requests
from bs4 import BeautifulSoup
import csv

class newsSpider():

    def __init__(self,kw):
        self.filename = kw
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
        self.url_list = []


    def init_allUrl(self):
        self.start_url = "https://news.online.sh.cn/news/gb/node/creport.htm"
        self.baseurl ='https://news.online.sh.cn/news/gb/node/'
        self.baseurlA = 'https://news.online.sh.cn/news/gb/'

        self.url_list.append(self.start_url)

    def  parse_url(self,url):

        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        return response.text

    def get_url_content(self, content):

        """遍历所有的页面"""

        soup = BeautifulSoup(content, 'html.parser')
        div_list = soup.find_all(name = 'div',class_="list_thread")


        content_list = []
        # 遍历内容
        for mydiv in div_list:
            item = {}

            a = mydiv.find(name='a')
            href = self.__replceDot(a.get("href"))
            title = a.text
            datetime = mydiv.find(name="h3").text
            item = dict({"链接": href, "标题": title,"发布日期":datetime})

            # time.sleep(random.random() * 5)

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

    # 特殊处理连接../
    def __replceDot(self,url):
        return url.replace("../",self.baseurlA)


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
n= newsSpider("国内新闻")
# n.run()

