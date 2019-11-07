'''
今日内容:
1.爬虫介绍
编写程序，根据url获取网站的信息

注意：别犯法 2015之后

2.爬取汽车之家新闻
    a.伪造浏览器向某个地址发送Http请求,获取返回的字符串
        pip install requests

        response = requests.get("url='地址")
        response.content
        response.encoding = apparent_encoding
        response.text

    b. bs4 解析HTML格式的字符串
        pip install beautifulsoup4

        soup = BeautifulSoup('<html>...</html>','html.parser')

        div = soup.find(name='标签名')
        div = soup.find(name='标签名',id='l1')
        div = soup.find(name='标签名',class='il')

        div.text
        div.attrs
        div.get('href')

        divs = soup.find_all(name='标签名')
        divs = soup.find_all(name='标签名',id='l1')
        divs = soup.find_all(name='标签名',_class='il')
        divs = soup.find_all(name='div',attrs={'id':"auto-channel-lazyload-article",'class':'dd'})

        divs是列表
        divs[0]

3.requests
4.bs4
'''

import requests
from bs4 import BeautifulSoup

#1.下载页面
ret = requests.get(url='https://www.autohome.com.cn/news/')
# print(ret.content)#返回是字节串
# print(ret.apparent_encoding)
ret.encoding = ret.apparent_encoding
# print(ret.text)#返回字符串


#2.解析：获取想要的指定内容 BeautifulSoup
#html.parser: 内置的解释器
#lxml:速度更快
soup = BeautifulSoup(ret.text,'html.parser')
div = soup.find(name='div',id="auto-channel-lazyload-article")
#div = soup.find(name='div',attrs={'id':"auto-channel-lazyload-article",'class':'dd'})
li_list = div.find_all(name='li')
# print(li_list)

for li in li_list:
    h3 = li.find(name='h3')
    if not h3:
        continue

    p = li.find(name='p')
    a = li.find(name='a')


    img = li.find('img')
    src = img.get('src')
    file_name = src.rsplit('__',maxsplit=1)[1]

    ret_img = requests.get(
        url = 'https:'+ src
    )
    with open(file_name,'wb') as f:
        f.write(ret_img.content)


    print(h3.text,a.get('href'))
    print(p.text)
    print('='*120)
















