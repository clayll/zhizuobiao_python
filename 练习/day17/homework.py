
import requests
from pyquery import PyQuery as pq
import csv
import re

class DoubanSpider():

    def __init__(self,kw):
        self.filename = kw
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}

    def init_allUrl(self):
        self.start_url = "https://movie.douban.com/top250"
        self.baseurl ='https://movie.douban.com/top250'


    def  parse_url(self,url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        return response.text

    def get_url_content(self, content):
        """遍历所有的页面"""
        div_list = pq(content)("ol li")
        content_list = []
        # 遍历内容
        for mydiv in div_list.items():
            item = {}
            movie_a = mydiv(".info")("div .hd a:first")
            movie_bd = mydiv("div .bd")
            item["movie_num"] = mydiv("div .pic em").text()
            item["movie_name"] = self.__replceBlank(movie_a("span").text())
            self.__replceActorDir(movie_bd("p:first").text(),item)
            item["movie_score"] = movie_bd(".rating_num").text()
            item["movie_intro"] = movie_bd(".quote").text()
            item["movie_url"] = movie_a.attr("href")
            # time.sleep(random.random() * 5)

            content_list.append(item)

        # 抽取下一页
        next_page = pq(content)("div .paginator")("a:contains('后页')")

        next_url = ""
        if next_page:
            next_url =self.baseurl + next_page.attr("href")
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

    # 特殊&nbsp; 以及字符/
    def __replceBlank(self,content):
        content = content.replace("\n", "")
        return "".join(content.split("\xa0"))

    def __replceActorDir(self,content,item):
        '''
        提取导演、演员、年份、国家、类型,传入item，并返回
        :param content:
        :return:item
        '''
        content = self.__replceBlank(content)
        try:
            # p = re.compile("导演:(.*)主.(.*?)(\d+.*)")
            p = re.compile("导演:(.*?)[主|\.\.\.|主演:].(.*?)(\d+.*)")
            r1 = re.search(p, content)
            item["movie_director"] = r1.group(1).strip()
            item["movie_star"] = r1.group(2)

            # 在进行正则替换
            p2 = re.compile(r"[\:|\/|\.]+")
            item["movie_star"] = re.sub(p2,"",item["movie_star"]).strip()

            r2 = r1.group(3).split("/")
            item["movie_year"] = r2[0].strip()
            item["movie_country"] = r2[1].strip()
            item["movie_type"] = r2[2].strip()
        except Exception as ex:
            print("错误号：",item["movie_num"])
            print("内容：", content)
            print(ex)
        return item

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

n= DoubanSpider("douban250")
n.run()


def test():
    s = "导演: 奥利维·那卡什 Olivier Nakache / 艾力克·托兰达 Eric Toledano主...2011/法国/剧情 喜剧"
    s1= "导演: 弗洛里安·亨克尔·冯·多纳斯马尔克 Florian Henckel von Donnersmarck&n...2006/德国/剧情 悬疑"
    p = re.compile("导演:(.*?)[主|\.\.\.|主演:].(.*?)(\d+.*)")

    r1 = re.search(p, s1)
    print(r1.groups())

    s3="丹尼尔·雷德克里夫DanielRadcliffe / ..."
    s4 ="..."
    p2 = re.compile(r"[\/|\.]+")
    rs3= re.sub(p2, "",s4).strip()

    print(rs3)

# test()



