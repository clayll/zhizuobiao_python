from pyquery import PyQuery as pq
import requests
import time
import csv

begin = time.process_time() #添加程序运行计时功能

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    doc = pq(url, headers=headers)#将解析的URL网址当作参数传递给PyQuery类
    return doc

def parse_page(doc):
    dd = doc('.board-wrapper').find('dd')
    '''
    yield在函数中功能类似于return，不同的是yield每次返回结果之后函数并没有退出。
    而是每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待下一次调用。
    如果一个函数需要多次循环执行一个动作，并且每次执行结果都是需要的，这种情况很适合使用yield实现。
    '''
    for item in dd.items():
        yield {
            'rank':item.find('.board-index').text(),
            'name':item.find('.name').text(),
            'img':item.find('.board-img').attr('data-src'),
            'star':item.find('.star').text(),
            #strip()转化为字符串去除前后空格
            'time':item.find('.releasetime').text().strip(),
            'score':item.find('.score').find('.integer').text().strip()
                    + item.find('.score').find('.fraction').text().strip()
        }

def write_to_file(item):
    writer.writerow((item['rank'],item['name'],item['img'],item['star'],item['time'],item['score']))


def main():
    for i in range(10):
        url = 'https://maoyan.com/board/4?offset=' + str(i * 10)
        doc = get_page(url)#每一页的内容
        for item in parse_page(doc):
            print(item)
            write_to_file(item)
        time.sleep(1)


if __name__ =='__main__':
    f = open('maoyan100.csv','a',newline='',encoding='utf-8')
    writer = csv.writer(f)
    #写入头部信息
    writer.writerow(('Rank','Name','Picture','Star','Time','Score'))
    main()
    f.close()
    end = time.process_time()
    print("爬取完毕,耗时: %f 秒"% (end-begin))


