import requests
from lxml import etree
import re
import pymysql
import time
from hello_world import free_proxyIP

conn = pymysql.connect(
    host='106.14.220.77', user='root', password='', db='mydb', port=3306, charset='utf8'
)
cursor = conn.cursor()
ipmain = free_proxyIP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}


def main():
    urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        get_url_movice(url)
    conn.commit()
    print("all done")

def get_url_movice(url):
    ip = ipmain.proxyip()
    IP = {'http': ip}
    html = requests.get(url, headers=headers, proxies=IP, timeout=3)
    selector = etree.HTML(html.text)
    movie_refs = selector.xpath('//div[@class="hd"]/a/@href')
    for movie_ref in movie_refs:
        get_movie_info(movie_ref)
    print("page ok,next page")

def get_movie_info(url):
    ip = ipmain.proxyip()
    IP = {'http': ip}
    html = requests.get(url, headers=headers, proxies=IP, timeout=3)
    selector = etree.HTML(html.text)
    try:
        name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        director = selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        actors = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]
        actor = actors.xpath('string(.)')
        styles = re.findall('<span property="v:genre">(.*?)</span>', html.text, re.S)
        style = "/".join(styles)
        countrys = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>', html.text, re.S)
        country = "/".join(countrys)
        release_times = re.findall('<span property="v:initialReleaseDate".*?>(.*?)</span>', html.text, re.S)
        release_time = "/".join(release_times)
        time = re.findall('<span property="v:runtime".*?>(.*?)</span>', html.text, re.S)[0]
        score = selector.xpath('//*[@property="v:average"]/text()')[0]
        cursor.execute(
            "insert into doban_topmovie(name,director,actor,style,country,release_time,time,score) value (%s,%s,%s,%s,%s,%s,%s,%s)",
            (str(name),str(director),str(actor),str(style),str(country),str(release_time),str(time),str(score)))
    except IndexError:
        pass


if __name__ == '__main__':
    # ipmain.main()
    main()
