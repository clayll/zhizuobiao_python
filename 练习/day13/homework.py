
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
