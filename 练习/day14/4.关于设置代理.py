import urllib.request

url = 'http://www.baidu.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
#构造两个代理Handler，一个有代理ip，一个没有代理ip
httpproxy_handler = urllib.request.ProxyHandler({"http":"61.135.217.7.80"})
nullproxy_handler = urllib.request.ProxyHandler({})

proxySwitch = True #定义一个代理开关

#根据代理开关是否打开，使用不同的代理模式
if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

request = urllib.request.Request(url,headers=headers)

#opener.open(request)发送请求时才使用自定义代理
response = opener.open(request)

#全局都能使用如下：
urllib.install_opener(opener)
response = urlopen(request)
print(response.read().decode('utf-8'))