#用urllib.request爬取网页

import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")

print(response.read().decode('utf-8'))