'''

ck:
name: 111
password: 22
remember: false

'''

import requests

def main():
    url_basic = "https://accounts.douban.com/j/mobile/login/basic"
    url = 'https://www.douban.com/'
    ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    data = {
        'ck':'',
        'name': '18939905107',
        'password': 'my123456',
        'remember': 'false',
        'ticket':''
    }
    s = requests.session()  #跨请求保持参数。session对象所发出的请求之间会保持cookie
    s.post(url=url_basic,headers=ua_headers,data=data)
    response = s.get(url=url,headers=ua_headers)
    with open('douban.html','wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    main()