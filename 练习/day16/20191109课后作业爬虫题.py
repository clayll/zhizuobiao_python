# import requests
# from bs4 import BeautifulSoup
#
#
# url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# header = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
# }
# ret = requests.get(url,headers=header)
# ret.encoding = ret.apparent_encoding
# # print(ret.text)
#
# soup = BeautifulSoup(ret.text,'html.parser')
#
# divs = soup.find_all(name='div',class_="el")
#
# for div in divs:
#     p = div.find(name='p',class_='t1')
#     span = div.find(name='span')
#     a = span.find(name='a')
    # print(a)
#     if not a:
#         continue
#     title = a.get('title')
#     print(title)




import urllib.request as res
import re


allresult = []

url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
response = res.urlopen(url)
html = response.read().decode('gbk')
# print(html)

#编写正则用来提取信息，去掉的东西都用.*?来代替
#是用re.S，正则表达式会将这个字符串为一个整体进行匹配
reg = re.compile('<div class="el">.*?<p class="t1 ">.*?<a target="_blank" '
           'title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?).*?<span '
           'class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span'
           ' class="t5">(.*?)</span>.*?</div>',re.S)

result = re.findall(reg,html)
allresult += result
print(allresult)

