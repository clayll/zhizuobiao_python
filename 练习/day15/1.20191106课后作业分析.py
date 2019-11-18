#有两个元组(('a'),('b')),(('c'),('d')), 匿名函数方法生成列表[{'a':'c'},{'b':'d'}]
#
# tup1 = (('a'),('b'))
# tup2 = (('c'),('d'))
# #
# ret = zip(tup1,tup2)
# def func(tup):
#     return {tup[0]:tup[1]}
# lst = []
# ret2 = map(func,ret)
#
# for i in ret2:
#     lst.append(i)
# print(lst)

# tup1 = (('a'),('b'))
# tup2 = (('c'),('d'))
#
# ret = zip(tup1,tup2)
# ret2 = list(map(lambda tup:{tup[0]:tup[1]},ret))
# print(ret2)


# import requests
# from bs4 import BeautifulSoup
#
# ret = requests.get(url='https://news.online.sh.cn/news/gb/node/creport.htm')
#
# ret.encoding = ret.apparent_encoding
#
# soup = BeautifulSoup(ret.text,'html.parser')
#
# divs = soup.find_all(name='div',class_= 'list_thread')
#
# for div in divs:
#     h2 = div.find(name='h2')
#     p = div.find(name='p')
#     a = h2.find(name='a')
#
#     href = a.get('href')
#
#     content = href.rsplit('/',maxsplit=1)[1]
#
#     file_name = content.rsplit('.',maxsplit=1)[0]+'.txt'
#
#     with open(file_name,'w',encoding='utf-8') as f:
#         f.write(h2.text)
#         f.write(href+'\n')
#         f.write(p.text)
#
#     print(h2.text,href)
#     print(p.text)
#     print('=' * 120)
#

# .编程题（6分）：
# 1.   请编写代码爬取以下国内新闻内容（包括新闻标题+新闻标题的超链接地址+内容）
# 2.   写代码将爬取下来的内容保存到txt文档中。
# 提示：请使用BeautifulSoup的方法来爬取。
# 网页地址：https://news.online.sh.cn/news/gb/node/creport.htm
# import requests
# from bs4 import BeautifulSoup
# import csv
#
# class newsSpider():
#
#     def __init__(self,kw):
#         self.filename = kw
#         self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
#         self.url_list = []
#
#
#     def init_allUrl(self):
#         self.start_url = "https://news.online.sh.cn/news/gb/node/creport.htm"
#         self.baseurl ='https://news.online.sh.cn/news/gb/node/'
#         self.baseurlA = 'https://news.online.sh.cn/news/gb/'
#
#         self.url_list.append(self.start_url)
#
#     def  parse_url(self,url):
#
#         response = requests.get(url, headers=self.headers)
#         response.encoding = "utf-8"
#         return response.text
#
#     def get_url_content(self, content):
#
#         """遍历所有的页面"""
#
#         soup = BeautifulSoup(content, 'html.parser')
#         div_list = soup.find_all(name = 'div',class_="list_thread")
#
#
#         content_list = []
#         # 遍历内容
#         for mydiv in div_list:
#             item = {}
#
#             a = mydiv.find(name='a')
#             href = self.__replceDot(a.get("href"))
#             title = a.text
#             datetime = mydiv.find(name="h3").text
#             item = dict({"链接": href, "标题": title,"发布日期":datetime})
#
#             # time.sleep(random.random() * 5)
#
#             content_list.append(item)
#
#
#         # 抽取下一页
#         next_page = soup.find(name= 'a',text="下一页")
#         next_url = ""
#         if next_page:
#             next_url =self.baseurl + next_page.get("href")
#         return content_list,next_url
#
#
#
#
#     def save_content_list(self,content_list):
#
#         f = open(self.filename + ".csv", mode="a", encoding="utf-8")
#         writer = csv.writer(f)
#         flag = True
#         for item in content_list:
#             print(item)
#             keys = list(item.keys())
#             if flag:
#                 writer.writerow(keys)  # 将属性列表写入csv中
#                 flag = False
#
#             #读取json数据的每一行，将values数据一次一行的写入csv中
#             writer.writerow(list(item.values()))
#
#     # 特殊处理连接../
#     def __replceDot(self,url):
#         return url.replace("../",self.baseurlA)
#
#
#     def run(self):
#         # t1 = time.time()
#         # 1 整个页面的标题以及对应标题的URL
#         self.init_allUrl()
#         next_url = self.start_url
#         content_list = []
#         while next_url:
#             # 2 根据url去请求列表页面
#             html = self.parse_url(next_url)
#             # 2.1请求详情页面的地址
#             content,next_url = self.get_url_content(html)
#             if len(content)>0:
#                 content_list.extend(content)
#
#
#         # 3.做数据保存
#         self.save_content_list(content_list)
#
#
#
#         # print(time.time()-t1)
# n= newsSpider("国内新闻")
# n.run()
#
#



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