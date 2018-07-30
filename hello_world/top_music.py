import requests
from lxml import etree
import re
import pymongo
import time
from hello_world import free_proxyIP

client = pymongo.MongoClient('106.14.220.77',27017)
mydb = client['mydb']
musictrop = mydb['musictop']
ipmain = free_proxyIP
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}



def main():
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_url_music(url)

def get_url_music(url):
    ip = ipmain.proxyip()
    IP = {'http':ip}
    html = requests.get(url,headers=headers ,proxies=IP, timeout=3)
    selector = etree.HTML(html.text)
    music_refs = selector.xpath('//a[@class="nbg"]/@href')
    for music_ref in music_refs:
        get_music_info(music_ref)

def  get_music_info(url):
    ip = ipmain.proxyip()
    IP = {'http':ip}
    html = requests.get(url,headers = headers ,proxies=IP, timeout=3)
    selector = etree.HTML(html.text)
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    author = re.findall('表演者：.*?>(.*?)</a>',html.text,re.S)[0]
    styles = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />',html.text,re.S)
    if len(styles) == 0:
        style = '未知'
    else:
        style = styles[0].strip()
    date = re.findall('<span class="pl">发行时间:</span>&nbsp;(.*?)<br />', html.text, re.S)[0].strip()
    publishs = re.findall('<span class="pl">出版者:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(publishs) == 0:
        publish = '未知'
    else:
        publish = publishs[0].strip()
    score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
    print(name,style,date,publish,score)
    info = {
        'name' : name,
        'style' : style,
        'date': date,
        'publisher': publish,
        'score': score
    }
    musictrop.insert_one(info)

if __name__ == '__main__':
    ipmain.main()
    main()

