import os
import time

import requests
#json解析库,对应到lxml
import json
#json的解析语法，对应到xpath
import jsonpath
from lxml import etree
from hello_world import free_proxyIP

urls = ['https://photo.fengniao.com/ajaxPhoto.php?action=getPhotoLists&fid=403&sort=1&page={}/'.format(str(i)) for i in range(1, 10)]
headers = {'Host': 'photo.fengniao.com',
            'X-Requested-With':'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
                          }
def get_info_url(url,page):
    is_exists = os.path.exists("./fengniao")
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs("./fengniao")
    ip = free_proxyIP.proxyip()
    ip = free_proxyIP.proxyip()
    Proxy_Ip = {'http': ip}
    html = requests.get(url, headers=headers, proxies=Proxy_Ip, timeout=3)
    # 把json形式的字符串转换成python形式的Unicode字符串
    unicodestr = json.loads(html.text)
    # python形式的列表
    pic_list = jsonpath.jsonpath(unicodestr, "$..picUrl")
    for i,pic_url in enumerate(pic_list):
        html = requests.get("https://photo.fengniao.com/"+pic_url, headers=headers, proxies=Proxy_Ip, timeout=3)
        selector = etree.HTML(html.text)
        pic = selector.xpath('//a[@class="downPic"]/@href')[0]
        title = selector.xpath('//h3[@class="title overOneTxt"]/text()')[0]
        filename = '%s/%s/%s.jpg' % (os.path.abspath('.'), "fengniao", str(page)+"-"+str(i+1)+"-"+title)
        print(u'开始下载图片:%s/%s' % ("fengniao", str(page)+"-"+str(i+1)+"-"+title))
        with open(filename, "wb") as jpg:
            jpg.write(requests.get(pic).content)
            time.sleep(1)


if __name__ == '__main__':
    for i,url in enumerate(urls):
        get_info_url(url,i+1)