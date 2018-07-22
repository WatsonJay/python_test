import requests
from lxml import etree
import re
import pymongo
import time
from hello_world import free_proxyIP

client = pymongo.MongoClient('106.14.220.77',27017)
mydb = client['mydb']
musictrop = mydb['musictop']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}



def main():
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_url_music(url)

def get_url_music(url):
    ipmain = free_proxyIP
    ip = ipmain.proxyip()
    html = requests.get(url,headers = headers ,proxies=ip, timeout=3)
    selector = etree.HTML(html.text)
    music_refs = selector.xpath('//a[@class="nbg"]/@href')
    for music_ref in music_refs:
        get_music_info(music_ref)


if __name__ == '__main__':
    main()

