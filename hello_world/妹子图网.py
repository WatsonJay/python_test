import requests
from lxml import etree
import os
import shutil
import time
from hello_world import free_proxyIP

urls = ['https://www.mzitu.com/xinggan/page/{}/'.format(str(i)) for i in range(1, 10)]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
}
downpic_headers = {

}

def get_info_url(url):
    ip = free_proxyIP.proxyip()
    Proxy_Ip = {'http': ip}
    html = requests.get(url, headers=headers, proxies=Proxy_Ip, timeout=3)
    selector = etree.HTML(html.text)
    pic_info_refs = selector.xpath('//ul[@id="pins"]/li/a/@href')
    for pic_info_url in pic_info_refs:
        get_pics(pic_info_url)

def get_pics(pic_info_url):
    ip = free_proxyIP.proxyip()
    Proxy_Ip = {'http': ip}
    html = requests.get(pic_info_url, headers=headers, proxies=Proxy_Ip, timeout=3)
    selector = etree.HTML(html.text)
    pic_total = selector.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0]
    title = selector.xpath('//h2[@class="main-title"]/text()')[0]
    pic_url_list = []
    for i in range(int(pic_total)):
        link ='{}/{}'.format(pic_info_url,i+1)
        html = requests.get(link, headers=headers, timeout=3)
        selector = etree.HTML(html.text)
        jpg = selector.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        pic_url_list.append(jpg)
    downloadPic(title, pic_url_list)

def downloadPic(title, pic_url_list):
    k=1
    # 图片数量
    count = len(pic_url_list)
    # 文件夹格式
    dirName = u"girl_picture/%s[%sP]" % (title, str(count))
    topdirName = u"%s[%sP]" % (title, str(count))
    # 新建文件夹
    if topdirName not in os.listdir('./girl_picture'):
        os.mkdir(dirName)
    else:
        shutil.rmtree(dirName)
        os.mkdir(dirName)
    for pic_url in pic_url_list:
        filename = '%s/%s/%s.jpg' % (os.path.abspath('.'), dirName, k)
        print(u'开始下载图片:%s 第%s张' % (dirName, k))
        with open(filename, "wb") as jpg:
            jpg.write(requests.get(pic_url, headers=header(pic_url)).content)
            time.sleep(1)
        k += 1

def header(referer):
    headers = {
        'Accept':'image/webp,*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'i.meizitu.net',
        'Referer':'{}'.format(referer),
        'TE':'Trailers',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
    }
    return headers

if __name__ == '__main__':

    for url in urls :
        get_info_url(url)