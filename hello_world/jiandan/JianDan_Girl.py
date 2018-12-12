import requests
from bs4 import BeautifulSoup
from lxml import etree
import time

index = 0
headers = {
    'referer': 'http://www.freebuf.com/',
    'host':'jandan.net',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
}




# 保存图片
def save_jpg(res_url):
    global index
    html = requests.get(res_url, headers=headers)
    # html = BeautifulSoup(.text,'lxml')
    selector = etree.HTML(html.text)
    links = selector.xpath('//a[@class = "view_img_link"]')
    # links = html.find_all('a', {'class': 'view_img_link'})
    for link in links:
        with open('{}.{}'.format(index, link.get('href')[len(link.get('href'))-3: len(link.get('href'))]), 'wb') as jpg:
            jpg.write(requests.get("http:" + link.get('href')).content)
        print("正在抓取第%s条数据" % index)
        index += 1


#  抓取煎蛋妹子图片，默认抓取5页
if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    for i in range(0, 5):
        save_jpg(url)
        url = "http:" + BeautifulSoup(requests.get(url, headers=headers).text,'lxml').find('a', {'class': 'previous-comment-page'}).get('href')