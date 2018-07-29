import requests
from lxml import etree
import re
import pymysql
import time
from hello_world import free_proxyIP
conn = pymysql.connect(
    host='106.14.220.77', user='root',password='',db='mydb',port=3306,charset='utf-8'
)
cursor = conn.cursor()
ipmain = free_proxyIP
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

def main():
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_url_movice(url)

def get_url_movice(url):
    ip = ipmain.proxyip()
    IP = {'http':ip}
    html = requests.get(url,headers=headers ,proxies=IP, timeout=3)
    selector = etree.HTML(html.text)
    movie_refs = selector.xpath('//*div[@class="hd"]/a/@href')
    for movie_ref in movie_refs:
        get_movie_info(movie_ref)

def  get_movie_info(url):
    ip = ipmain.proxyip()
    IP = {'http': ip}
    html = requests.get(url, headers=headers, proxies=IP, timeout=3)
    selector = etree.HTML(html.text)
    try:
        name = selector.xpath('//*div[@id="content"]/h1/span[1]/text()')[0]
        director =selector.xpath('//*div[@id="info"]/span[1]/span[2]/a/text()')[0]
        actors = selector.xpath('//*div[@id="info"]/span[3]/span[2]/')

    except IndexError:
        pass