from lxml import etree
import requests
import csv
import re

fq = open('book/test.csv','w',newline = '',encoding='GBK')
writer = csv.writer(fq)
writer.writerow(('书名','链接','作者','出版社','出版时间','价格','评分','短评'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

for url in urls:
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class = "item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_info = info.xpath('td/p/text()')[0]
        author = book_info.split('/')[0]
        price = book_info.split('/')[-1]
        date = book_info.split('/')[-2]
        publisher = book_info.split('/')[-3]
        star = info.xpath('td/div/span[2]/text()')[0]
        comments= info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments)!= 0 else "空"
        writer.writerow((name, url, author, publisher, date, price, star, comment))
        print(name+'摘录完毕')

fq.close()
